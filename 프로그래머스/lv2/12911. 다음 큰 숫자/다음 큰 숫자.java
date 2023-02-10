class Solution {
    public int solution(int n) {
        int numOfOne = Integer.bitCount(n);

        while (true) {
            if (numOfOne == Integer.bitCount(++n)) {
                return n;
            }
        }
    }
}