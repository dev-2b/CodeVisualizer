let windowEditor;
let currentDecorations = [];
let fileModels = {}; // Speichert die Monaco-Models (Dateien)

// 1. Monaco Initialisierung (bleibt wie sie ist)
require.config({ paths: { 'vs': 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.36.1/min/vs' } });
require(['vs/editor/editor.main'], function () {
    windowEditor = monaco.editor.create(document.getElementById('editor-container'), {
        // value: 'class HelloWorld {\n    public static void main(String[] args) {\n        System.out.println("Hello, World!");\n    }\n}',
        // language: 'java',
        theme: 'vs-dark'
    });
});


// Nimmt eine neue Datei auf, erstellt ein Model und einen klickbaren Tab
window.addFileToEditor = function (filename, code) {
    // Ein neues Monaco-Model für die Datei erstellen
    const model = monaco.editor.createModel(code, 'java');
    fileModels[filename] = model;

    // Einen Tab in der HTML-Leiste erzeugen
    const tab = document.createElement('div');
    tab.innerText = filename;
    tab.style.padding = '8px 15px';
    tab.style.cursor = 'pointer';
    tab.style.borderRight = '1px solid #444';
    tab.style.userSelect = 'none';

    // Beim Klick auf den Tab das Model im Editor austauschen
    tab.onclick = () => {
        windowEditor.setModel(model);

        // Alle Tabs etwas abdunkeln und den aktiven hervorheben
        document.querySelectorAll('#editor-tabs div').forEach(t => t.style.background = 'transparent');
        tab.style.background = '#1e1e1e';
    };

    document.getElementById('editor-tabs').appendChild(tab);

    // Wenn es die allererste Datei ist, klicken wir den Tab direkt virtuell an, 
    // damit der Editor nicht leer bleibt
    if (Object.keys(fileModels).length === 1) {
        tab.click();
    }
};

// Holt alle geladenen Dateien für den Versand ans Backend
window.getAllFiles = function () {
    return Object.keys(fileModels).map(filename => ({
        filename: filename,
        code: fileModels[filename].getValue(),
        language: "java"
    }));
};

// 2. Neue Hilfsfunktion für die app.js: Holt den aktuellen Code
window.getEditorCode = function () {
    return windowEditor.getValue();
};

// 3. Neue Hilfsfunktion für die graph.js: Setzt das Highlighting
window.highlightAstNode = function (loc) {
    windowEditor.revealRangeInCenter({
        startLineNumber: loc.startLineNumber,
        startColumn: loc.startColumn,
        endLineNumber: loc.endLineNumber,
        endColumn: loc.endColumn
    });

    currentDecorations = windowEditor.deltaDecorations(currentDecorations, [
        {
            range: new monaco.Range(
                loc.startLineNumber, loc.startColumn,
                loc.endLineNumber, loc.endColumn
            ),
            options: { inlineClassName: 'ast-highlight' }
        }
    ]);
};