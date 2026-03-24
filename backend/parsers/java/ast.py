import tree_sitter_java as tsjava
from tree_sitter import Language, Parser

JAVA_LANGUAGE = Language(tsjava.language())
parser = Parser()
parser.language = JAVA_LANGUAGE

def extract(files: list) -> dict:
    nodes = []
    edges = []
    
    # Ein globaler Zähler für eindeutige vis.js IDs
    node_counter = 0

    for file_obj in files:
        tree = parser.parse(bytes(file_obj.code, "utf8"))
        cursor = tree.root_node.walk()

        # Elternknoten-ID wmuss jetzt mit übergeben werden, damit die Kanten korrekt erstellt werden können
        def traverse(cursor, parent_id=None):
            nonlocal node_counter  # Erlaubt den Zugriff auf den Zähler außerhalb der Funktion --> Tipp von KI kannte ich nicht, aber es ist notwendig, damit die IDs eindeutig bleiben
            
            node = cursor.node
            current_id = node_counter
            node_counter += 1
            
            # Das Label für vis.js zusammenbauen
            label = node.type
            
            
            if node.child_count == 0:
                text = node.text.decode('utf8')
                # Verhindert, dass Zeilenumbrüche das Layout zerschießen
                text = text.replace('\n', '\\n').replace('\r', '')
                
                # Wenn Typ und Text identisch sind (bei anonymen Knoten wie "{"), eigen wir es nicht doppelt an
                if label != text:
                    label += f"\n({text})"

            # Knoten hinzufügen
            nodes.append({
                "id": current_id,
                "label": label
            })
            
            # Kante zum Elternknoten hinzufügen (außer beim allerersten Wurzelknoten)
            if parent_id is not None:
                edges.append({
                    "from": parent_id,
                    "to": current_id
                })
            
            # Rekursion (Tiefensuche) mit Übergabe der aktuellen Knoten-ID als Eltern-ID für die Kinder
            if cursor.goto_first_child():
                traverse(cursor, current_id)  # Der aktuelle Knoten ist der Parent für die Kinder
                while cursor.goto_next_sibling():
                    traverse(cursor, current_id)
                cursor.goto_parent()

        # Start der Traversierung (None, weil der Wurzelknoten keinen Elternknoten hat)
        traverse(cursor, None)

    return {"nodes": nodes, "edges": edges}