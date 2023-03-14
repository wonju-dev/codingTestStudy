import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

class Solution {
    public long solution(int n, int[] works) {
        if (n >= Arrays.stream(works).reduce(0, (i1, i2) -> i1 + i2)) {
            return 0;
        }
        
        PriorityQueue<Integer> q = queuefy(works);
        for (int i = 0 ; i < n; i++) {
            Integer poll = q.poll();
            q.add(poll - 1);
        }
        long answer = 0;
        while (!q.isEmpty()) {
            Integer i = q.poll();
            answer += i * i;
        }
        return answer;
    }

    private PriorityQueue<Integer> queuefy(int[] works) {
        PriorityQueue<Integer> q = new PriorityQueue<>(Comparator.reverseOrder());
        for (int work : works) {
            q.add(work);
        }
        return q;
    }
}