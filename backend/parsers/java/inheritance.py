import tree_sitter_java as tsjava
from tree_sitter import Language, Parser

JAVA_LANGUAGE = Language(tsjava.language())
parser = Parser()
parser.language = JAVA_LANGUAGE

def extract(files: list) -> dict:
    nodes_dict = {}
    edges = []

    for file_obj in files:
        tree = parser.parse(bytes(file_obj.code, "utf8"))
        cursor = tree.root_node.walk()

        def traverse(cursor):
            node = cursor.node
            
            # Wir suchen nur nach Klassen und Interfaces
            if node.type == "class_declaration" or node.type == "interface_declaration":
                
                # 1. Den eigenen Namen der Klasse/des Interfaces extrahieren
                name_node = node.child_by_field_name("name")
                if name_node:
                    class_name = name_node.text.decode('utf8')
                    
                    # Knoten anlegen, falls er noch nicht existiert
                    if class_name not in nodes_dict:
                        # Klassen pink, Interfaces hellorange
                        color = "#FFC0CB" if node.type == "class_declaration" else "#FFE4B5"
                        nodes_dict[class_name] = {
                            "id": class_name, 
                            "label": class_name, 
                            "shape": "box",
                            "color": color
                        }
                    
                    # 2. Superklasse suchen (extends)
                    superclass_node = node.child_by_field_name("superclass")
                    if superclass_node:
                        for child in superclass_node.children:
                            if child.type == "type_identifier":
                                parent_name = child.text.decode('utf8')
                                
                                # Elternklasse als Knoten anlegen, falls sie nicht im Code definiert wurde
                                if parent_name not in nodes_dict:
                                    nodes_dict[parent_name] = {"id": parent_name, "label": parent_name, "shape": "box", "color": "#D3D3D3"}
                                
                                # Kante hinzufügen (Pfeil zeigt von Kind zu Elternklasse)
                                edges.append({
                                    "from": class_name, 
                                    "to": parent_name, 
                                    "label": "extends",
                                    "arrows": "to"
                                })

                    # 3. Interfaces suchen (implements)
                    interfaces_node = node.child_by_field_name("interfaces")
                    if interfaces_node:
                        for child in interfaces_node.children:
                            if child.type == "type_list":
                                for type_node in child.children:
                                    if type_node.type == "type_identifier":
                                        interface_name = type_node.text.decode('utf8')
                                        
                                        if interface_name not in nodes_dict:
                                            nodes_dict[interface_name] = {"id": interface_name, "label": interface_name, "shape": "box", "color": "#FFE4B5"}
                                        
                                        # Gestrichelte Kante für Interfaces (UML-Standard)
                                        edges.append({
                                            "from": class_name, 
                                            "to": interface_name, 
                                            "label": "implements",
                                            "arrows": "to",
                                            "dashes": True 
                                        })
                                        
            # Rekursion: Weiter in die Tiefe und Breite suchen
            if cursor.goto_first_child():
                traverse(cursor)
                while cursor.goto_next_sibling():
                    traverse(cursor)
                cursor.goto_parent()

        traverse(cursor)

    # Das Dictionary wieder in eine flache Liste für vis.js umwandeln
    return {"nodes": list(nodes_dict.values()), "edges": edges}