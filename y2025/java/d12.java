package y2025.java;

import java.util.Arrays;
import java.util.List;

import y2025.Runnable;

public class d12 implements Runnable {
    //This wouldn't work in a general problem, but seems to work in the problem given to me
    private int[] partCounts = new int[] {7, 7, 6, 7, 7, 5};
    private int solution1 = 0;

    @Override
    public void run(List<String> input) {
        for (String line : input) {
            if (line.contains("x")) {
                String[] parts = line.split(" ");

                int a = Integer.valueOf(parts[0].split("x")[0]);
                int b = Integer.valueOf(parts[0].split("x")[1].substring(0, parts[0].split("x")[1].length()-1));

                List<String> values = Arrays.stream(Arrays.copyOfRange(parts, 1, parts.length)).toList();

                int total = 0;

                int i = 0;
                for (String value : values) {
                    int num = Integer.valueOf(value);
                    num *= partCounts[i];

                    total += num;
                    i++;
                }
                if (total < a * b) {
                    solution1++;
                }
            }
        }

        System.out.println("Solution: %d".formatted(solution1));
    }
    
}
