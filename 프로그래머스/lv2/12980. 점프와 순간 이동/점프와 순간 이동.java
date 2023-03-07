public class Solution {
    public int solution(int n) {
        int count = 0;

        while (n != 0) {
            if (n % 2 == 1) {
                count++;
                n--;
            } else {
                n /= 2;
            }
        }

        return count;
    }
}