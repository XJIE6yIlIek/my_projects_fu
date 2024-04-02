package essentials.library;

import essentials.Identification;

public class Book extends Identification {



    int id, publish_year;
    String title, author, publish, publisher, category;

    public Book(String title, String author, String publish, String publisher, int publish_year, String category) {
        super();
        this.title = title;
        this.author = author;
        this.publish = publish;
        this.publisher = publisher;
        this.publish_year = publish_year;
        this.category = category;
    }

}
