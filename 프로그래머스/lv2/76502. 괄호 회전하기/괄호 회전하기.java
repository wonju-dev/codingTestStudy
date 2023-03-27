import java.util.Map;
import java.util.Stack;

class Solution {

    public static void main(String[] args) {
        solution("()(");
    }

    public static int solution(String s) {
        if (s.length() == 1) {
            return 0;
        }

        String ss = s + s;
        Map<Character, Character> map = Map.of(')', '(', ']', '[', '}', '{');

        int answer = 0;
        int head = 0;
        int tail = s.length() - 1;
        while (head < s.length()) {
            boolean flag = true;
            Stack<Character> stack = new Stack<>();
            for (int i = head; i <= tail; i++) {
                char c = ss.charAt(i);
                // System.out.println(c);

                if (c == ')' || c == ']' || c == '}') {
                    if (stack.isEmpty()) {
                        flag = false;
                        break;
                    }
                    char pair = map.get(c);
                    if (pair != stack.pop()) {
                        flag = false;
                        break;
                    }
                } else {
                    stack.push(c);
                }
            }
            head++;
            tail++;
            if (flag && stack.isEmpty()) {
                answer++;
            }
            System.out.println();
        }

        return answer;
    }
}
/*
0 1 2 3 4 5
{ ( [ ] ) }

()(
(
{{{{{{

 */