package y2025.java;

import java.util.List;

import y2025.Runnable;

public class d1 implements Runnable {
    private Direction direction = new Direction();
    public int count1 = 0;
    public int count2 = 0;

    @Override
    public void run(List<String> input) {
        for (String line : input) {
            int number = Integer.valueOf(line.substring(1, line.length()));
            if (line.charAt(0) == 'L') {
                direction.remove(this, number);
            } else {
                direction.add(this, number);
            }
            if (direction.isZero()) {
                count1++;
            }
        }
        System.out.println("Part 1: %d".formatted(count1));
        System.out.println("Part 2: %d".formatted(count2));
    }
    
    static class Direction {
        private int MAX_VALUE = 100;
        private int current = 50;

        void add(d1 item, int value) {
            current += value;

            if (current == 0) {
                item.count2 += 1;
            }

            if (current >= MAX_VALUE) {
                item.count2 += current / MAX_VALUE;
            }
            current = current % MAX_VALUE;
        }

        void remove(d1 item, int value) {
            int start = current;
            current -= value;

            if (current == 0 || (current < 0 && start > 0)) {
                item.count2 += 1;
            }

            if (current <= 0) {
                item.count2 += -current / MAX_VALUE;
            }
            current = (current + MAX_VALUE * ((-current / MAX_VALUE) + 1)) % MAX_VALUE;
        }

        boolean isZero() {
            return current == 0;
        }
    }
}