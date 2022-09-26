package recursion.hanoi;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class main {
    static List<Integer> first = new ArrayList<>();
    static List<Integer> second = new ArrayList<>();
    static List<Integer> third = new ArrayList<>();
    static String ans = "";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int loop = Integer.parseInt(scanner.nextLine());

        for (int i = 0; i < loop; i++) {
            int n = Integer.parseInt(scanner.nextLine());
            for (int j = n; j > 0; j--) {
                first.add(j);
            }

            hanoi(n, 1, 2, 3);
            System.out.println(ans.trim());

            first.clear();
            second.clear();
            third.clear();
            ans = "";
        }
    }

    private static void hanoi(int n, int a, int b, int c) {
        if (n > 0) {
            hanoi(n - 1, a, c, b);

            if (a == 1 && c == 2) {
                second.add(first.get(first.size() - 1));
                first.remove(first.size() - 1);
            } else if (a == 1 && c == 3) {
                third.add(first.get(first.size() - 1));
                first.remove(first.size() - 1);
                ans += third.get(third.size() - 1) + " ";
            } else if (a == 2 && c == 1) {
                first.add(second.get(second.size() - 1));
                second.remove(second.size() - 1);
            } else if (a == 2 && c == 3) {
                third.add(second.get(second.size() - 1));
                second.remove(second.size() - 1);
                ans += third.get(third.size() - 1) + " ";
            } else if (a == 3 && c == 1) {
                first.add(third.get(third.size() - 1));
                third.remove(third.size() - 1);
                if (third.isEmpty()) {
                    ans += 0 + " ";
                } else {
                    ans += third.get(third.size() - 1) + " ";
                }
            } else if (a == 3 && c == 2) {
                second.add(third.get(third.size() - 1));
                third.remove(third.size() - 1);
                if (third.isEmpty()) {
                    ans += 0 + " ";
                } else {
                    ans += third.get(third.size() - 1) + " ";
                }
            }

            hanoi(n - 1, b, a, c);
        }
    }
}
