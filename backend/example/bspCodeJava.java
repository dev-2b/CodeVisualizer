class Task {
    private String title;
    private boolean isCompleted;

    public Task(String title) {
        this.title = title;
        this.isCompleted = false;
    }

    public void complete() {
        this.isCompleted = true;
    }

    public String getTitle() {
        return this.title;
    }
    
    public boolean checkStatus() {
        return this.isCompleted;
    }
}

public class TaskManager {
    public static void main(String[] args) {
        // Array initialisieren
        Task[] myTasks = new Task[3];
        myTasks[0] = new Task("Frontend bauen");
        myTasks[1] = new Task("Backend fixen");
        myTasks[2] = new Task("AST analysieren");

        // Eine Aufgabe als erledigt markieren
        myTasks[0].complete();

        System.out.println("Offene Aufgaben:");
        
        // Schleife und Kontrollstrukturen testen
        for (int i = 0; i < myTasks.length; i++) {
            if (!myTasks[i].checkStatus()) {
                System.out.println("- " + myTasks[i].getTitle());
            }
        }
    }
}