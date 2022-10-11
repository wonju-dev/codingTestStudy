package mcss;

import java.util.Arrays;
import java.util.Scanner;

public class DevideAndCon {

    static int MIN = -1001;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int testCase = Integer.parseInt(scanner.nextLine());

        while (testCase > 0) {
            int[] raw = Arrays.stream(scanner.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            int size = raw[0];
            int[] numbers = Arrays.copyOfRange(raw, 1, size + 1);

            int max = findMax(numbers, 0, size - 1);

            System.out.println(max > 0 ? max : 0);

            testCase--;
        }
    }

    private static int findMax(int[] numbers, int head, int tail) {

        if (head == tail) {
            return numbers[head];
        }

        int mid = (head + tail) / 2;
        int left = MIN;
        int right = MIN;
        int sum = 0;

        for (int i = mid; i >= head; i--) {
            sum += numbers[i];
            left = left > sum ? left : sum;
        }

        sum = 0;
        for (int i = mid + 1; i <= tail; i++) {
            sum += numbers[i];
            right = right > sum ? right : sum;
        }

        int front = findMax(numbers, head, mid);
        int back = findMax(numbers, mid + 1, tail);

        int single = front > back ? front : back;

        return left + right > single ? left + right : single;
    }
}
