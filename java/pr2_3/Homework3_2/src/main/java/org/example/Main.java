package org.example;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
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
        t.join();
        t.printState();
    }
}