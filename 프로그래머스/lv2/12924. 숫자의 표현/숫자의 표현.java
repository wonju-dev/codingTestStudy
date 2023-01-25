class Solution {
    public int solution(int n) {
        int answer = 0;

        int k = 1;
        while (k + sum(k) <= n) {
            if ((n - sum(k)) % k == 0) {
                answer++;
            }
            k++;
        }

        return answer;
    }

    private int sum(int k) {
        int sum = 0;
        for (int i = k - 1; i > 0; i--) {
            sum += i;
        }
        return sum;
    }
}