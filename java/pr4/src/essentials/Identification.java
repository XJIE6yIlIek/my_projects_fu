package essentials;

public class Identification {

    static int current_id = 0;
    int id;

    public Identification() {
        this.id = Identification.current_id;
        Identification.current_id++;
    }
}
