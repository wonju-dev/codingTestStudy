class Solution {
    boolean solution(String s) {
        int stack = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack++;
            } else {
                stack--;
                if (stack < 0) {
                    return false;
                }
            }
        }
        return stack == 0;
    }
}