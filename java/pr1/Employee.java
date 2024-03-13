import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Employee {

    public static void main(String[] args) {
        List<List<String>> storage = new_storage();
        storage_output(storage);
        System.out.println(search_id(storage));
        search_name_date(storage);
        search_name_date(storage);
        change_info(storage);
        storage_output(storage);
    }

    public static List<List<String>> new_storage() {

        Scanner in = new Scanner(System.in);
        List<List<String>> group = new ArrayList<List<String>>(100);
        String input = "null";

        while(group.size() < 100 && input != "") {

            System.out.println("Input employee's info or press Enter to stop the program: ");
            input = in.nextLine().replaceAll(",", " ");
            if(!input.isEmpty()) {
                List<String> info = Arrays.asList(input.split(" "));
                group.add(info);
            }

        }

        return group;

    }

    public static void storage_output(List<List<String>> group) {

            System.out.println(group);

    }

    public static List<String> search_id(List<List<String>> group) {

        Scanner in = new Scanner(System.in);
        System.out.println("Input employee's id for his info: ");
        String input = in.next();

        for(List<String> i : group) {
            if(i.getFirst().equals(input)) {
                return i;
            }
        }

        return null;

    }

    public static void search_name_date(List<List<String>> group) {

        Scanner in = new Scanner(System.in);
        System.out.println("Input name or date of birth of employee: ");
        String input = in.next();

        if(Character.isDigit(input.charAt(0))) {
            for(List<String> i : group) {
                if(i.get(3).equals(input)) {
                    System.out.println(i);
                }
            }
        } else {
            for(List<String> i : group) {
                if (i.get(1).equals(input)) {
                    System.out.println(i);
                }
            }
        }

    }

    public static void change_info(List<List<String>> group) {

        Scanner in = new Scanner(System.in);
        System.out.println("Input id of employee which info you want to change: ");
        Integer emp_id = in.nextInt();
        System.out.println("Input which detail you want to change (id - 0, name - 1, surname - 2, date of birth - 3, salary - 4, marital status - 5): ");
        Integer ind = in.nextInt();
        System.out.println("Input new info: ");
        String input = in.nextLine();

        search_id(group);

        group.get(emp_id).set(ind, input);

    }
}
// Сделал Задачу 1 (1, 2). Доделать 3, 4, 5 + тесты (узнать как писать эти тесты)