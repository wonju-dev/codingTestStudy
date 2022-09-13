package insertion;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int loop = Integer.parseInt(scanner.nextLine());

        for (int i = 0; i < loop; i++) {
            List<Integer> numberArray = getNumberArray(scanner.nextLine().split(" "));
            insertionSort(numberArray);
        }
    }

    private static void insertionSort(List<Integer> numberArray) {
        int countCompare = 0;
        int countSwap = 0;

        for (int i = 1; i < numberArray.size(); i++) {
            int temp = numberArray.get(i);
            int j = i - 1;
            while (j >= 0) {
                countCompare++;
                if (temp < numberArray.get(j)) {
                    countSwap++;
                    numberArray.set(j + 1, numberArray.get(j));
                } else {
                    break;
                }
                j--;
            }

            numberArray.set(j + 1, temp);

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
