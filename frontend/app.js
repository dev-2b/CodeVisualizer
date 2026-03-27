// 1. NEU: Event-Listener für den Ordner-Upload
document.getElementById('folder-upload').addEventListener('change', async (event) => {
    const files = event.target.files;

    // HTML-Container leeren, falls vorher schon ein Ordner geladen wurde
    document.getElementById('editor-tabs').innerHTML = '';

    for (let file of files) {
        // Wir filtern nur nach .java Dateien
        if (file.name.endsWith('.java')) {
            const text = await file.text();
            window.addFileToEditor(file.name, text);
        }
    }
});

// 2. ANGEPASST: Visualisieren-Button
document.getElementById('visualize-btn').addEventListener('click', async () => {
    try {
        const selectedVisType = document.getElementById('vis-type').value;

        // Wir holen uns jetzt das komplette Array aller Dateien aus dem Editor
        const filesArray = window.getAllFiles();

        if (filesArray.length === 0) {
            alert("Bitte lade zuerst einen Ordner mit Java-Dateien hoch.");
            return;
        }

        const requestPayload = {
            visualization_type: selectedVisType,
            files: filesArray // Hier schicken wir jetzt die ganze Liste ans Backend
        };

        const response = await fetch('http://127.0.0.1:8000/api/parse', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(requestPayload)
        });

        if (!response.ok) throw new Error(`HTTP-Fehler! Status: ${response.status}`);

        const data = await response.json();
        window.renderGraph(data);

    } catch (error) {
        console.error("Fehler beim Visualisieren:", error);
    }
});