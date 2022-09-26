package recursion.math;

import java.util.Arrays;
import java.util.Scanner;

public class Expo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int loop = Integer.parseInt(scanner.nextLine());

        while (loop > 0) {
            int[] numbers = Arrays.stream(scanner.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();

            System.out.println(getExpo(numbers[0], numbers[1]));

            loop--;
        }
    }

    private static int getExpo(int a, int b) {
        if (b == 0) {
            return 1;
        } else if (b == 1) {
            return a;
        }

        int e = getExpo(a, b / 2);
        e = e * e % 1000;


        if (b % 2 == 1) {
            e = e * a % 1000;
        }

        // System.out.println("a= " + a + " " + "b= " + b + " " + "e= " + e);

        return e;
    }
}
