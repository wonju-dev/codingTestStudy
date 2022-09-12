package comb;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Main {

    public static Double SHRINK_FACTOR = 1.3;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int loop = Integer.parseInt(scanner.nextLine());

        for (int i = 0; i < loop; i++) {
            List<Integer> numbers = getNumberArray(scanner.nextLine().split(" "));
            combSort(numbers);

        }
    }

    private static void combSort(List<Integer> numbers) {
        int countCompare = 0;
        int countSwap = 0;

        int gap = (int) Math.floor(numbers.size() / SHRINK_FACTOR);

        while (gap != 0) {
            for (int i = 0; i < numbers.size() - gap; i++) {
                countCompare++;
                if (numbers.get(i) > numbers.get(i + gap)) {
                    countSwap++;
                    swap(numbers, i, i + gap);
                }
            }
            gap = (int) Math.floor(gap / SHRINK_FACTOR);
        }

        System.out.println(countCompare + " " + countSwap);
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

    private static void swap(List<Integer> numbers, int j, int i) {
        int temp = numbers.get(j);
        numbers.set(j, numbers.get(i));
        numbers.set(i, temp);
    }
}
