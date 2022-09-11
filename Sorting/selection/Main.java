package selection;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int loop = Integer.parseInt(scanner.nextLine());

        for (int i = 0 ; i < loop ; i++) {
            selectionSort(scanner);
        }
    }

    private static void selectionSort(Scanner scanner) {
        List<Integer> integers = new ArrayList<>();

        String[] s = scanner.nextLine().split(" ");
        for (int i = 0; i < s.length; i++) {
            if (i != 0) {
                integers.add(Integer.parseInt(s[i]));
            }
        }

        int countCompare = 0;
        int countSwap = 0;

        for (int i = 0; i < integers.size() - 1; i++) {

            int minIndex = i + 1;
            for (int j = i + 1; j < integers.size(); j++) {
                countCompare++;
                if (integers.get(j) < integers.get(minIndex)) {
                    minIndex = j;
                }
            }

            if (integers.get(i) > integers.get(minIndex)) {
                countSwap++;
                int temp = integers.get(i);
                integers.set(i, integers.get(minIndex));
                integers.set(minIndex, temp);
            }
        }

        System.out.println(countCompare + " " + countSwap);
    }
}
