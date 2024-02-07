import java.util.Scanner;

public class examples {
    public static void example(int x, char [] s) {
        s[1] = 'x';
        x = -1;
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int x = 1;
        char [] xx = {'a', 'b', 'c'};
        boolean d = true;
        example(x, xx);
        System.out.println(xx);
        System.out.println(x);
//        String c = in.next();
//        System.out.println(c);
        System.out.printf("%.2f", 1f/9999999); System.out.println();

        System.out.printf("string example = %s," + " integer example = %x," + " boolean example = %b", "SSSS", 13, false);
    }
}