function checkSame (lottos, win_nums){
    let best = 0;
    for (let i = 0; i < lottos.length ; i++) {
        if (lottos[i] === 0) continue;
        for (let j = 0 ; j < win_nums.legnth ; j++) {
            if (lottos[i]===win_nums[j]) best -=1;
        }
    }
    return best;
}

function solution(lottos, win_nums) {
    let best = 6;
    const checkSameNumber = checkSame(lottos, win_nums);
    best -= checkSameNumber;
    best -= lottos.filter((number)=>number === 0).length;
    const worst = 6 - checkSameNumber;
    return [best, worst];
}
