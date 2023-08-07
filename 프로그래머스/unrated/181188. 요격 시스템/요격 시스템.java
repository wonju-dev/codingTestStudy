import java.util.*;

class Solution {
        public int solution(int[][] targets) {
        int count = 0;

        Arrays.sort(targets, (i1, i2) -> i1[0] - i2[0]);

        int preStart = targets[0][0];
        int preEnd = targets[0][1];

        for (int[] target : targets) {
            if (count == 0) {
                count++;
                continue;
            }

            int curStart = target[0];
            int curEnd = target[1];

            if (preStart <= curStart && curStart < preEnd) {
                preStart = Math.max(preStart, curStart);
                preEnd = Math.min(preEnd, curEnd);
            } else {
                preStart = curStart;
                preEnd = curEnd;
                count++;
            }
        }

        return count;
    }
}