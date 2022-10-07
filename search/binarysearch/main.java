package binary;

import java.util.Arrays;
import java.util.Scanner;

public class main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int loop = Integer.parseInt(scanner.nextLine());

        while (loop > 0) {
            int[] meta = Arrays.stream(scanner.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            int[] numbers = Arrays.stream(scanner.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();

            System.out.println(binarySearch(meta[1], 0, meta[0] - 1, numbers));

            loop -= 1;
        }
    }

    private static int binarySearch(int target, int head, int tail, int[] numbers) {
        int mid = (head + tail) / 2;

        if (head > tail) {
            return -1;
        }


        if (numbers[mid] == target) {
            return mid;
        } else if (numbers[mid] < target) {
            return binarySearch(target, mid + 1, tail, numbers);
        } else {
            return binarySearch(target, head, mid - 1, numbers);
        }
    }
}
