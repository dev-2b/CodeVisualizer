from parsers.java import ast as java_ast
# Hier kommen später Imports für Python oder andere Module hin

def get_visualisation(files: list, vis_type: str) -> dict:
    # Sicherheitscheck: Wenn keine Dateien übergeben wurden, leeres Dict zurückgeben
    if not files:
        return {"nodes": [], "edges": []}
    
    # Fürs Erste bestimmen wir die Sprache anhand der ersten Datei
    lang = files[0].language.lower()

    if vis_type == "ast":
        if lang == "java":
            return java_ast.extract(files)
        # elif lang == "python":
        #     return python_ast.extract(files)
        else:
            raise ValueError(f"Sprache '{lang}' wird für AST noch nicht unterstützt.")
            
    # Platzhalter für spätere Typen
    elif vis_type == "inheritance":
        raise ValueError("Inheritance-Visualisierung ist noch nicht implementiert.")
    elif vis_type == "dataflow":
        raise ValueError("Dataflow-Visualisierung ist noch nicht implementiert.")
    else:
        raise ValueError(f"Visualisierungstyp '{vis_type}' ist unbekannt.")