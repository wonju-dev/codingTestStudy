import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    static Map<String, Integer> dict = initDict();
    static int index = 0;

    public static void main(String[] args) {
        solution("KAKAO");
        solution("TOBEORNOTTOBEORTOBEORNOT");
    }

    public static int[] solution(String msg) {
        List<Integer> answer = new ArrayList<>();
        while (index < msg.length()) {
            // System.out.println("index: " + index);
            int code = getSubString(index, msg);
            answer.add(code);
            // System.out.println(dict);
            // System.out.println(answer);
        }
        return answer.stream().filter(i -> i != 0).mapToInt(Integer::valueOf).toArray();
    }

    private static Integer getSubString(int start, String msg) {
        for (int end = msg.length(); end > start; end--) {
            String subString = msg.substring(start, end);
            if (dict.get(subString) != null) {
                // System.out.println("subString: " + subString);
                if (end < msg.length() - 1) {
                    String newString = subString + msg.charAt(end);
                    dict.put(newString, dict.size() + 1);
                }
                index = end;
                return dict.get(subString);
            }
        }
        return dict.get(start);
    }

    private static Map<String, Integer> initDict() {
        Map<String, Integer> dict = new HashMap<>();
        for (int i = 65; i <= 90; i++) {
            char toChar = (char) i;
            dict.put(Character.toString(toChar), i - 64);
        }
        return dict;
    }
}