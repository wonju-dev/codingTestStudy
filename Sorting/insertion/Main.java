package insertion;

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int loop = Integer.parseInt(scanner.nextLine());
        for (int i = 0; i < loop; i++) {
            String s = scanner.nextLine();
            int numOfNumbers = Integer.parseInt(s.substring(0, 1));
            int[] numberArray = getNumberArray(numOfNumbers, s.substring((2)));
            insertionSort(numOfNumbers, numberArray);
        }
    }

    private static int[] getNumberArray(int size, String substring) {
        int[] numbers = new int[size];
        int index = 0;

        for (int i = 0; i < substring.length(); i++) {
            if (substring.charAt(i) != ' ') {
                numbers[index] = Character.getNumericValue(substring.charAt(i));
                index++;
            }
        }

        return numbers;
    }

    private static void insertionSort(int size, int[] numbers) {
        int countCompare = 0;
        int countSwap = 0;
        for (int i = 1; i < size; i++) {
            int index = i - 1;
            while (index >= 0) {
                countCompare++;
                if (numbers[index + 1] < numbers[index]) {
                    countSwap++;
                    swap(numbers, index);
                    index--;
                } else {
                    break;
                }
            }
        }
        System.out.println(countCompare + " " + countSwap);
    }

    private static void swap(int[] numbers, int index) {
        int temp = numbers[index + 1];
        numbers[index + 1] = numbers[index];
        numbers[index] = temp;
    }
}
