let windowEditor;
let currentDecorations = [];

// 1. Monaco Initialisierung (bleibt wie sie ist)
require.config({ paths: { 'vs': 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.36.1/min/vs' } });
require(['vs/editor/editor.main'], function () {
    windowEditor = monaco.editor.create(document.getElementById('editor-container'), {
        value: 'class HelloWorld {\n    public static void main(String[] args) {\n        System.out.println("Hello, World!");\n    }\n}',
        language: 'java',
        theme: 'vs-dark'
    });
});

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