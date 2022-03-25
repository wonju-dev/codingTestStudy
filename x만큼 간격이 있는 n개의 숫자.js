function solution(x, n) {
    return (new Array(n)).fill(1).map((num,idx)=> num * x * (idx+1))
}
