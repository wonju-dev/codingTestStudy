package recursion.knightstour;

import java.util.Arrays;
import java.util.Scanner;

public class main {

    static int[][] delta = {{-2, 1}, {-1, 2}, {1, 2}, {2, 1}, {2, -1}, {1, -2}, {-1, -2}, {-2, -1}};
    static int width = 0;
    static int height = 0;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int loop = Integer.parseInt(scanner.nextLine());

        while (loop > 0) {
            int[] numbers = Arrays.stream(scanner.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();

            width = numbers[0];
            height = numbers[1];
            int row = numbers[2] - 1;
            int col = numbers[3] - 1;
            int[][] table = new int[width][height];

            table[row][col] = 1;

            if (knightTour(table, row, col, 1)) {
                System.out.println(1);
                printAnswer(table);
            } else {
                System.out.println(0);
            }

            loop--;
        }
    }

    private static void printAnswer(int[][] table) {
        for (int i = 0; i < width; i++) {
            for (int j = 0; j < height; j++) {
                if (j != height - 1) {
                    System.out.print(table[i][j] + " ");
                } else{
                    System.out.print(table[i][j]);
                }
            }
            System.out.println();
        }
    }

    private static boolean knightTour(int[][] table, int row, int col, int count) {

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
                    table[nextRow][nextCol] = count + 1;

                    if (knightTour(table, nextRow, nextCol, count + 1)) {
                        return true;
                    }

                    table[nextRow][nextCol] = 0;
                }
            }
        }
        return false;
    }
}