import java.util.Scanner;

public class fancy_function {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Введите свою фамилию:");
        String f = in.next();
        System.out.println("Введите своё имя:");
        String i = in.next();
        System.out.println("Введите своё отчество:");
        String o = in.next();
        System.out.printf("Здравствуйте, пользователь!\nВаша фамилия: %s\nВаше имя: %s\nВаше отчество: %s\nДобро пожаловать в систему!", f, i, o);
    }
}
