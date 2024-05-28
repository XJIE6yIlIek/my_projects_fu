import java.util.HashMap;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String input = "";
        HashMap<String, String> dict = Dictionary.filetoHashmap("dictionary.txt");
        while (!input.equals("Exit")) {
            System.out.println("Введите слово для поиска по словарю:");
            input = in.next();
            if (dict.containsKey(input)) {
                System.out.println(dict.get(input));
            } else if (!input.equals("Exit")) System.out.println("Данное слово отсутствует в словаре");
        }
    }
}
