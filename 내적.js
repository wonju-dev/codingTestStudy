function solution(a, b) {
    let answer = 0;
    a.forEach((number,index)=> answer += number * b[index])
    return answer;
}
