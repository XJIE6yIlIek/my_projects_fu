package essentials.menu;

import java.util.Scanner;
import java.util.Stack;

public class MenuManager {
    static public Stack<Menu> menus = new Stack<Menu>();
    public boolean isExit = false;

    public MenuManager(Menu menu) {
        menus.push(menu);
    }
    public void run() {
        // Бесконечный цикл, пока не нажали кнопку выход
        while (!this.isExit && !menus.isEmpty()) {
            Menu menu = menus.peek();
            Scanner in = new Scanner(System.in);
            menu.printMenu();
            int choice = in.nextInt();
            // Выбираем нажатый пункт меню и выполняем его код
            MenuEntry entry = menu.getEntries().get(choice - 1);
            entry.run();
            if (menu.isExit) menus.pop();
        }
    }

}
