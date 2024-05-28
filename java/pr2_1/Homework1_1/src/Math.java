import java.util.ArrayDeque;
import java.util.Stack;

public class Math {

    public static boolean checkExprBalance(String expr) {
        ArrayDeque<Character> expr_arr = new ArrayDeque<>();

        for (char ch:expr.toCharArray()) {
            if (ch == '(' || ch == '[' || ch == '{') {
                expr_arr.push(ch);
            } else if (ch == ')' || ch == ']' || ch == '}') {
                if (expr_arr.isEmpty()) return false;
                char top_ch = expr_arr.pop();
                if ((ch == ')' && top_ch != '(') ||
                        (ch == ']' && top_ch != '[') ||
                        (ch == '}' && top_ch != '{')) {
                    return false;
                }
            }
        }
        return expr_arr.isEmpty();
    }
}
