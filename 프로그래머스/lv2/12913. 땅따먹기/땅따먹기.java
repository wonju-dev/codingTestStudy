import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

class Solution {

    int solution(int[][] land) {
        int[][] dp = new int[land.length][land[0].length];
        dp[0][0] = land[0][0];
        dp[0][1] = land[0][1];
        dp[0][2] = land[0][2];
        dp[0][3] = land[0][3];

        if (land.length == 1) {
            return findMax(land[0]);
        }

        for (int row = 1; row < land.length; row++) {
            for (int col = 0; col < 4; col++) {
                dp[row][col] = land[row][col] + Collections.max(getCandidates(dp, row, col));
            }
        }
        return findMax(dp[land.length - 1]);
    }

    private List<Integer> getCandidates(int[][] land, int row, int col) {
        List<Integer> candidates = new ArrayList<>();
        for (int i = 0; i < 4; i++) {
            if (i != col) {
                candidates.add(land[row - 1][i]);
            }
        }
        return candidates;
    }

    private int findMax(int[] ints) {
        int max = -1;
        for (int i = 0; i < ints.length; i++) {
            if (ints[i] > max) {
                max = ints[i];
            }
        }
        return max;
    }
}