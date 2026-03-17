# Mitwirken am Code Visualizer

Willkommen im Team! Dieses Dokument beschreibt unseren gemeinsamen Git-Workflow. Bitte lies dir diese Regeln durch, bevor du mit der Arbeit an einem Issue beginnst, damit wir Konflikte im Code (Merge Conflicts) vermeiden und die Code-Qualität hoch halten.

## 1. Ein Issue finden und zuweisen
* Schau im Reiter **Issues** nach offenen Aufgaben.
* Wenn du an einem Issue arbeiten möchtest, weise es dir selbst zu (Assignees) oder schreibe einen kurzen Kommentar: *"Ich übernehme das."*
* Arbeite im Idealfall immer nur an einem Issue gleichzeitig, um den Fokus zu behalten.

## 2. Der Git Workflow (Feature Branches)
Wir arbeiten **niemals** direkt auf dem `main`-Branch. Für jede neue Aufgabe (jedes Issue) erstellen wir einen eigenen Branch.

1. **Aktualisiere deinen lokalen main-Branch:**
   Bevor du startest, hole dir immer den neuesten Stand vom Server:
   `git checkout main`
   `git pull origin main`

2. **Erstelle einen neuen Branch:**
   Der Branch-Name sollte beschreiben, woran du arbeitest, und die Issue-Nummer enthalten.
   **Namenskonvention:** `art/issue-nummer-kurzbeschreibung`
   * *Features (Neue Funktionen):* `feature/12-add-monaco-editor`
   * *Bugfixes (Fehlerbehebungen):* `bugfix/15-fix-cors-error`
   * *Docs (Dokumentation):* `docs/3-update-readme`
   
   Befehl zum Erstellen und Wechseln:
   `git checkout -b feature/12-add-monaco-editor`

## 3. Commits schreiben
* Mache regelmäßig Commits, wenn ein logischer Zwischenschritt fertig und lauffähig ist.
* Schreibe aussagekräftige Commit-Nachrichten.
* **Schlecht:** *"Code geändert"* oder *"Fix"* oder *"Test"*
* **Gut:** *"Füge vis-network Bibliothek via CDN in index.html hinzu"* oder *"Integriere FastAPI CORS Middleware"*

## 4. Pull Requests (PR) erstellen
Sobald dein Code fertig ist und lokal fehlerfrei funktioniert, integrieren wir ihn in den `main`-Branch:

1. Lade deinen Branch auf GitHub hoch:
   `git push -u origin dein-branch-name`
2. Gehe auf GitHub und klicke auf den grünen Button **Compare & pull request**.
3. Beschreibe in deinem PR kurz, was du gemacht hast. Verlinke das zugehörige Issue, indem du in die Beschreibung schreibst: *"Closes #12"*. (Dadurch wird das Issue auf GitHub automatisch geschlossen, sobald der PR gemerged wird).
4. **Code Review:** Ein anderes Teammitglied muss deinen PR prüfen. Das Vier-Augen-Prinzip hilft uns, Fehler früh zu finden.
5. Nach der Freigabe (Approve) wird der Code vom Maintainer in den `main`-Branch gemerged. Danach kannst du deinen Branch lokal und remote löschen.

## 5. Code-Richtlinien
* **Backend (Python):** Achte auf saubere Einrückungen (4 Leerzeichen, keine Tabs). Wir orientieren uns am PEP 8 Standard.
* **Frontend (JS/HTML/CSS):** Nutze sprechende Variablen- und Funktionsnamen auf Englisch (z.B. `renderGraph()` statt `rg()`). Kommentiere komplexe Logikblöcke.
