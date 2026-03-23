
import tree_sitter_java as tsjava
from tree_sitter import Language, Parser

# Sprache initailisieren
JAVA_LANGUAGE = Language(tsjava.language())
# Parser initialisieren
parser = Parser()
parser.language = JAVA_LANGUAGE


def get_ast(java_code: str):
    """
    Nimmt Java-Quellcode als String, parst ihn und gibt 
    den Root-Node des Abstract Syntax Tree zurück.
    """
    tree = parser.parse(bytes(java_code, "utf8"))

    # 1. Prüfen: Kommt der Code überhaupt im Backend an?
    print("--- EMPFANGENER CODE ---")
    print(java_code)
    
    tree = parser.parse(bytes(java_code, "utf8"))
    
    # 2. Prüfen: Wie sieht der von Tree-sitter gebaute Baum aus?
    print("--- AST STRUKTUR ---")
    print(tree.root_node)


    return tree

def extract_classes_to_visjs(root_node) -> dict:
    nodes = []
    edges = []
    
    print("--- STARTE EXTRAKTION ---")

    # Initialisiere den offiziellen TreeCursor
    cursor = root_node.walk()

    def traverse(cursor):
        node = cursor.node
        
        if node.type == "class_declaration":
            name_node = node.child_by_field_name("name")
            if name_node:
                text = name_node.text
                class_name = text.decode('utf8') if isinstance(text, bytes) else text
                print(f"-> Klasse extrahiert: {class_name}")
                
                nodes.append({
                    "id": class_name,
                    "label": class_name
                })
        
        # Rekursiver Durchlauf mit dem Cursor
        if cursor.goto_first_child():
            traverse(cursor)
            while cursor.goto_next_sibling():
                traverse(cursor)
            cursor.goto_parent()

    traverse(cursor)
    
    print("--- EXTRAKTION BEENDET, GEFUNDENE KNOTEN:", nodes, "---")
    return {"nodes": nodes, "edges": edges}