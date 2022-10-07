package recursion.stringpermutation;

import java.util.Scanner;

class main {

    static int count = 0;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int loop = Integer.parseInt(scanner.nextLine());

        for (int i = 0; i < loop; i++) {
            char[] string = scanner.nextLine().toCharArray();
            getPermutations(string, 0, string.length);
            System.out.println(count);
            count = 0;
        }
    }

    private static void getPermutations(char[] string, int head, int tail) {
        int range = tail - head;

        if (range == 1) {
            int sum = 0;
            for (int i = 0 ; i < string.length; i++) {
                if (i % 2 == 0) {
                    sum += getW(string[i]);
                } else {
                    sum -= getW(string[i]);
                }
            }

            if (sum > 0) {
                count++;
            }
        } else {
            for (int i = 0; i < range; i++) {
                swap(string, head, head + i);
                getPermutations(string, head + 1, tail);
                swap(string, head, head + i); /* recover */
            }
        }

    }

    private static void swap(char[] string, int head, int next) {
        char temp = string[head];
        string[head] = string[next];
        string[next] = temp;
    }

    private static int getW(char target) {
        return (int) target - (int) 'a';
    }
}
