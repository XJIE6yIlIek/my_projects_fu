import java.util.Objects;
import java.util.Scanner;

public class calculator {
    public static void main(String[] args) {
        int result = 0;
        Scanner in = new Scanner(System.in);
        System.out.println("Введите первое значение:");
        int a = in.nextInt();
        System.out.println("Введите второе значение:");
        int b = in.nextInt();
        System.out.println("Введите действие (+ - / *):");
        String d = in.next();
        if (Objects.equals(d, "+"))
        {
            result = a + b;
        }
        else if (Objects.equals(d, "-"))
        {
            result = a - b;
        }
        else if (Objects.equals(d, "*"))
        {
            result = a * b;
        }
        else if (Objects.equals(d, "/"))
        {
            result = a / b;
        }
        else
        {
            System.out.println("Введена неподдерживаемая операция");
        }
        System.out.println(result);
    }
}
