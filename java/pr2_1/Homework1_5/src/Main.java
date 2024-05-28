public class Main {
    public static void main(String[] args) {
        MyDoublyLinkedList<Integer> lst = new MyDoublyLinkedList<Integer>();
        lst.append(5);
        lst.append(3);
        lst.append(8);
        lst.append(123);
        lst.print();
        lst.insert(78, 2);
        lst.print();
        lst.delete(0);
        lst.print();
        lst.replace(600, 3);
        lst.print();
        lst.sort(Integer::compareTo);
        lst.print();
    }
}