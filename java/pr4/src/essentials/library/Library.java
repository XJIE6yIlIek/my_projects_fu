package essentials.library;

import essentials.people.Employee;
import essentials.people.Manager;
import essentials.people.Person;
import essentials.people.Reader;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Library {

    ArrayList<Employee> employees = new ArrayList<Employee>();
    int books_amount = 0;
    int taken_books_cnt = 0;
    // Book_id, Person_id
    Map<Integer, Integer> taken_books = new HashMap<Integer, Integer>();
    Map<String, Integer> books_category_cnt = new HashMap<String, Integer>();
    private ArrayList<Book> books = new ArrayList<Book>();

    public ArrayList<Book> get_books() {
        return this.books;
    }

    public void take_book(int book_id, int person_id) {
        taken_books.put(book_id, person_id);
        taken_books_cnt++;
    }

    public void return_book(int book_id) {
        taken_books.remove(book_id);
        taken_books_cnt--;
    }

    public void add_book(Book book) {
        books.add(book);
        books_amount++;
    }

    public void del_book(Book book) {
        return;
    }

    public Manager get_any_manager() {
        ArrayList<Manager> ppl = this.get_managers();
        if (!ppl.isEmpty()) {
            return ppl.getFirst();
        }
        return null;
    }

    public Employee get_any_employee() {
        ArrayList<Employee> ppl = this.get_employees();
        if (!ppl.isEmpty()) {
            return ppl.getFirst();
        }
        return null;
    }

    public ArrayList<Manager> get_managers() {
        ArrayList<Manager> managers = new ArrayList<>();

        for (Object obj : this.employees) {
            if (obj instanceof Manager) {
                managers.add((Manager) obj);
            }
        }

        return managers;
    }

    public ArrayList<Employee> get_employees() {
        ArrayList<Employee> employees = new ArrayList<>();

        for (Object obj : this.employees) {
            if (obj instanceof Employee) {
                employees.add((Employee) obj);
            }
        }

        return employees;
    }

    public Reader add_employee(Person person) {
        if (person instanceof Manager) {
            this.employees.add((Manager) person);
            ((Manager) person).setLibrary(this);
            return null;
        } else if (person instanceof Employee) {
            this.employees.add((Employee) person);
            ((Employee) person).setLibrary(this);
            return null;
        }
        return (Reader) person;
    }

    public ArrayList<Reader> add_employee(ArrayList<Person> persons) {
        ArrayList<Reader> ppl = new ArrayList<Reader>();
        for (Person person : persons) {
            Reader p = this.add_employee(person);
            if (p!= null) ppl.add(p);
        }
        return ppl;
    }

}
