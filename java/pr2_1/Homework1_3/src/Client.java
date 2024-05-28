class Client implements Comparable<Client> {
    private String name;
    private int distance;

    public Client(String name, int distance) {
        this.name = name;
        this.distance = distance;
    }

    public String getName() {
        return name;
    }

    public int getDistance() {
        return distance;
    }

    @Override
    public int compareTo(Client other) {
        return Integer.compare(other.distance, distance);
    }

    @Override
    public String toString() {
        return "Клиент " + name + ", дистанция до клиента = " + distance;
    }
}
