function solution(A, B) {
    A.sort((a, b) => b - a);
    B.sort((a, b) => b - a);

    let j = 0; // B를 가리키는 인덱스
    let ans = 0; // 점수

    for (let i = 0; i < A.length; i++) { // i는 A를 가리키는 인덱스
        if (A[i] < B[j]) { // B가 더 클 때 
            ans++; // 점수 증가
            j++; // B를 가리키는 인덱스 증가
        }
    }

    return ans;
}
