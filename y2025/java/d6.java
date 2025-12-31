package y2025.java;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import y2025.Runnable;

public class d6 implements Runnable {
    private List<List<Integer>> numbers = new ArrayList<>();
    private List<String> operators = new ArrayList<>();
    private long solution1 = 0;
    private long solution2 = 0;

    @Override
    public void run(List<String> input) {
        for (int i = 0; i < Stream.of(input.get(0).split(" ")).filter(item -> !item.isEmpty()).count(); i++) {
            numbers.add(new ArrayList<>());
        }
        for (String line : input) {
            int lineCount = 0;
            List<String> parts = Stream.of(line.trim().split(" ")).filter(item -> !item.isEmpty()).toList();

            if (parseInt(parts.get(0)) != 0) {
                for (int index = 0; index < parts.size(); index++) {
                    numbers.get(lineCount).add(Integer.parseInt(parts.get(index)));
                    lineCount++;
                }
            } else {
                operators = parts;
            }
        }

        solution1 = calculateTotals(numbers, operators);

        List<List<Long>> part2Numbers = parsePart2Lines(input, operators.size());

        solution2 = calculateTotals(part2Numbers, operators);

        System.out.println("Part 1: %d".formatted(solution1));
        System.out.println("Part 2: %d".formatted(solution2));
    }

    private List<List<Long>> parsePart2Lines(List<String> input, int columns) {
        List<List<Long>> ans = new ArrayList<>();
        for (int i = 0; i < columns; i++) {
            ans.add(new ArrayList<>());
        }

        int i = 0;
        int column = 0;
        while (column < columns) {
            while (i < input.get(0).length()) {
                final int index = i;
                String columnNumbers = input.stream().map(value -> value.substring(index, index+1)).collect(Collectors.joining(""));

                if (columnNumbers.trim().isBlank()) {
                    break;
                }
                
                Long number = Long.parseLong(columnNumbers.substring(0, columnNumbers.length()-1).trim());
                ans.get(column).add(number);
                i++;
            }
            i++;
            column++;
        }

        return ans;
    }

    private long calculateTotals(List<? extends List<? extends Number>> numbers2, List<String> operators2) {
        long answer = 0;
        for (int i = 0; i < operators2.size(); i++) {
            long ans = 0;
            if (operators2.get(i).equals("*")) {
                ans = 1;
                for (Number num : numbers2.get(i)) {
                    ans *= num.longValue();
                }
            } else if (operators2.get(i).equals("+")) {
                for (Number num : numbers2.get(i)) {
                    ans += num.longValue();
                }
            } else {
                throw new IllegalArgumentException("Not a valid operator");
            }
            answer += ans;
        }
        return answer;
    }

    private int parseInt(String number) {
        try {
            return Integer.parseInt(number);
        } catch (NumberFormatException e) {
            return 0;
        }
    }
    
}
