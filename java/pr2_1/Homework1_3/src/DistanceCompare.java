import java.util.Comparator;

public class DistanceCompare implements Comparator<Client> {
    @Override
    public int compare(Client client1, Client client2) {
        return Integer.compare(client2.getDistance(), client1.getDistance());
    }

}
