import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};

    public int solution(int[][] maps) {
        Queue<Cord> q = new ArrayDeque<>();
        q.add(new Cord(0, 0, 1));
        int n = maps.length;
        int m = maps[0].length;

        while (!q.isEmpty()) {
            Cord c = q.poll();
            if (c.x == n - 1 && c.y == m - 1) {
                return c.d;
            }
            if (maps[c.x][c.y] == 0) {
                continue;
            }
            maps[c.x][c.y] = 0;

            for (int i = 0; i < 4; i++) {
                int nx = c.x + dx[i];
                int ny = c.y + dy[i];

                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    q.add(new Cord(nx, ny, c.d + 1));
                }
            }
        }
        return -1;
    }

    private class Cord {
        int x;
        int y;
        int d;

        public Cord(int x, int y, int d) {
            this.x = x;
            this.y = y;
            this.d = d;
        }
    }
}