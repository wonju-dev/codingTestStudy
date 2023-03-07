import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {

    public int[] solution(int n, int s) {
        if (n > s) {
            int[] a = {-1};
            return a;
        }

        int i = 0;
        int[] answer = new int[n];
        while (n >= 1) {
            answer[i] = s / n;
            i++;
            s -= s / n;
            n -= 1;
        }
        return answer;
    }
}