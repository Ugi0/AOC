package y2025.java;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import y2025.Runnable;

public class d11 implements Runnable {
    private Map<String, String[]> connections = new HashMap<>();
    private Map<Seen, Long> visited = new HashMap<>();
    private int solution1 = 0;
    private long solution2 = 0;

    @Override
    public void run(List<String> input) {
        for (String line : input) {
            String[] parts = line.split(" ");

            connections.put(parts[0].substring(0, parts[0].length()-1), Arrays.copyOfRange(parts, 1, parts.length));
        }

        solution1 = recur("you");
        solution2 = recur2("svr", false, false);

        System.out.println("Part 1: %d".formatted(solution1));
        System.out.println("Part 2: %d".formatted(solution2));
    }

    private class Seen {
        private final boolean dac;
        private final boolean fft;
        private final String node;

        private Seen(String node, boolean dac, boolean fft) {
            this.node = node;
            this.dac = dac;
            this.fft = fft;
        }

        @Override
        public boolean equals(Object o) {
            return o instanceof Seen seen && this.dac == seen.dac && this.fft == seen.fft && this.node.equals(seen.node);
        }

        @Override
        public int hashCode() {
            int result = Boolean.hashCode(dac);
            result = 31 * result + Boolean.hashCode(fft);
            result = 31 * result + (node != null ? node.hashCode() : 0);
            return result;
        }
    }

    private int recur(String point) {
        int count = 0;
        for (String connection : connections.get(point)) {
            if (connection.equals("out")) {
                return 1;
            } else {
                count += recur(connection);
            }
        }
        return count;
    }

    private long recur2(String point, boolean dac, boolean fft) {
        dac |= point.equals("dac");
        fft |= point.equals("fft");
        Seen key = new Seen(point, dac, fft);
        Long cached = visited.get(key);
        if (cached != null) {
            return cached;
        }
        long count = 0;
        for (String connection : connections.get(point)) {
            if (connection.equals("out")) {
                count += (dac && fft) ? 1 : 0;
            } else {
                count += recur2(connection, dac, fft);
            }
        }

        visited.put(key, count);
        return count;
    }
    
}
