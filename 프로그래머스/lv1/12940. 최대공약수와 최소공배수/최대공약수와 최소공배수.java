class Solution {
    // m * n = 최대공약수(GCD) * 최소공배수(LCM)
    public int[] solution(int n, int m) {
        int gcd = getGCD(n, m);
        int lcm = n * m / gcd;
        int[] answer = {gcd, lcm};
        return answer;
    }

    private int getGCD(int n, int m) {
        int a = n >= m ? n : m;
        int b = a == n ? m : n;
        int c = a % b;

        while (c != 0) {
            a = b;
            b = c;
            c = a % b;
        }

        return b;
    }
}