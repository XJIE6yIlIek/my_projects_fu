public interface Animal {

    default void make_sound(){
        System.out.println("Making some sounds");
    }

    default void move(){
        System.out.println("Moving around");
    }

    default void eat(){
        System.out.println("Eating food");
    }

    default void sleep(){
        System.out.println("Sleeping...");
    }
}
