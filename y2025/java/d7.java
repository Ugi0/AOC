package y2025.java;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import y2025.Runnable;

public class d7 implements Runnable {
    private Map<Coordinate, Long> memo = new HashMap<>();

    private List<Coordinate> splitters = new ArrayList<>();
    private List<Coordinate> visited = new ArrayList<>();
    private Set<String> fullPaths = new HashSet<>();
    private Coordinate startPoint;
    private int maxDistance;
    private int solution1 = 0;
    private long solution2 = 0;

    @Override
    public void run(List<String> input) {
        int lineIndex = 0;
        maxDistance = input.size();
        for (String line : input) {
            int charIndex = -1;
            for (char c : line.toCharArray()) {
                charIndex++;
                if (c == '.') continue;

                if (c == '^') {
                    splitters.add(new Coordinate(lineIndex, charIndex));
                } else if (c == 'S') {
                    startPoint = new Coordinate(lineIndex, charIndex);
                }
            }
            lineIndex++;
        }

        String path = "S";
        solution2 = recur(new Coordinate(startPoint.x + 1, startPoint.y), path);

        System.out.println("Part 1: %d".formatted(solution1));
        System.out.println("Part 2: %d".formatted(solution2));
    }

    private long recur(Coordinate current, String currentPath) {
        if (memo.containsKey(current)) {
            return memo.get(current);
        }

        if (current.x > maxDistance) {
            fullPaths.add(currentPath);
            memo.put(current, 1L);
            return 1;
        }

        if (splitters.contains(current)) {
            if (!visited.contains(current)) {
                solution1++;
                visited.add(current);
            }
            long value1 = recur(new Coordinate(current.x, current.y + 1), currentPath.concat("^"));
            long value2 = recur(new Coordinate(current.x, current.y - 1), currentPath.concat("^"));

            memo.put(current, value1 + value2);

            return value1 + value2;
        }

        currentPath = currentPath.concat(".");

        long value = recur(new Coordinate(current.x + 1, current.y), currentPath);
        memo.put(current, value);
        return value;
    }

    private class Coordinate {
        public int x;
        public int y;

        public Coordinate(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object o) {
            return o instanceof Coordinate val && val.x == this.x && val.y == this.y;
        }

        @Override
        public int hashCode() {
            return 31 * x + y;
        }
    }
    
}
