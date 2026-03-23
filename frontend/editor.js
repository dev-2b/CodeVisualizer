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
    // Sicherstellen, dass der Editor schon geladen ist
    if (!windowEditor) return;

    // 1. Code aus dem Editor holen
    const code = windowEditor.getValue();

    try {
        // 2. Request an das Python-Backend senden
        const response = await fetch('http://localhost:8000/api/parse', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ code: code })
        });

        if (!response.ok) {
            throw new Error(`HTTP-Fehler! Status: ${response.status}`);
        }

        const data = await response.json();

        // 3. Den Graphen mit den empfangenen Daten zeichnen
        drawGraph(data);

    } catch (error) {
        console.error("Fehler bei der Kommunikation mit dem Backend:", error);
        alert("Fehler: Konnte keine Daten abrufen. Läuft der FastAPI-Server auf Port 8000?");
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
        nodes: {
            shape: 'box',
            color: '#97C2FC',
            font: {
                size: 16
            }
        }
    };

    // 4. Graph initialisieren
    new vis.Network(container, data, options);
}