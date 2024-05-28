package org.example;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        System.out.println("The different states of a thread are: ");
        List<Thread.State> states = new ArrayList<>();
        // Iterate through all enum constants and add them to the list
        for (Thread.State state:Thread.State.values()) {
            states.add(state);
        }
        for(Thread.State state:states)
        {
            System.out.print(state+" ");
        }
        System.out.print("\nLet's get practical:\n");
        MyThreadRunnable t = new MyThreadRunnable("Thread States");
        t.start();
        //wait 500 milliseconds for the thread to die
        t.join(500);
        t.printState();
        t.join(3000);
        t.printState();
        //Notify thread to wake up
        t.threadNotify();
        t.printState();
        //wait forever for the thread to die
        try {
            t.join();
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
        t.printState();
        // Поток t всё ещё RUNNABLE, хотя он и "умер". Это может быть связано с тем, что в данной реализации класса
        // MyThreadRunnable происходит наследование Thread и в данном случае состояние потока не успевает обновиться
        // (это можно проверить, просто выводя состояние потока 2-3 раза, вместо одного, последние 2 (или 1) вывода
        // состояния выведут состояние TERMINATED)
    }
}