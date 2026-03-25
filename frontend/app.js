// Event-Listener für den "Visualisieren" Button
document.getElementById('visualize-btn').addEventListener('click', async () => {
    try {
        // 1. Code aus der editor.js holen
        const code = window.getEditorCode();
        const selectedVisType = document.getElementById('vis-type').value;

        const requestPayload = {
            visualization_type: selectedVisType,
            files: [
                { filename: "Main.java", code: code, language: "java" }
            ]
        };

        // 2. Daten ans Backend schicken
        const response = await fetch('http://127.0.0.1:8000/api/parse', { // Achte auf deinen aktuellen Port
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(requestPayload)
        });

        if (!response.ok) {
            throw new Error(`HTTP-Fehler! Status: ${response.status}`);
        }

        const data = await response.json();

        // 3. Daten an die graph.js zum Zeichnen übergeben
        window.renderGraph(data);

    } catch (error) {
        console.error("Fehler beim Visualisieren:", error);
    }
});