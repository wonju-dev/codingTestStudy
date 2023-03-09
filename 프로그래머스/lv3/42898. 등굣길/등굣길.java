class Solution {
    static int DIVISION = 1_000_000_007;

    public int solution(int m, int n, int[][] puddles) {
        int[][] dp = new int[n][m];
        dp[0][0] = 1;
        for (int[] puddle : puddles) {
            int col = puddle[0] - 1;
            int row = puddle[1] - 1;
            dp[row][col] = -1;
        }
        
        for (int row = 0; row < n; row++) {
            for (int col = 0; col < m; col++) {
                // System.out.println(row + " " + col);
                if (dp[row][col] != -1) {
                    if (row == 0 && col == 0) {
                        continue;
                    } else if (row == 0) {
                        dp[row][col] = (dp[row][col - 1] != -1 ? dp[row][col - 1] : 0) % DIVISION;
                    } else if (col == 0) {
                        dp[row][col] = (dp[row - 1][col] != -1 ? dp[row - 1][col] : 0) % DIVISION;
                    } else {
                        int left = dp[row][col - 1] != -1 ? dp[row][col - 1] : 0;
                        int top = dp[row - 1][col] != -1 ? dp[row - 1][col] : 0;
                        dp[row][col] = (left + top) % DIVISION;
                    }
                }
                // System.out.println(dp[row][col]);
                // System.out.println();
            }
        }
        return dp[n - 1][m - 1];
    }
}