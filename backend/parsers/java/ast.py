import tree_sitter_java as tsjava
from tree_sitter import Language, Parser

# Tree-sitter Setup für Java
JAVA_LANGUAGE = Language(tsjava.language())
parser = Parser()
parser.language = JAVA_LANGUAGE

def extract(files: list) -> dict:
    """
    Parst eine Liste von CodeFile-Objekten und extrahiert die Klassen
    für die vis.js Visualisierung.
    """
    nodes = []
    edges = []

    # Iteriere über alle Dateien, die vom Frontend gesendet wurden
    for file_obj in files:
        tree = parser.parse(bytes(file_obj.code, "utf8"))
        cursor = tree.root_node.walk()

        def traverse(cursor):
            node = cursor.node
            
            if node.type == "class_declaration":
                name_node = node.child_by_field_name("name")
                if name_node:
                    text = name_node.text
                    class_name = text.decode('utf8') if isinstance(text, bytes) else text
                    
                    nodes.append({
                        "id": class_name,
                        "label": class_name
                    })
            
            # Rekursiver Durchlauf
            if cursor.goto_first_child():
                traverse(cursor)
                while cursor.goto_next_sibling():
                    traverse(cursor)
                cursor.goto_parent()

        # Starte die Traversierung für den aktuellen AST
        traverse(cursor)

    return {"nodes": nodes, "edges": edges}