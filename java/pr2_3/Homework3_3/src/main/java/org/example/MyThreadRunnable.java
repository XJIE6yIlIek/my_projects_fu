package org.example;

public class MyThreadRunnable extends Thread {
    private Thread t;
    private final String name;
    private final Object obj;
    public MyThreadRunnable(String name)
    {
        this.name=name;
        obj=new Object();
    }

    @Override
    public void run() {
        printState();
        try {
            //Make thread sleep for 2000 milliseconds
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
        synchronized (obj) {
            try {
                //make the thread wait until it is notified
                obj.wait();
            } catch (InterruptedException ex) {
                throw new RuntimeException(ex);
            }
        }
        printState();
    }

    public void start()
    {
        t=new Thread(this,name);
        printState();
        t.start();
    }

    public void printState()
    {
        //print the current state of the thread
        System.out.println("Thread state after waiting: " + t.getState());
    }

    public void join(int millis) {
        try {
            t.join(millis);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
    }

    public void threadNotify()
    {
        synchronized (obj) {
            obj.notify();
        }
    }
}
