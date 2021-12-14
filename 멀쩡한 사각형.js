function solution(w, h) {
    const getY = (x) => -1 * h * x / w + h;    
    
    if (w === 1 || h === 1) return 0;
    else if (w === h) return w * h - w;
    
    let totalBlock = w * h;
    for (let i = 0 ; i < w ; i++) totalBlock -= (Math.ceil(getY(i)) - Math.floor(getY(i+1)));
    
    return totalBlock;
}

/*

이전 버전
문제 : 자바스크립트의 계산 한계(?)를 고려하지 않음 (소숫점 계산)

function solution(w, h) {
    if (w === 1 || h === 1) return 0;
    else if (w === h) return w * h - w;
    
    const traces = [];
    for (let i = 0 ; i <= w ; i++) traces.push(getY(i, w, h))
    
    let totalBlock = w * h;
    for (let i = 0 ; i < w ; i++) totalBlock -= (Math.ceil(traces[i]) - Math.floor(traces[i+1]));
    
    return totalBlock;
}

const getY = (x, w, h) => -1 * h / w * x + h;
*/

/*

이전 버전
문제 : W가 홀수인지 짝수인지에 따라 사용불가능한 블록 개수가 다름 (잘못된 로직)

function solution(w, h) {
    // 길이가 1이면 전부 못 씀
    if (w === 1 || h === 1) return 0;
    // 정사각형이면 길이만큼 못 씀
    if (w === h) return w * (w -1);
    
    const difference = getY(0,w,h) - getY(1,w,h);
    return w*h - Math.ceil(difference) * w;
}

const getY = (x, w, h) => -1 * h / w * x + h;
*/
