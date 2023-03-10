class Solution {
    public int solution(int n, int[] stations, int w) {
        int previousStation = -w;
        int sFrom = 0;
        int sTo = 0;
        int nFrom = 0;
        int nTo = 0;
        int answer = 0;
        for (int station : stations) {
            sFrom = station - w <= 0 ? 1 : station - w;
            sTo = station + w > n ? n : station + w;
            nFrom = previousStation + w + 1;
            nTo = sFrom - 1;
            previousStation = station;
            if (nFrom <= nTo) {
                int divi = (1 + w * 2);
                int diff = nTo - nFrom + 1;
                answer += diff / divi;
                if (diff % divi != 0) {
                    answer++;
                }
            }
        }
        if (sTo != n) {
            int divi = (1 + w * 2);
            int diff = n - (sTo + 1) + 1;
            answer += diff / divi;
            if (diff % divi != 0) {
                answer++;
            }
        }
        return answer;
    }
}
