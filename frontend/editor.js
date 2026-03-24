// Konfiguriere den Pfad zu den Monaco-Ressourcen
require.config({ paths: { 'vs': 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.45.0/min/vs' } });

// Eine globale Variable, damit wir später den Code auslesen können
let windowEditor;

// Lade das Hauptmodul des Editors
require(['vs/editor/editor.main'], function () {

    // Initialisiere den Editor im Container aus Issue 2a
    windowEditor = monaco.editor.create(document.getElementById('editor-container'), {
        value: [
            'public class Main {',
            '    public static void main(String[] args) {',
            '        System.out.println("Hello World");',
            '    }',
            '}'
        ].join('\n'),
        language: 'java',
        theme: 'vs-dark', // oder 'vs' für ein helles Theme
        automaticLayout: true // Sorgt dafür, dass sich der Editor an Fensteränderungen anpasst
    });
});

// Event-Listener für den Button
document.getElementById('visualize-btn').addEventListener('click', async () => {
    console.log("--- NEUER KLICK ---");
    console.log("1. Button-Klick wurde registriert!");

    try {
        // HINWEIS: Falls deine Variable anders heißt (z.B. window.editor), passe das hier an!
        const code = windowEditor.getValue();
        console.log("2. Code erfolgreich ausgelesen. Länge:", code.length, "Zeichen");

        const selectedVisType = document.getElementById('vis-type').value;
        console.log("3. Visualisierungs-Typ aus Dropdown:", selectedVisType);

        const requestPayload = {
            visualization_type: selectedVisType,
            files: [
                {
                    filename: "Main.java",
                    code: code,
                    language: "java"
                }
            ]
        };
        console.log("4. Payload fertig zusammengebaut:", requestPayload);

        console.log("5. Starte Fetch-Anfrage an das Backend...");
        const response = await fetch('http://localhost:8000/api/parse', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestPayload)
        });

        console.log("6. Antwort vom Server empfangen! HTTP Status:", response.status);

        if (!response.ok) {
            throw new Error(`HTTP-Fehler! Status: ${response.status}`);
        }

        const data = await response.json();
        console.log("7. JSON-Daten verarbeitet:", data);

        drawGraph(data);
        console.log("8. Graph erfolgreich gezeichnet!");

    } catch (error) {
        // Das fängt JEDEN Fehler ab und zwingt ihn in die Konsole
        console.error("!!! FEHLER ABGEFANGEN !!! ->", error);
    }
});

// Funktion zum Initialisieren von vis.js
function drawGraph(graphData) {
    // 1. Lass uns in der Konsole prüfen, was ankommt
    console.log("Daten vom Backend empfangen:", graphData);

    const container = document.getElementById('graph-container');

    // 2. Sicherheitsmaßnahme: Container leeren, falls Reste eines alten Graphen existieren
    container.innerHTML = "";

    // 3. WICHTIG: Die rohen Arrays übergeben, OHNE 'new vis.DataSet()'
    const data = {
        nodes: graphData.nodes,
        edges: graphData.edges
    };

    const options = {
        layout: {
            hierarchical: {
                enabled: true,
                direction: 'UD',       // UD = Up-Down (von oben nach unten)
                sortMethod: 'directed' // Beachtet die Richtung der Pfeile
            }
        },
        physics: {
            hierarchicalRepulsion: {
                nodeDistance: 150      // Abstand zwischen den Knoten
            }
        },
        nodes: {
            shape: 'box',           // 'box', 'ellipse', 'circle', 'database' etc.
            margin: 10,             // Innenabstand zum Text
            font: {
                face: 'monospace',  // Schriftart (gut für Code)
                size: 14
            },
            color: {
                background: '#D2E5FF',
                border: '#2B7CE9'
            }
        },
        edges: {
            arrows: 'to',           // Pfeilspitze am Ende der Linie
            color: '#848484',
            smooth: {
                type: 'cubicBezier' // Abgerundete Linienführung
            }
        }
    };

    // 4. Graph initialisieren
    new vis.Network(container, data, options);
}