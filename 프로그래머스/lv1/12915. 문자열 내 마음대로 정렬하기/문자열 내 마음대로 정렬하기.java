import java.util.Arrays;

class Solution {
    public String[] solution(String[] strings, int n) {
        return Arrays.stream(strings).sorted((s1, s2) -> {
            char c1 = s1.charAt(n);
            char c2 = s2.charAt(n);
            if (c1 - c2 <0) {
                return -1;
            } else if (c1 - c2 == 0) {
                return s1.compareTo(s2);
            }
            return 1;
        }).toArray(String[]::new);
    }
}