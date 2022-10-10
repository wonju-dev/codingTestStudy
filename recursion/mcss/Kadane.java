package mcss;

import java.util.Arrays;
import java.util.Scanner;

public class Kadane {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int testCase = Integer.parseInt(scanner.nextLine());

        while (testCase > 0) {

            int[] raw = Arrays.stream(scanner.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            int size = raw[0];

            int[] numbers = Arrays.copyOfRange(raw, 1, size + 1);
            int[][] dp = new int[size][3];
            dp[0][0] = numbers[0];

            for (int i = 1; i < size; i++) {
                int previous = dp[i - 1][0] + numbers[i];
                int onlyNow = numbers[i];

                int bigger = getBigger(previous, onlyNow);

                dp[i][0] = bigger;
                if (previous == onlyNow) {
                    dp[i][1] = i;
                } else {
                    dp[i][1] = bigger == previous ? dp[i - 1][1] : i;
                }
                dp[i][2] = i;
            }

            int[] max = getMax(dp);

            System.out.println(max[0] + " " + max[1] + " " + max[2]);

            testCase--;
        }
    }

    private static int[] getMax(int[][] dp) {
        int[] max = new int[3];
        max[1] = -1;
        max[2] = -1;

        for (int[] number : dp) {
            if (number[0] > max[0]) {
                max = number;
            }
        }

        return max;
    }

    private static int getBigger(int one, int two) {
        return one > two ? one : two;
    }
}
