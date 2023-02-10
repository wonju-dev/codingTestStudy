class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = {0, 0};
        for (int col = 1; col <= yellow; col++) {
            int row = yellow / col;
            if (col * row == yellow) {
                if (col * 2 + row * 2 + 4 == brown) {
                    answer[0] = row + 2;
                    answer[1] = col + 2;
                    return answer;
                }
            }
        }
        return answer;
    }
}