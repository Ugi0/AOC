package y2025.java;

import java.util.ArrayList;
import java.util.List;

import y2025.Runnable;

public class d4 implements Runnable {
    private char[][] map;
    private int[][] surrounding = {
        {-1, -1}, {-1, 0}, {-1, 1},
        { 0, -1},          { 0, 1},
        { 1, -1}, { 1, 0}, { 1, 1}
    };
    private int solution1 = 0;

    @Override
    public void run(List<String> input) {
        map = new char[input.size()][input.get(0).length()];
        int index = 0;
        for (String line : input) {
            map[index] = line.toCharArray();
            index++;
        }


        for (int i = 0; i < map.length; i++) {
            for (int j = 0; j < map[0].length; j++) {
                if (map[i][j] == '@') {
                    if (countSurroundingRolls(i, j) < 4) {
                        solution1++;
                    }
                }
            }
        }
        int start = countRolls();

        int current = 0;
        List<int[]> removed = new ArrayList<>();
        do {
            current = countRolls();
            for (int i = 0; i < map.length; i++) {
                for (int j = 0; j < map[0].length; j++) {
                    if (map[i][j] == '@') {
                        if (countSurroundingRolls(i, j) < 4) {
                            removed.add(new int[] {i, j});
                        }
                    }
                }
            }
            for (int[] remove : removed) {
                map[remove[0]][remove[1]] = '.';
            }
        } while (current != countRolls());
        

        System.out.println("Part 1: %d".formatted(solution1));
        System.out.println("Part 2: %d".formatted(start - countRolls()));
    }

    private int countSurroundingRolls(int i, int j) {
        int count = 0;
        for (int[] direction : surrounding) {
            if (isRoll(i + direction[0], j + direction[1])) {
                count++;
            }
        }
        return count;
    }

    private int countRolls() {
        int ans = 0;
        for (int i = 0; i < map.length; i++) {
            for (int j = 0; j < map[0].length; j++) {
                if (map[i][j] == '@') {
                    ans++;
                }
            }
        }
        return ans;
    }

    private boolean isRoll(int i, int j) {
        if (i < 0 || i >= map.length) {
            return false;
        }
        if (j < 0 || j >= map[0].length) {
            return false;
        }
        return map[i][j] == '@';
    }
    
}
