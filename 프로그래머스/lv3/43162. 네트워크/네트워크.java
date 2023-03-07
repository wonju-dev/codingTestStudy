import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    public int solution(int n, int[][] computers) {
        int count = 0;
        boolean[] visited = new boolean[n];

        for (int now = 0; now < n; now++) {
            // System.out.println("now: " + now);
            if (!visited[now]) {
                Queue<Integer> q = new ArrayDeque<>();
                q.add(now);
                while (!q.isEmpty()) {
                    Integer p = q.poll();
                    // System.out.println("p: " + p);
                    visited[p] = true;
                    for (int i = 0; i < n; i++) {
                        boolean isConnected = computers[p][i] == 1;
                        // System.out.println("isConnected: " + isConnected);
                        if (p != i && isConnected && !visited[i]) {
                            q.add(i);
                            visited[i] = true;
                        }
                    }
                }
                count++;
            }
        }

        return count;
    }
}