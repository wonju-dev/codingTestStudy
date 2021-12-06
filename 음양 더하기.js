function solution(absolutes, signs) {
    let answer = 0 ;
    absolutes.forEach((number, index) => {
        if (signs[index]) answer += number;
        else answer += -1 * number;
    })
    return answer;
}
