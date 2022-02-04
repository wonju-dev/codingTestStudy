class Solution {
    public int solution(long num) {
        int answer = 0;
        while (num != 1) {
            num = num % 2 == 0 ? num / 2 : num * 3 + 1;
            answer ++;
        }
        return answer <= 500 ? answer : -1;
    }
}
