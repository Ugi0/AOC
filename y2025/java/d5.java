package y2025.java;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

import y2025.Runnable;

public class d5 implements Runnable {
    private List<long[]> ranges = new ArrayList<>();
    private List<Marker> markers = new ArrayList<>();
    private int solution1 = 0;
    private long solution2 = 0;

    @Override
    public void run(List<String> input) {
        boolean parse = false;
        for (String line : input) {
            if (line.isBlank()) {
                parse = true;
                continue;
            }
            if (parse) {
                long value = Long.parseLong(line);
                for (long[] range : ranges) {
                    if (value >= range[0] && value <= range[1]) {
                        solution1++;
                        break;
                    }
                }
            } else {
                long[] range = new long[]{Long.parseLong(line.split("-")[0]), Long.parseLong(line.split("-")[1])};
                markers.add(new Marker(Long.parseLong(line.split("-")[0]), true));
                markers.add(new Marker(Long.parseLong(line.split("-")[1]), false));
                ranges.add(range);
            }
        }

        List<Marker> sorted = markers.stream().sorted(Comparator.comparing(Marker::getID).thenComparing(Marker::getOpen, Comparator.reverseOrder())).toList();
        long ID = 1;
        int opens = 0;
        for (Marker marker : sorted) {
            if (opens > 0) {
                solution2 += marker.ID - ID;
            }
            ID = marker.ID;

            opens += marker.open ? 1 : -1;

            if (opens == 0 && !marker.open) {
                solution2++;
            }
        }

        System.out.println("Part 1: %d".formatted(solution1));
        System.out.println("Part 2: %d".formatted(solution2));
    }
    private class Marker {
        public long ID;
        public boolean open;

        public Marker(long ID, boolean open) {
            this.ID = ID;
            this.open = open;
        }

        public long getID() {
            return ID;
        }

        public boolean getOpen() {
            return open;
        }
    } 
    
}
