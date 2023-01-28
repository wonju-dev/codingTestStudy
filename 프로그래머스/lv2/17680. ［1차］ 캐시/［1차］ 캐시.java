import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        Deque<String> q = new ArrayDeque<>();
        int answer = 0;
        if (cacheSize == 0) {
            return cities.length * 5;
        }

        for (String city : cities) {
            city = city.toLowerCase();

            if (q.contains(city)) {
                answer++;
                q.remove(city);
                q.add(city);
            } else {
                if (q.size() < cacheSize) {
                    q.add(city);
                } else {
                    q.pollFirst();
                    q.add(city);
                }
                answer += 5;
            }
        }
        return answer;
    }
}