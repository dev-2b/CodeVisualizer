// globale Optionen für die vis.js Netzwerk-Visualisierung
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

// Die Hauptfunktion, die von der app.js aufgerufen wird
window.renderGraph = function (data) {
    const container = document.getElementById('graph-container');
    const network = new vis.Network(container, data, options);

    // Klick-Listener für die Synchronisation
    network.on("click", function (params) {
        if (params.nodes.length > 0) {
            const nodeId = params.nodes[0];
            const clickedNode = data.nodes.find(n => n.id === nodeId);

            if (clickedNode && clickedNode.loc) {
                // Hier rufen wir die Funktion aus der editor.js auf
                window.highlightAstNode(clickedNode.loc);
            }
        }
    });
};