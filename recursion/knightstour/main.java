package recursion.knightstour;

import java.util.Arrays;
import java.util.Scanner;

public class main {

    static int[][] delta = {{-2, -1}, {-2, 1}, {-1, 2}, {1, 2}, {2, 1}, {2, -1}, {1, -2}, {-1, -2}};
    static int count = 1;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int loop = Integer.parseInt(scanner.nextLine());

        while (loop > 0) {
            int[] numbers = Arrays.stream(scanner.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            int width = numbers[0];
            int height = numbers[1];
            int[][] table = new int[width][height];

            boolean canTour = knightTour(table, numbers[2] - 1, numbers[3] - 1, width, height);

            if (canTour) {
                System.out.println(1);
                printAnswer(table, width, height);
            } else {
                System.out.println(0);
            }

            count = 1;
        }
    }

    private static void printAnswer(int[][] table, int width, int height) {
        for (int i = 0; i < width; i++) {
            for (int j = 0; j < height; j++) {
                if (j != height - 1) {
                    System.out.print(table[i][j] + " ");
                } else {
                    System.out.print(table[i][j]);
                }
            }
            System.out.println();
        }
    }

    private static boolean knightTour(int[][] table, int row, int col, int width, int height) {
        table[row][col] = count;

        System.out.println(row + " " + col);

        printAnswer(table, width, height);

        if (count == width * height) {
            return true;
        }

        int nextRow = 0;
        int nextCol = 0;

        for (int i = 0; i < 8; i++) {
            nextRow = row + delta[i][0];
            nextCol = col + delta[i][1];


            if (nextRow >= 0 && nextRow < width && nextCol >= 0 && nextCol < height) {
                if (table[nextRow][nextCol] == 0) {
                    System.out.println(nextRow + " " + nextCol);
                    count++;
                    boolean b = knightTour(table, nextRow, nextCol, width, height);
                    if (!b) {
                        continue;
                    } else {
                        return true;
                    }
                }
            }
        }

        table[nextRow][nextCol] = 0;
        return false;
    }
}