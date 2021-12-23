function solution(d, budget) {
    let answer = 0;
    d.sort();
    for (let i = 0 ; i < d.length ; i++) {
        if (budget - d[i] >= 0) {
            answer +=1
            budget -= d[i];
        } else break;
    }
    return answer;
}
