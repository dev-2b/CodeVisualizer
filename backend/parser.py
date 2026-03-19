
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

