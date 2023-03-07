import java.util.Comparator;
import java.util.PriorityQueue;

class Solution {

    public static PriorityQueue<Integer> q = new PriorityQueue();
    public static PriorityQueue<Integer> rq = new PriorityQueue<>(Comparator.reverseOrder());

    public int[] solution(String[] operations) {
        for (String operation : operations) {
            String[] s = operation.split(" ");
            String op = s[0];
            Integer value = Integer.parseInt(s[1]);

            if (op.equals("I")) {
                insert(value);
            } else {
                if (rq.size() == 0) {
                    continue;
                }
                if (value == -1) {
                    deleteMin();
                } else {
                    deleteMax();
                }
            }
        }
        int[] answer = new int[2];
        System.out.println(q);
        System.out.println(rq);
        if (rq.size() != 0) {
            answer[0] = rq.poll();
            answer[1] = q.poll();
        }
        return answer;
    }

    private void deleteMax() {
        Integer poll = rq.poll();
        q.remove(poll);
    }

    private void deleteMin() {
        Integer poll = q.poll();
        rq.remove(poll);
    }

    private void insert(Integer value) {
        q.add(value);
        rq.add(value);
    }
}