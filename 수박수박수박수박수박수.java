class Solution {
    public String solution(int n) {
        String answer = "";
        String[] charArray = {"수","박"};
        for (int i = 1 ; i <= n ; i++) {
            if (i%2 == 0) answer += charArray[1];
            else answer += charArray[0];
        }
        return answer;
    }
}
