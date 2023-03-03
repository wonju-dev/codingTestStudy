import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    public int solution(int n, int m, int[] section) {
        int count = 0;
        int lastPaintedIndex = 0;
        for (int sec : section) {
            if (sec > lastPaintedIndex) {
                count++;
                lastPaintedIndex = sec + m - 1;
            }
        }
        return count;
    }
}