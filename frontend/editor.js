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