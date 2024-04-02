package essentials.people;

import essentials.Identification;

public class Person extends Identification {

    int id;
    String name, last_name, middle_name, address;

    public Person(String name, String last_name, String middle_name, String address) {
        this.name = name;
        this.last_name = last_name;
        this.middle_name = middle_name;
        this.address = address;
    }

    @Override
    public String toString() {
        return String.format("%d - %s %s %s", this.id, this.name, this.last_name, this.middle_name);
    }


}
