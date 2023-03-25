class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        answer += n * 12_000;
        int surplus = k - n / 10;
        if (surplus > 0) {
            answer += surplus * 2_000;
        }
        return answer;
    }
}