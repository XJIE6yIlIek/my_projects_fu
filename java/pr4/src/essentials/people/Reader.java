package essentials.people;

import essentials.library.Book;

import java.util.ArrayList;

public class Reader extends Person {

    ArrayList<Book> taken_books = new ArrayList<Book>();

    public Reader( String name, String last_name, String middle_name, String address) {
        super(name, last_name, middle_name, address);
    }

    Book get_book(Employee employee, String query) {
        return null;
    }
}
