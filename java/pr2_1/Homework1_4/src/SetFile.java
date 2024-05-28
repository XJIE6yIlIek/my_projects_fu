import java.io.*;
import java.util.Scanner;
import java.util.TreeSet;

public class SetFile {

    public static void CreateSetFile(String filename, String output_filename) throws IOException {

        TreeSet<String> words_set = new TreeSet<>();
        Scanner in = new Scanner(new File(filename));
        FileWriter wr = new FileWriter(output_filename);
        String input;
        while (in.hasNextLine()) {
            input = in.nextLine();
            String[] words = input.split("\\s+");
            for (String word : words) {
                word = word.replaceAll("[^a-zA-Z0-9]", "");
                if (!words_set.contains(word)) {
                    words_set.add(word);
                }
            }
        }
        for (String word:words_set) {
            wr.write(word + " ");
        }
        wr.close();
    }
}
