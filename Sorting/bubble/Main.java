package bubble;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int loop = Integer.parseInt(scanner.nextLine());

        for (int i = 0; i < loop; i++) {
            List<Integer> numbers = getNumberArray(scanner.nextLine().split(" "));
            String answer = "";

            int[] results = bubbleSort(copyArray(numbers));
            answer += results[0] + " " + results[1] + " ";

            results = bubbleSort1(copyArray(numbers));
            answer += results[0] + " " + results[1] + " ";

            results = bubbleSort2(copyArray(numbers));
            answer += results[0] + " " + results[1];

            System.out.println(answer);
        }
    }

    private static List<Integer> getNumberArray(String[] s) {
        List<Integer> numbers = new ArrayList<>();
        for (int i = 0; i < s.length; i++) {
            if (i != 0) {
                numbers.add(Integer.parseInt(s[i]));
            }
        }
        return numbers;
    }

    private static List<Integer> copyArray(List<Integer> numbers) {
        List<Integer> copyNumbers = new ArrayList<>();
        for (int i = 0; i < numbers.size(); i++) {
            copyNumbers.add(numbers.get(i));
        }
        return copyNumbers;
    }

    private static int[] bubbleSort(List<Integer> numbers) {
        int countCompare = 0;
        int countSwap = 0;
        for (int i = 1; i < numbers.size(); i++) {
            for (int j = 0; j < numbers.size() - i; j++) {
                countCompare++;
                if (numbers.get(j) > numbers.get(j + 1)) {
                    countSwap++;
                    swap(numbers, j, j + 1);
                }
            }
        }
        int[] ans = {countCompare, countSwap};
        return ans;
    }

    private static int[] bubbleSort1(List<Integer> numbers) {
        int countCompare = 0;
        int countSwap = 0;

        for (int i = 1; i < numbers.size(); i++) {
            boolean swapped = false;

            for (int j = 0; j < numbers.size() - i; j++) {
                countCompare++;
                if (numbers.get(j) > numbers.get(j + 1)) {
                    swapped = true;
                    countSwap++;
                    swap(numbers, j, j + 1);
                }
            }

            if (!swapped) break;
        }

        int[] ans = {countCompare, countSwap};
        return ans;
    }

    private static int[] bubbleSort2(List<Integer> numbers) {
        int countCompare = 0;
        int countSwap = 0;
        int lastSwappedIndex = numbers.size();

        while (lastSwappedIndex > 0) {
            int swappedIndex = 0;
            for (int i = 1; i < lastSwappedIndex; i++) {
                countCompare++;
                if (numbers.get(i - 1) > numbers.get(i)) {
                    countSwap++;
                    swap(numbers, i - 1, i);
                    swappedIndex = i;
                }
            }
            lastSwappedIndex = swappedIndex;
        }

        int[] ans = {countCompare, countSwap};
        return ans;
    }

    private static void swap(List<Integer> numbers, int j, int i) {
        int temp = numbers.get(j);
        numbers.set(j, numbers.get(i));
        numbers.set(i, temp);
    }
}
