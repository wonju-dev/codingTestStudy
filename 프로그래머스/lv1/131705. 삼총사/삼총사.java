class Solution {
    public int solution(int[] number) {
        int answer = 0;
        for (int f = 0; f < number.length - 2; f++) {
            for (int s = f + 1; s < number.length - 1; s++) {
                for (int t = s + 1; t < number.length; t++) {
                    if (number[f] + number[s] + number[t] == 0) {
                        answer++;
                    }
                }
            }
        }
        return answer;
    }
}