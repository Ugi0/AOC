package y2025.java;

import java.util.HashMap;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;
import java.util.List;
import java.util.Map;
import java.util.stream.IntStream;
import y2025.Runnable;

public class d10 implements Runnable {
    private Map<Unit, Integer> visited = new HashMap<>();
    private Deque<Unit> queue = new ArrayDeque<>();
    private int[] lights;
    private List<int[]> buttons;
    private int[] joltages;
    private int solution1 = 0;
    private int solution2 = 0;

    @Override
    public void run(List<String> input) {
        for (String line : input) {
            queue.clear();
            visited.clear();
            String[] parts = line.split(" ");
            //System.out.println(line);

            lights = parts[0].substring(1, parts[0].length()-1).chars().map(part -> part == '.' ? 0 : 1).toArray();

            buttons = Arrays.stream(parts, 1, parts.length - 1)
                    .map(s ->
                        Arrays.stream(s.substring(1, s.length() - 1).split(","))
                            .mapToInt(Integer::parseInt)
                            .toArray()
                    )
                    .toList();

            joltages = Arrays.stream(parts[parts.length-1].substring(1, parts[parts.length-1].length()-1).split(",")).mapToInt(Integer::parseInt).toArray();

            queue.add(new Unit(0, new int[lights.length]));

            while (!queue.isEmpty()) {
                Unit current = queue.pop();
                if (visited.containsKey(current)) {
                    continue;
                }
                visited.put(current, current.depth);

                if (Arrays.equals(current.current, lights)) {
                    solution1 += current.depth;
                    break;
                }

                for (int[] button : buttons) {
                    queue.add(new Unit(current.depth + 1, 
                        IntStream.range(0, current.current.length).map(index -> current.current[index] ^ (Arrays.stream(button).anyMatch(x -> x == index) ? 1 :0)).toArray()
                    ));
                }
            }

            queue.clear();
            visited.clear();
            queue.add(new Unit(0, new int[lights.length]));

            ParitySolver solver = new ParitySolver(joltages, buttons);
            solution2 += solver.solve();
        }

        System.out.println("Part 1: %d".formatted(solution1));
        System.out.println("Part 2: %d".formatted(solution2));
    }

    private class Unit {
        private int depth;
        private int[] current;

        public Unit(int depth, int[] current) {
            this.depth = depth;
            this.current = current;
        }

        @Override
        public boolean equals(Object o) {
            return o instanceof Unit unit && Arrays.equals(this.current, unit.current);
        }

        @Override
        public int hashCode() {
            return Arrays.hashCode(current);
        }
    }

    private static class Combo {
        int presses;
        int[] joltage;

        Combo(int presses, int[] joltage) {
            this.presses = presses;
            this.joltage = joltage;
        }
    }

    public class ParitySolver {
        private final int[] initialJoltage;
        private final List<int[]> buttons;

        private Map<String, List<Combo>> combosByPattern;
        private Map<String, Integer> cache;

        public ParitySolver(int[] initialJoltage, List<int[]> buttons) {
            this.initialJoltage = initialJoltage;
            this.buttons = buttons;
            buildCombos();
        }

        private void buildCombos() {
            combosByPattern = new HashMap<>();

            int buttonCount = buttons.size();
            int comboCount = 1 << buttonCount;

            for (int mask = 0; mask < comboCount; mask++) {
                int[] joltage = new int[initialJoltage.length];
                int presses = 0;

                for (int b = 0; b < buttonCount; b++) {
                    if (((mask >> b) & 1) == 1) {
                        presses++;
                        for (int idx : buttons.get(b)) {
                            joltage[idx]++;
                        }
                    }
                }

                String pattern = parityPattern(joltage);
                combosByPattern
                    .computeIfAbsent(pattern, k -> new ArrayList<>())
                    .add(new Combo(presses, joltage));
            }
        }

        public int solve() {
            cache = new HashMap<>();
            return countPresses(initialJoltage);
        }

        private int countPresses(int[] target) {
            String key = Arrays.toString(target);

            Integer cached = cache.get(key);
            if (cached != null) return cached;

            boolean allZero = true;
            for (int v : target) {
                if (v < 0) return Integer.MAX_VALUE;
                if (v != 0) allZero = false;
            }

            if (allZero) return 0;

            String pattern = parityPattern(target);
            List<Combo> combos = combosByPattern.get(pattern);

            if (combos == null) {
                cache.put(key, Integer.MAX_VALUE);
                return Integer.MAX_VALUE;
            }

            int best = Integer.MAX_VALUE;

            for (Combo combo : combos) {
                int[] half = new int[target.length];
                boolean valid = true;

                for (int i = 0; i < target.length; i++) {
                    int diff = target[i] - combo.joltage[i];
                    if ((diff & 1) != 0) {
                        valid = false;
                        break;
                    }
                    half[i] = diff >> 1;
                }

                if (!valid) continue;

                int sub = countPresses(half);
                if (sub == Integer.MAX_VALUE) continue;

                int presses = combo.presses + (sub << 1);
                best = Math.min(best, presses);
            }

            cache.put(key, best);
            return best;
        }

        private String parityPattern(int[] joltage) {
            StringBuilder sb = new StringBuilder(joltage.length);
            for (int v : joltage) {
                sb.append(v & 1);
            }
            return sb.toString();
        }
    }



}
