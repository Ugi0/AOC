package y2025.java;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import y2025.Runnable;

public class d3 implements Runnable {
    private static int PART1_LENGTH = 2;
    private static int PART2_LENGTH = 12;
    private int solution1 = 0;
    private long solution2 = 0;
    
    @Override
    public void run(List<String> input) {
        for (String line : input) {
            List<Integer> voltages = Stream.of(line.split("")).map(Integer::parseInt).toList();

            int ans1 = getPart1Number(voltages);
            long ans2 = getPart2Number(voltages);
            solution1 += ans1;
            solution2 += ans2;
        }

        System.out.println("Part 1: %d".formatted(solution1));
        System.out.println("Part 2: %d".formatted(solution2));
    }

    private int getPart1Number(List<Integer> voltages) {
        int leftPieces = PART1_LENGTH;
        int[] first = getLargestAndIndex(voltages.subList(0, voltages.size() - leftPieces + 1));
        leftPieces--;
        int[] second = getLargestAndIndex(voltages.subList(first[0] + 1, voltages.size() - leftPieces + 1));

        return first[1] * 10 + second[1];
    }

    private long getPart2Number(List<Integer> voltages) {
        int leftPieces = PART2_LENGTH;
        int[] found = new int[12];
        int cumulIndex = 0;
        while (leftPieces != 0) {
            int[] val = getLargestAndIndex(voltages.subList(cumulIndex, voltages.size() - leftPieces + 1));
            found[leftPieces - 1] = val[1];
            cumulIndex += val[0] + 1;
            leftPieces--;
        }

        String answer = Arrays.stream(found).mapToObj(String::valueOf).collect(Collectors.joining());
        String reversed = new StringBuilder(answer).reverse().toString();
        return Long.parseLong(reversed);
    }

    private int[] getLargestAndIndex(List<Integer> voltages) {
        int value = voltages.subList(0, voltages.size()).stream().reduce(Integer::max).get();
        int index = voltages.indexOf(value);
        
        return new int[] {index, value};
    }
    
}
