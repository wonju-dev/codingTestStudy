import java.util.Arrays;

class Solution {
    public int solution(int[] A, int[] B) {
        Arrays.sort(A);
        Arrays.sort(B);

        int ia = 0;
        int ib = 0;
        int answer = 0;


        while (ia < A.length && ib < B.length) {
            if (A[ia] < B[ib]) {
                ia++;
                answer++;
            }
            ib++;
        }

        return answer;
    }
}