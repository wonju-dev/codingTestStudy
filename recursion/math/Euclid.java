package recursion.math;

import java.util.Scanner;

public class Euclid {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int loop = Integer.parseInt(scanner.nextLine());

        while (loop > 0) {
            String[] s = scanner.nextLine().split(" ");
            System.out.println(getGCD(Integer.parseInt(s[0]), Integer.parseInt(s[1])));
            loop--;
        }
    }

    private static int getGCD(int a, int b) {
        if (b == 0) {
            return a;
        } else {
            return getGCD(b, a % b);
        }
    }
}
