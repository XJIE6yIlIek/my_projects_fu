import java.util.HashMap;
import java.util.Scanner;
import java.io.File;

public class Dictionary {

    public static HashMap<String, String> filetoHashmap(String filename) {
        try {
            HashMap<String, String> dict = new HashMap<String, String>();
            Scanner in = new Scanner(System.in);
            File file = new File(filename);
            in = new Scanner(file);

            while (in.hasNextLine()) {
                String line = in.nextLine();
                String[] line_arr = line.split(":");
                dict.put(line_arr[0], line_arr[1]);
            }

            return dict;

        } catch (Exception ex) {
            ex.printStackTrace();
        }

        return null;
    }
}
