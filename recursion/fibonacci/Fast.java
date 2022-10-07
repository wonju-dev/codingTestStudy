package recursion.fibonacci;

import java.util.Scanner;

public class Fast {
    public static int[][] f = {{1, 1}, {1, 0}};

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int loop = Integer.parseInt(scanner.nextLine());

        while (loop > 0) {
            int number = Integer.parseInt(scanner.nextLine());
            if (number == 0) {
                System.out.println(0);
            } else if (number == 1) {
                System.out.println(1);
            } else {
                int[][] fibonacci = getFibonacci(number - 1);
                System.out.println(fibonacci[0][0]);
            }
            loop--;
        }
    }

    private static int[][] getFibonacci(int number) {
        if (number == 1 || number == 0) {
            return f;
        }

        int[][] fibonacci = getFibonacci(number / 2);

        fibonacci = product(fibonacci, fibonacci);

        if (number % 2 == 1) {
            fibonacci = product(fibonacci, f);
        }

        return fibonacci;
    }

    private static int[][] product(int[][] a, int[][] b) {
        int returnArray[][] = {{0, 0}, {0, 0}};

        returnArray[0][0] = (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % 1000;
        returnArray[0][1] = (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % 1000;
        returnArray[1][0] = (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % 1000;
        returnArray[1][1] = (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % 1000;

        return returnArray;
    }

}
