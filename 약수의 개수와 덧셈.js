function solution(left, right) {
    let answer = 0;
    for (let i = left; i <= right; i++){
        let numberOfDivisor = 1;
        for (let j = 1; j < Math.floor(i / 2)+1; j++) {
            if (i % j ===0) numberOfDivisor +=1;
        }
        if (numberOfDivisor % 2 ===0) answer += i;
        else answer -= i;
    }
    return answer;
}
