package y2025;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import y2025.java.*;

public class Main {
    public static void main(String[] args) {
        File input = new File("y2025/input");
        List<String> inputLines = new ArrayList<>();

        Runnable solution = new d2();

        try (Scanner myReader = new Scanner(input)) {
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                inputLines.add(data);
            }
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

        solution.run(inputLines);
    }
}
