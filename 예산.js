function solution(d, budget) {
    let answer = 0;
    d.sort((a,b)=> a-b);
    for (let i = 0 ; i < d.length ; i++) {
        if (budget - d[i] >= 0) {
            answer +=1
            budget -= d[i];
        } else break;
    }
    return answer;
}
/*
JS의 array.sort()는 유니코드 기반으로 정렬된다
즉, [1,2,11].sort => [1,11,2]

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
*/
