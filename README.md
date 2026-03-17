# Code Visualizer

Ein interaktives Full-Stack-Tool zur Visualisierung von Code-Strukturen. Das Programm parst Quellcode und generiert daraus dynamische, interaktive Graphen (Klassen, Abhängigkeiten und Kontrollfluss). Ziel ist es, Entwicklern einen schnellen visuellen Überblick über Workflows in fremden Codebases zu geben.

## Tech-Stack

* **Backend:** Python, FastAPI, Tree-sitter (generiert den Abstract Syntax Tree)
* **Frontend:** HTML, CSS, Vanilla JavaScript
* **Code-Editor:** Monaco Editor (Syntax-Highlighting)
* **Graph-Visualisierung:** vis.js (vis-network)

## Voraussetzungen

* [Python 3.10+](https://www.python.org/downloads/)
* [Git](https://git-scm.com/)
* Ein Code-Editor (empfohlen: Visual Studio Code)

## Lokales Setup für die Entwicklung

Da das Projekt aus einem separierten Backend und Frontend besteht, müssen für die lokale Entwicklung zwei Server gestartet werden.

### 1. Repository klonen
```bash
git clone https://github.com/DEIN_USERNAME/CodeVisualizer.git
cd CodeVisualizer
```

### 2. Backend starten
Öffne ein Terminal und wechsle in den Backend-Ordner:
```bash
cd backend
```
Erstelle und aktiviere eine virtuelle Umgebung:
* **Windows:** `python -m venv venv` und danach `venv\Scripts\activate`
* **macOS/Linux:** `python3 -m venv venv` und danach `source venv/bin/activate`

Installiere die benötigten Abhängigkeiten:
```bash
pip install -r requirements.txt
```

Starte den lokalen FastAPI-Server (mit Auto-Reload für die Entwicklung):
```bash
uvicorn main:app --reload
```
Das Backend läuft nun unter `http://localhost:8000`. Die interaktive API-Dokumentation (Swagger UI) ist unter `http://localhost:8000/docs` erreichbar.

### 3. Frontend starten
Öffne ein **zweites, neues Terminal** und wechsle in den Frontend-Ordner:
```bash
cd frontend
```
Um CORS-Probleme (Cross-Origin Resource Sharing) beim Laden der Module zu vermeiden, solltest du die `index.html` nicht einfach per Doppelklick öffnen, sondern einen simplen lokalen Webserver nutzen. Das geht direkt mit Python:
```bash
python -m http.server 8080
```
*(Alternativ kannst du in VS Code die Erweiterung "Live Server" nutzen).*

Öffne nun deinen Browser und navigiere zu `http://localhost:8080`.

## Nutzung (Meilenstein 1)

1. Die Web-App öffnet sich im Split-Screen-Design.
2. Füge gültigen Java-Code in den Monaco Editor auf der linken Seite ein.
3. Klicke auf den Button "Code visualisieren".
4. Auf der rechten Seite wird der dynamische Graph gerendert. Du kannst die Knotenpunkte frei verschieben und in die Ansicht hineinzoomen.

## Mitwirken (Contributing)

Wenn du an diesem Projekt mitarbeiten möchtest, lies dir bitte zuerst unsere [CONTRIBUTING.md](CONTRIBUTING.md) durch. Dort sind unsere Namenskonventionen für Branches, das Erstellen von Pull Requests und unsere Code-Richtlinien definiert.
