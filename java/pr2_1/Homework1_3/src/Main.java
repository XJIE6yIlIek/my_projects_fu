import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) {
        PriorityQueue<Client> queue = new PriorityQueue<>(new DistanceCompare());

        // Добавление клиентов в очередь
        queue.add(new Client("Андрей", 500));
        queue.add(new Client("Наталья", 700));
        queue.add(new Client("Сергей", 200));
        queue.add(new Client("Ольга", 600));
        queue.add(new Client("Дмитрий", 400));

        // Вызов клиентов в порядке очереди
        while (!queue.isEmpty()) {
            Client nextClient = queue.poll();
            System.out.println("Следующий клиент: " + nextClient);
        }
    }
}