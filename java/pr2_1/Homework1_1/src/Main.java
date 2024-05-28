public class Main {
    public static void main(String[] args) {
        System.out.println(String.format("Синтаксис выражения {(1+2+3)(5-2)*3}-5 верный - %b",
                Math.checkExprBalance("{(1+2+3)(5-2)*3}-5")));
        System.out.println(String.format("Синтаксис выражения {1+2+3)(5-2)*3}-5 верный - %b",
                Math.checkExprBalance("{1+2+3)(5-2)*3}-5")));
    }
}