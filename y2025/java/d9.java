package y2025.java;

import java.util.ArrayList;
import java.util.List;

import y2025.Runnable;

public class d9 implements Runnable {
    private List<Point> points = new ArrayList<>();
    private Point[][] collapsedMap;
    private List<Integer> Xcoords;
    private List<Integer> Ycoords;
    private long solution1 = 0;
    private long solution2 = 0;

    private List<int[]> pending = new ArrayList<>(List.of(new int[] {100, 100}));

    @Override
    public void run(List<String> input) {
        for (String line : input) {
            String[] parts = line.split(",");
            int x = Integer.valueOf(parts[0]);
            int y = Integer.valueOf(parts[1]);

            points.add(new Point(x, y));
        }

        Xcoords = points.stream().map(Point::getX).distinct().sorted().toList();
        Ycoords = points.stream().map(Point::getY).distinct().sorted().toList();

        int Xdim = (int) points.stream().map(Point::getX).distinct().count();
        int Ydim = (int) points.stream().map(Point::getY).distinct().count();

        collapsedMap = new Point[Xdim][Ydim];
        int[] first = null;
        int[] previous = null;
        for (Point point : points) {
            if (first == null) first = new int[] {point.x, point.y};
            int Y = Ycoords.indexOf(point.y);
            int X = Xcoords.indexOf(point.x);

            collapsedMap[Y][X] = point;

            if (previous != null) {
                for (int i = Math.min(X, previous[0]); i <= Math.max(X, previous[0]); i++) {
                    for (int j = Math.min(Y, previous[1]); j <= Math.max(Y, previous[1]); j++) {
                        collapsedMap[j][i] = collapsedMap[j][i] == null ? Point.NULL : collapsedMap[j][i];
                    }
                }
            }
            previous = new int[] {X, Y};
        }


        for (int i = Math.min(Xcoords.indexOf(first[0]), previous[0]); i <= Math.max(Xcoords.indexOf(first[0]), previous[0]); i++) {
            for (int j = Math.min(Ycoords.indexOf(first[1]), previous[1]); j <= Math.max(Ycoords.indexOf(first[1]), previous[1]); j++) {
                collapsedMap[j][i] = collapsedMap[j][i] == null ? Point.NULL: collapsedMap[j][i];
            }
        }

        while (!pending.isEmpty()) {
            int[] point = pending.removeFirst();

            int i = point[0];
            int j = point[1];
            
            if (collapsedMap[i][j] != null) continue;
            collapsedMap[i][j] = Point.NULL;

            if (collapsedMap[i+1][j] == null) {
                pending.add(new int[] {i+1, j});
            }
            if (collapsedMap[i-1][j] == null) {
                pending.add(new int[] {i-1, j});
            }
            if (collapsedMap[i][j+1] == null) {
                pending.add(new int[] {i, j+1});
            }
            if (collapsedMap[i][j-1] == null) {
                pending.add(new int[] {i, j-1});
            }
        }

        for (Point point1 : points) {
            for (Point point2 : points) {
                if (point1 == point2) break;

                long area =  ((long) Math.abs(point1.x - point2.x) + 1) * ((long) Math.abs(point1.y - point2.y) + 1);
                if (area > solution1) {
                    solution1 = area;
                }
                if (checkArea(point1, point2) && solution2 < area) {
                    solution2 = area;
                }
            }
        }

        System.out.println("Part 1: %d".formatted(solution1));
        System.out.println("Part 2: %d".formatted(solution2));
    }

    private boolean checkArea(Point point1, Point point2) {
        for (int i = Math.min(Xcoords.indexOf(point1.x), Xcoords.indexOf(point2.x)); i <= Math.max(Xcoords.indexOf(point1.x), Xcoords.indexOf(point2.x)); i++) {
            for (int j = Math.min(Ycoords.indexOf(point1.y), Ycoords.indexOf(point2.y)); j <= Math.max(Ycoords.indexOf(point1.y), Ycoords.indexOf(point2.y)); j++) {
                if (collapsedMap[j][i] == null) {
                    return false;
                }
            }
        }

        return true;
    }

    static class Point {
        public static final Point NULL = new Point(0,0);
        final int x;
        final int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }
    }
    
}
