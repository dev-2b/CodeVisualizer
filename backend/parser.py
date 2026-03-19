
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
    return tree.root_node

# --- Issue #6: Klassen extrahieren ---
class_query = JAVA_LANGUAGE.Query("""
    (class_declaration
        name: (identifier) @class_name
    )
""")

def extract_classes_to_visjs(root_node) -> dict:
    """
    Nimmt den Root-Node eines AST, durchsucht ihn nach Klassennamen
    und gibt ein Dictionary im vis.js-Format zurück.
    """
    nodes = []
    edges = []
    
    captures = class_query.captures(root_node)
    
    if "class_name" in captures:
        # captures["class_name"] ist eine Liste von Nodes
        for node in captures["class_name"]:
            class_name = node.text.decode('utf8')
            nodes.append({
                "id": class_name,
                "label": class_name
            })

    return {"nodes": nodes, "edges": edges}