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

        # Wir übergeben jetzt die ID des Eltern-Knotens an die nächste Ebene
        def traverse(cursor, parent_id=None):
            nonlocal node_counter  # Erlaubt den Zugriff auf den Zähler außerhalb der Funktion
            
            node = cursor.node
            current_id = node_counter
            node_counter += 1
            
            # Das Label für vis.js zusammenbauen
            label = node.type
            
            # Wenn der Knoten keine Kinder mehr hat (ein "Blatt" am Baum ist), 
            # hängen wir den tatsächlichen Code-Text an das Label an
            if node.child_count == 0:
                text = node.text.decode('utf8')
                # Verhindert, dass Zeilenumbrüche das Layout zerschießen
                text = text.replace('\n', '\\n').replace('\r', '')
                
                # Wenn Typ und Text identisch sind (bei anonymen Knoten wie "{"), 
                # zeigen wir es nicht doppelt an
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
            
            # Rekursiver Durchlauf
            if cursor.goto_first_child():
                traverse(cursor, current_id)  # Der aktuelle Knoten ist der Parent für die Kinder
                while cursor.goto_next_sibling():
                    traverse(cursor, current_id)
                cursor.goto_parent()

        # Start der Traversierung (der Root-Node hat keinen Parent, also None)
        traverse(cursor, None)

    return {"nodes": nodes, "edges": edges}