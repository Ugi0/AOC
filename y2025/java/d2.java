package y2025.java;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import y2025.Runnable;

public class d2 implements Runnable {
    private long MAX_NUMBER = 10000000000L;
    private Long[] illegalNumbers1;
    private Long[] illegalNumbers2;
    private long solution1 = 0;
    private long solution2 = 0;

    @Override
    public void run(List<String> input) {
        generateIllegalNumbers();
        for (String value : input.get(0).split(",")) {
            Range range = new Range(value.split("-")[0], value.split("-")[1]);

            int index = binarySearch(illegalNumbers1, 0, illegalNumbers1.length, range.start);
            int count = 0;

            if (illegalNumbers1[index] >= range.start && illegalNumbers1[index] <= range.end) {
                while (illegalNumbers1[index + count] <= range.end) {
                    solution1 += illegalNumbers1[index + count];
                    count++;
                } 
            }
            count = 0;
            while (illegalNumbers2[index + count] <= range.end) {
                if (illegalNumbers2[index + count] >= range.start) {
                    solution2 += illegalNumbers2[index + count];
                }
                count++;
            } 
        }

        System.out.println("Part 1: %d".formatted(solution1));
        System.out.println("Part 2: %d".formatted(solution2));
    }

    private void generateIllegalNumbers() {
        Set<Long> il1 = new HashSet<>();
        Set<Long> il2 = new HashSet<>();

        for (int i = 1; i < 999999; i++) {
            il1.add(Long.parseLong("%d%d".formatted(i,i)));
            int count = 2;
            while (true) {
                Long value = Long.parseLong(String.valueOf(i).repeat(count));
                if (value < MAX_NUMBER) {
                    il2.add(value);
                    count++;
                } else {
                    break;
                }
            }
        }
        List<Long> illegal1 = new ArrayList<>(il1);
        List<Long> illegal2 = new ArrayList<>(il2);
        Collections.sort(illegal1);
        Collections.sort(illegal2);

        illegalNumbers1 = illegal1.toArray(new Long[illegal1.size()]);
        illegalNumbers2 = illegal2.toArray(new Long[illegal2.size()]);
    }

    private class Range {
        public long start;
        public long end;

        public Range(String start, String end) {
            this.start = Long.parseLong(start);
            this.end = Long.parseLong(end);
        }
    }

    int binarySearch(Long a[], int l, int r, long x){
        while (l <= r){
            int m = (l + r) / 2;
            // Index of Element Returned
            if (a[m] == x) {
                return m;
                // If element is smaller than mid, then
                // it can only be present in left subarray
                // so we decrease our r pointer to mid - 1
            } else if (a[m] > x) {
                r = m - 1;
                // Else the element can only be present
                // in right subarray
                // so we increase our l pointer to mid + 1
            } else {
                l = m + 1;
            }
        }
        return l;
    }
}
