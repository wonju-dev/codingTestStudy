package comb;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class main {

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

        int gap = numbers.size();
        boolean sorted = false;

        while (!sorted) {
            gap = (int) Math.floor(gap / SHRINK_FACTOR);

            if (gap <= 1) {
                gap = 1;
                sorted = true;
            }

            int index = 0;
            while (index + gap < numbers.size()) {
                countCompare++;
                if (numbers.get(index) > numbers.get(index + gap)) {
                    countSwap++;
                    swap(numbers, index, index + gap);
                    sorted = false;
                }
                index++;
            }
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
