import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

class Solution {
    public int solution(int k, int[] tangerine) {
        Map<Integer, Integer> sizeCounter = new HashMap<>();

        for (int i : tangerine) {
            if (sizeCounter.get(i) == null) {
                sizeCounter.put(i, 1);
            } else {
                sizeCounter.put(i, sizeCounter.get(i) + 1);
            }
        }

        List<Map.Entry<Integer, Integer>> entries = sizeCounter.entrySet().stream().sorted((e1, e2) -> -e1.getValue().compareTo(e2.getValue())).collect(Collectors.toList());

        int count = 0;
        int answer = 0;
        for (Map.Entry<Integer, Integer> entry : entries) {
            if (count < k) {
                count += entry.getValue();
                answer++;
            } else {
                return answer;
            }
        }
        return answer;
    }
}