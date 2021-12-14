function solution(w, h) {
    // 길이가 1이면 전부 못 씀
    if (w === 1 || h === 1) return 0;
    // 정사각형이면 길이만큼 못 씀
    if (w === h) return w * (w -1);
    
    const difference = getY(0,w,h) - getY(1,w,h);
    return w*h - Math.ceil(difference) * w;
}

const getY = (x, w, h) => -1 * h / w * x + h;
