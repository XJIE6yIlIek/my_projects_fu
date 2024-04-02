package essentials.menu;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Menu {
    private String menuText;
    private ArrayList<MenuEntry> entries = new ArrayList();
    public boolean isExit = false;

    public void printMenu() {
        System.out.println(this.menuText);
        for (int i = 0; i < entries.size(); i++) {
            System.out.println((i + 1) + ". " + entries.get(i).getName());
        }
    }

    public Menu(String menuText) {
        this.menuText = menuText;
        // Добавляем пункт меню Exit
        entries.add(new MenuEntry("Exit") {
            @Override
            public void run() {
                isExit = true;
            }
        });
    }

    public void addEntry(MenuEntry entry) {
        entries.addFirst(entry);
    }

    public void forceExit() {
        isExit = true;
    }

    public ArrayList<MenuEntry> getEntries() {
        return this.entries;
    }
}
