class Solution {
    public int solution(int n) {
        int remainder = n % 7;
        if (remainder > 0) {
            return n / 7 + 1;
        } else {
            return n / 7;
        }
    }
}