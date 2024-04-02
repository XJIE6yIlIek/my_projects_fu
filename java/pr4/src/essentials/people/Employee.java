package essentials.people;

import essentials.library.Book;
import essentials.library.Library;

public class Employee extends Person {

    protected Library library = null;
    public Employee(String name, String last_name, String middle_name, String address) {
        super(name, last_name, middle_name, address);
    }

    Book find_book(String query) {
        return null;
    }

    public void setLibrary(Library library) {
        this.library = library;
    }
}
