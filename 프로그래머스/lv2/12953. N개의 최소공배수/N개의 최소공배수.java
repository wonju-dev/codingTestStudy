import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    public int solution(int[] arr) {
        // n * m = gcd /
        if (arr.length == 1) {
            return arr[0];
        }

        Queue<Integer> q = toQ(arr);

        while (q.size() != 1) {
            int a = q.poll();
            int b = q.poll();

            q.add(a / gcd(a, b) * b);
        }

        return q.poll();
    }

    private int gcd(int one, int two) {
        int big = one > two ? one : two;
        int small = big == one ? two : one;
        while (big % small != 0) {
            int remainder = big % small;
            big = small;
            small = remainder;
        }
        return small;
    }

    private Queue<Integer> toQ(int[] arr) {
        Queue<Integer> q = new ArrayDeque<>();
        for (int i : arr) {
            q.add(i);
        }
        return q;
    }
}