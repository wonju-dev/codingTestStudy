package recursion.factorial;

import java.util.Scanner;

class main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int loop = scanner.nextInt();

        for (int i = 0; i < loop; i++) {
            System.out.println(factorial(scanner.nextInt()));
        }

    }

    private static int factorial(int n) {
        if (n == 0) {
            return 1;
        }

        String s = n * factorial(n - 1) + "";
        int index = s.length() - 1;

        while (index >= 0 && s.charAt(index) == '0') {
            index--;
        }

        return Integer.parseInt(s.substring(0, index + 1)) % 1000;
    }
}
