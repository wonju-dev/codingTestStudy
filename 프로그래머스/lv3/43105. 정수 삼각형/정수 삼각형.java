class Solution {
    public int solution(int[][] triangle) {
        int[][] dp = new int[triangle.length][triangle.length];
        if (triangle.length == 1) {
            return triangle[0][0];
        } else {
            dp[0][0] = triangle[0][0];
            for (int row = 1; row < triangle.length; row++) {
                for (int col = 0; col < triangle[row].length; col++) {
                    if (col == 0) {
                        dp[row][col] = triangle[row][col] + dp[row - 1][col];
                    } else if (col == triangle[row].length - 1) {
                        dp[row][col] = triangle[row][col] + dp[row - 1][col - 1];
                    } else {
                        dp[row][col] = triangle[row][col] + Math.max(dp[row - 1][col - 1], dp[row - 1][col]);
                    }
                }
            }
            return getMax(dp[triangle.length - 1]);
        }
    }

    private int getMax(int[] ints) {
        int max = 0;
        for (int i = 0; i < ints.length; i++) {
            if (max < ints[i]) {
                max = ints[i];
            }
        }
        return max;
    }
}