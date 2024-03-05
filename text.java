import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class text {

    public static void main(String[] args) throws FileNotFoundException {

        String str = input_text();
        int w = count_words(str);
        int[] l = count_letters(str);
        int s = count_spaces(str);
        int[] n = count_numbers(str);
        Object[] list = count_punc(str);
        int p = (int)list[0];
        String txt = list[1].toString();

        output_text(new Object[]{w, l, s, n, p, txt});

        for (int[] element : search()) {
            System.out.println(Arrays.toString(element));
        }

    }

    public static String input_text() throws FileNotFoundException {

        File file = new File("Input.txt");
        Scanner in = new Scanner(file);

        StringBuilder strb = new StringBuilder();

        while(in.hasNext()) {
            strb.append(in.nextLine());
            strb.append('\n');
        }

        return strb.toString();

    }

    public static int count_words(String str) {

        Scanner in = new Scanner(str);
        int i = 0;
        while(in.hasNext()) {
            in.next();
            i++;
        }

        return i;

    }

    public static int[] count_letters(String str) {

        int ul = 0;
        int ll = 0;
        for(char i : str.toCharArray()) {
            if(Character.isLowerCase(i)) {
                ll++;
            } else if(Character.isUpperCase(i)) {
                ul++;
            }
        }

        return new int[] {ll, ul, ll + ul};

    }

    public static int count_spaces(String str) {

        int r = 0;
        for(char i : str.toCharArray()) {
            if(i == ' ') {
                r++;
            }
        }

        return r;

    }

    public static int[] count_numbers(String str) {

        int i = 0;
        int f = 0;

        Scanner in = new Scanner(str);
        while(in.hasNext()) {
            if(in.hasNextInt()) {
                i++;
                int num = in.nextInt();
                System.out.printf("Hex: %s\n", Integer.toHexString(num));
            } else if(in.hasNextDouble()) {
                f++;
                double num = in.nextDouble();
                System.out.printf("Float: %.2f\n", num);
            } else {
                in.next();
            }
        }



        return new int[] {i, f};

    }

    public static Object[] count_punc(String str) {

        StringBuilder strb = new StringBuilder(str);

        int p = 0;
        for(int i = str.length() - 1; i >= 0; i--) {
            if(str.charAt(i) == '"' || str.charAt(i) == ',' || str.charAt(i) == '!' || str.charAt(i) == '?' || str.charAt(i) =='.') {
                p++;
                strb.deleteCharAt(i);
            }
        }

        return new Object[] {p, strb};

    }

    public static void output_text(Object[] list) throws FileNotFoundException {

        PrintWriter out = new PrintWriter(new File("Result.txt"));
        String w = String.format("Number of words: %d\n", (int)list[0]);
        String l = String.format("Number of letters (lower, upper, sum): %s\n", Arrays.toString((int[])list[1]));
        String s = String.format("Number of spaces: %d\n", (int)list[2]);
        String n = String.format("Number of numbers (int, float): %s\n", Arrays.toString((int[])list[3]));
        String p = String.format("Number of punctuation marks: %d\n", (int)list[4]);
        String txt = String.format("Redacted text:\n%s", list[5]);

        out.print(w);
        out.print(l);
        out.print(s);
        out.print(n);
        out.print(p);
        out.print(txt);

        out.close();

    }

    public static ArrayList<int[]> search() throws FileNotFoundException {

        Scanner in = new Scanner(System.in);
        System.out.print("Input your word: ");
        String word = in.next();
        File file = new File("Input.txt");
        Scanner reader = new Scanner(file);

        StringBuilder strb = new StringBuilder();
        strb.append(' ');
        while(reader.hasNext()) {
            strb.append(reader.nextLine());
            strb.append('\n');
        }
        strb.append(' ');

        ArrayList<int[]> result = new ArrayList<>();
        for(int i = 1; i < strb.length() - word.length(); i++) {
            if(strb.charAt(i) == word.charAt(0) && !Character.isAlphabetic(strb.charAt(i - 1)) && !Character.isAlphabetic(strb.charAt(i + word.length()))) {
                if(strb.substring(i, i + word.length()).equals(word)) {
                    result.add(new int[]{i, i + word.length() - 1});
                }
            }
        }

        return result;

    }

}
