import essentials.library.Book;
import essentials.library.Library;
import essentials.menu.Menu;
import essentials.menu.MenuEntry;
import essentials.menu.MenuManager;
import essentials.people.Employee;
import essentials.people.Manager;
import essentials.people.Person;
import essentials.people.Reader;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static ArrayList<Book> load_books() throws FileNotFoundException {
        ArrayList<Book> books = new ArrayList<Book>();
        Scanner in = new Scanner(new File("books.txt"));
        try {
            while (in.hasNext()) {
                String[] book_info = in.nextLine().split("|");
                Book book = new Book(book_info[0], book_info[1], book_info[2], book_info[3], Integer.parseInt(book_info[4]), book_info[5]);
                books.add(book);
            }
        }catch (Exception e) {
            System.out.println("Error while reading books!");
        }

        return books;
    }

    public static ArrayList<Person> load_people() throws FileNotFoundException {
        ArrayList<Person> ppl = new ArrayList<>();
        Scanner in = new Scanner(new File("people.txt"));
        try {
            while (in.hasNext()) {
                String[] role = in.nextLine().split(":");
                String[] person_info = role[1].split("\\|");
                switch (role[0]) {
                    case "Manager":
                        Manager manager = new Manager(person_info[0], person_info[1], person_info[2], person_info[3]);
                        ppl.add(manager);
                        break;
                    case "Employee":
                        Employee employee = new Employee(person_info[0], person_info[1], person_info[2], person_info[3]);
                        ppl.add(employee);
                        break;
                    case "Reader":
                        Reader reader = new Reader(person_info[0], person_info[1], person_info[2], person_info[3]);
                        ppl.add(reader);
                        break;
                    default:
                        break;
                }
            }
        } catch (Exception e) {
            System.out.println("Error while reading ppl!");
        }
        return ppl;
    }

    public static void main(String[] args) throws FileNotFoundException {
        // Creating library and loading everything from files
        Library library = new Library();
        ArrayList<Reader> readers = library.add_employee(load_people());

        Manager manager = library.get_any_manager();
        if (manager != null) {
            manager.add_book(load_books());
        } else {
            System.out.println("No manager found!");
            return;
        }

        Menu menu = new Menu("Choose your role:"); // TODO: Make all of menu entries
        menu.addEntry(new MenuEntry("Manager") {
            @Override
            public void run() {
                menu.forceExit();
            }
        });
        menu.addEntry(new MenuEntry("Employee") {
            @Override
            public void run() {
                menu.forceExit();
            }
        });
        menu.addEntry(new MenuEntry("Reader") {
            @Override
            public void run() {
                Menu menu = new Menu("One of accounts:");
                for (Reader reader : readers) {
                    menu.addEntry(new MenuEntry(String.valueOf(reader)) {
                        @Override
                        public void run() {
                            Menu choose_employee = new Menu("Choose one of employee:");
                            for (Employee emp : library.get_employees()) {
                                choose_employee.addEntry(new MenuEntry(String.valueOf(emp)) {
                                    @Override
                                    public void run() {
                                        Menu reader_menu = new Menu("Choose an action:");
                                        reader_menu.addEntry(new MenuEntry("Take book") {
                                            @Override
                                            public void run() {
                                                Menu choose_book = new Menu("Choose a book to take:");
                                                for (Book bk : library.get_books()) {
                                                    choose_book.addEntry(new MenuEntry(String.valueOf(bk)) {
                                                        @Override
                                                        public void run() {
                                                            // FIXME
                                                        }
                                                    });
                                                }
                                            }
                                        });
                                        reader_menu.addEntry(new MenuEntry("Return book") {
                                            @Override
                                            public void run() {
                                                System.out.println("gay!"); // FIXME
                                                System.out.println(reader);
                                            }
                                        });
                                        MenuManager.menus.push(reader_menu);
                                    }
                                });
                            }
                            MenuManager.menus.push(choose_employee);
                        }
                    });
                }
                MenuManager.menus.push(menu);
            }
        });

        MenuManager menuManager = new MenuManager(menu);
        menuManager.run();
    }
}