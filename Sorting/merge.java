package mergesort;

import java.util.Arrays;
import java.util.Scanner;

public class main {

    static int count = 0;
    static int MAX_SIZE = 101;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int testCase = Integer.parseInt(scanner.nextLine());

        while (testCase > 0) {
            int[] raw = Arrays.stream(scanner.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();

            int size = raw[0];
            int[] numbers = Arrays.copyOfRange(raw, 1, size + 1);

            mergeSort(numbers, 0, size - 1);
            System.out.println(count);

            count = 0;
            testCase -= 1;
        }
    }

    private static void mergeSort(int[] numbers, int low, int high) {
        if (low == high) {
            return;
        }

        int mid = (low + high) / 2;

        mergeSort(numbers, low, mid);
        mergeSort(numbers, mid + 1, high);
        merge(numbers, low, mid, high);
    }

    private static void merge(int[] numbers, int low, int mid, int high) {
        int i = 0;
        int j = 0;
        int k = 0;
        int[] temp = new int[MAX_SIZE];

        for (i = low; i <= high; i++) {
            temp[i] = numbers[i];
        }

        i = k = low;
        j = mid + 1;

        while (i <= mid && j <= high) {
            count += 1;
            if (temp[i] <= temp[j]) {
                numbers[k++] = temp[i++];
            } else {
                numbers[k++] = temp[j++];
            }
        }

        while (i <= mid) {
            numbers[k++] = temp[i++];
        }

        while (j <= high) {
            numbers[k++] = temp[j++];
        }
    }
}
