import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int[] solution(String s) {
        Map<Character, Integer> indexMap = new HashMap<>();
        List<Integer> answer = new ArrayList<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (indexMap.containsKey(c)) {
                answer.add(i - indexMap.get(c));
            } else {
                answer.add(-1);
            }
            indexMap.put(c, i);
        }

        return answer.stream().mapToInt(Integer::valueOf).toArray();
    }
}