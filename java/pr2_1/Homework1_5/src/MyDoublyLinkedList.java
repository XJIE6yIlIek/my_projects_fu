import java.util.Comparator;

public class MyDoublyLinkedList<T> {
    private Node<T> head;
    private Node<T> tail;
    private int size;

    public MyDoublyLinkedList() {
        this.head = null;
        this.tail = null;
        this.size = 0;

    }

    public void append(T data) {
        Node<T> newNode = new Node<>(data);
        if (head == null) {
            head = newNode;
            tail = newNode;
        } else {
            tail.next = newNode;
            newNode.prev = tail;
            tail = newNode;
        }
        size++;
    }

    public void insert(T data, int ind) {
        if (ind < 0 || ind > size) {
            throw new IndexOutOfBoundsException("Index out of bounds");
        }
        Node<T> newNode = new Node<>(data);
        if (ind == 0) {
            if (size == 0) {
                head = newNode;
                tail = newNode;
            } else {
                newNode.next = head;
                head.prev = newNode;
                head = newNode;
            }
        } else if (ind == size) {
            append(data);
        } else {
            Node<T> current = head;
            for (int i = 0; i < ind; i++) {
                current = current.next;
            }
            newNode.prev = current.prev;
            newNode.next = current;
            newNode.prev.next = newNode;
            current.prev = newNode;
        }
        size++;
    }

    public void delete(int ind) {
        if (ind < 0 || ind > size - 1) {
            throw new IndexOutOfBoundsException("Index out of bounds");
        }
        if (ind == 0) {
            head = head.next;
            head.prev = null;
        } else if (ind == size - 1) {
            tail = tail.prev;
            tail.next = null;
        } else {
            Node<T> current = head;
            for (int i = 0; i < ind; i++) {
                current = current.next;
            }
            current.next.prev = current.prev;
            current.prev.next = current.next;
        }
        size--;
    }

    public void replace(T data, int ind) {
        if (ind < 0 || ind > size - 1) {
            throw new IndexOutOfBoundsException("Index out of bounds");
        }
        Node<T> current = head;
        for (int i = 0; i < ind; i++) {
            current = current.next;
        }
        current.data = data;
    }

    public void sort(Comparator<T> comparator) {
        if (size <= 1) {
            return;
        }

        boolean swapped;
        do {
            swapped = false;
            Node<T> current = head;

            while (current.next != null) {
                if (comparator.compare(current.data, current.next.data) > 0) {
                    T temp = current.data;
                    current.data = current.next.data;
                    current.next.data = temp;
                    swapped = true;
                }
                current = current.next;
            }
        } while (swapped);
    }

    public void print() {
        Node<T> current = head;
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.next;
        }
        System.out.println();
    }
}
