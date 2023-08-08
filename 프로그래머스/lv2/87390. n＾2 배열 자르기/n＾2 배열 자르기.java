import java.util.*;

class Solution {
    public int[] solution(int n, long left, long right) {
        List<Integer> answer = new ArrayList<>();

        for (long i = left; i <= right; i++) {
            int row = (int) (i / (long) n);
            int col = (int) (i % (long) n);
            if (row < col) {
                answer.add(col+1);
            } else {
                answer.add(row+1);
            }
        }

        return answer.stream().mapToInt(Integer::valueOf).toArray();
    }
}