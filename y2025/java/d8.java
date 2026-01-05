package y2025.java;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

import y2025.Runnable;

public class d8 implements Runnable {
    private int CONNECTIONS = 1000;

    private List<Point> points = new ArrayList<>();
    private Map<Point, Integer> groups = new HashMap<>();
    private Map<Pair<Point, Point>, Double> distances = new HashMap<>();

    @Override
    public void run(List<String> input) {
        int i = 0;
        for (String line : input) {
            String[] parts = line.split(",");
            int x = Integer.parseInt(parts[0]);
            int y = Integer.parseInt(parts[1]);
            int z = Integer.parseInt(parts[2]);

            points.add(new Point(x, y, z));
            groups.put(new Point(x, y, z), i);
            i++;
        }

        for (Point p1 : points) {
            for (Point p2 : points) {
                if (p1 == p2) break;

                distances.put(new Pair<d8.Point,d8.Point>(p1, p2), 
                    Math.sqrt(
                        Math.pow(Math.abs((double) p1.x - (double) p2.x), 2) +
                        Math.pow(Math.abs((double) p1.y - (double) p2.y), 2) +
                        Math.pow(Math.abs((double) p1.z - (double) p2.z), 2)
                    )
                );
            }
        }

        distances.entrySet().stream().sorted(Map.Entry.comparingByValue()).limit(CONNECTIONS).forEach(item -> {
            Integer group = groups.get(item.getKey().first);
            Integer old = groups.get(item.getKey().second);

            distances.remove(item.getKey());

            groups.replaceAll((key, value) ->
                value.equals(old) ? group : value
            );
        });

        List<Integer> top3 =
            groups.entrySet()
                .stream()
                .map(entry -> entry.getValue())
                .distinct()
                .map(entry -> Collections.frequency(groups.values(), entry))
                .sorted(Comparator.reverseOrder())
                .limit(3)
                .toList();

        System.out.println("Task 1: %d".formatted(top3.get(0) * top3.get(1) * top3.get(2)));

        Point first = null;
        Point second = null;
        for (Entry<Pair<Point, Point>, Double> entry : distances.entrySet().stream().sorted(Map.Entry.comparingByValue()).toList()) {
            if (groups.values().stream().distinct().count() == 1) break;
            
            first = entry.getKey().first;
            second = entry.getKey().second;

            Integer group = groups.get(first);
            Integer old = groups.get(second);

            groups.replaceAll((key, value) ->
                value.equals(old) ? group : value
            );
        }

        System.out.println("Task 2: %d".formatted(first.x * second.x));
    }

    private class Pair<K, V> {
        private final K first;
        private final V second;

        public Pair(K key, V value) {
            this.first = key;
            this.second = value;
        }

        @Override
        public boolean equals(Object o) {
            return o instanceof Pair val && val.first.equals(this.first) && val.second.equals(this.second);
        }

        @Override
        public int hashCode() {
            return 31 * first.hashCode() + second.hashCode();
        }
    }

    private class Point {
        private int x;  
        private int y;
        private int z;

        public Point(int x, int y, int z) {
            this.x = x;
            this.y = y;
            this.z = z;
        }

        @Override
        public boolean equals(Object o) {
            return o instanceof Point val && val.x == this.x && val.y == this.y && val.z == this.z;
        }

        @Override
        public int hashCode() {
            return 31 * 31 * x + 31 * y + z;
        }

        @Override
        public String toString() {
            return "%d %d %d".formatted(x, y, z);
        }
        
    }
    
}
