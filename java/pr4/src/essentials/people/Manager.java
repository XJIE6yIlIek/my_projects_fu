package essentials.people;

import essentials.library.Book;
import essentials.library.Library;

import java.util.ArrayList;

public class Manager extends Employee {

    public Manager( String name, String last_name, String middle_name, String address) {
        super(name, last_name, middle_name, address);
    }

    public void add_book(Book book) {
        if (this.library == null) return;
        library.add_book(book);
    }

    public void add_book(ArrayList<Book> book) {
        if (this.library == null) return;
        for (Book bk : book) library.add_book(bk);
    }
}
