package sort.shell;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class main {

    private static int SHRINK_FACTOR = 2;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int loop = Integer.parseInt(scanner.nextLine());

        for (int i = 0; i < loop; i++) {
            List<Integer> numberArray = getNumberArray(scanner.nextLine().split(" "));
            shellSort(numberArray);
        }
    }

    private static void shellSort(List<Integer> numberArray) {
        int countCompare = 0;
        int countSwap = 0;

        int gap = numberArray.size() / SHRINK_FACTOR;

        while (gap > 0) {
            for (int i = 0; i + gap < numberArray.size(); i++) {
                List<Integer> indexes = getSubListIndexes(numberArray, i, gap);
                for (int j = 1; j < indexes.size(); j++) {
                    int target = numberArray.get(indexes.get(j));
                    int k = j - 1;
                    for (; k >= 0; k--) {
                        if (target < numberArray.get((indexes.get(k)))) {
                            countSwap++;
                            numberArray.set(indexes.get(k + 1), numberArray.get(indexes.get(k)));
                        } else {
                            break;
                        }
                    }
                    numberArray.set(indexes.get(k + 1), target);
                }

            }
            gap /= SHRINK_FACTOR;
        }
        System.out.println(countCompare + " " + countSwap);
    }

    private static List<Integer> getSubListIndexes(List<Integer> numberArray, int index, int gap) {
        List<Integer> list = new ArrayList<>();
        while (index < numberArray.size()) {
            list.add(index);
            index += gap;
        }

        return list;
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
