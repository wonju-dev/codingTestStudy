import java.util.*;

class Solution {

    public int solution(int n, int a, int b) {
        List<Integer> players = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            players.add(i);
        }
        Queue<MatchInfo> q = getMatchQueue(players, 0);
        Stack<Integer> s = new Stack<>();

        while (!q.isEmpty()) {
            // System.out.println(q);
            MatchInfo poll = q.poll();
            int x = poll.x;
            int y = poll.y;

            if ((x == a || x == b) && (y == a || y == b)) {
                return poll.round;
            }

            if (x == a || x == b) {
                s.add(x);
            } else if (y == a || y == b) {
                s.add(y);
            } else {
                s.add(x);
            }
            if (s.size() == 2) {
                q.addAll(getMatchQueue(s, poll.round));
                s.clear();
            }
        }
        return (int) Math.sqrt(n);
    }

    private Queue<MatchInfo> getMatchQueue(List<Integer> players, int round) {
        Queue<MatchInfo> q = new ArrayDeque<>();
        for (int i = 0; i < players.size(); i += 2) {
            q.add(new MatchInfo(players.get(i), players.get(i + 1), round + 1));
        }
        return q;
    }

    private class MatchInfo {
        int x;
        int y;
        int round;

        public MatchInfo(int x, int y, int round) {
            this.x = x;
            this.y = y;
            this.round = round;
        }

        @Override
        public String toString() {
            return "{" +
                    "x=" + x +
                    ", y=" + y +
                    ", round=" + round +
                    '}';
        }
    }
}
