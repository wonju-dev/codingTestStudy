import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

class Solution {
    public int solution(int[] p, int limit) {
        List<Integer> people = Arrays.stream(p).sorted().boxed().collect(Collectors.toList());
        int count = 0;
        int h = 0;
        int t = people.size() - 1;
        while (h <= t) {
            int head = people.get(h);
            int tail = people.get(t);
            if (head + tail <= limit) {
                h++;
            }
            t--;
            count++;
        }
        return count;
    }
}