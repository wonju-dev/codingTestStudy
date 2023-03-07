import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    public int solution(int n, int[][] computers) {
        int count = 0;
        boolean[] visited = new boolean[n];

        for (int startIndex = 0; startIndex < n; startIndex++) {
            if (!visited[startIndex]) {
                Queue<Integer> q = new ArrayDeque<>();
                q.add(startIndex);
                while (!q.isEmpty()) {
                    Integer cur = q.poll();
                    visited[cur] = true;
                    for (int i = 0; i < n; i++) {
                        boolean isConnected = computers[cur][i] == 1;
                        if (cur != i && isConnected && !visited[i]) {
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