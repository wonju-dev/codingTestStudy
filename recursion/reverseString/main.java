package recursion.reverseString;

import java.util.Scanner;

class main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int loop = Integer.parseInt(scanner.nextLine());

        for (int i = 0; i < loop; i++) {
            String s = scanner.nextLine();
            System.out.println(reverse(s, 0, s.length() - 1));
        }

    }

    private static String reverse(String s, int head, int tail) {
        if (head < tail) {
            return reverse(swap(s, head, tail), head + 1, tail - 1);
        } else {
            return s;
        }
    }

    private static String swap(String s, int head, int tail) {
        char[] chars = s.toCharArray();

        char temp = chars[head];
        chars[head] = chars[tail];
        chars[tail] = temp;

        String ss = "";
        for (char aChar : chars) {
            ss += aChar;
        }

        return ss;
    }
}
