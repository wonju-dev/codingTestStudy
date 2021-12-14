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

/*

이전 버전
W가 홀수인지 짝수인지에 따라 사용불가능한 블록 개수가 다름
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
