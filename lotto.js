const result = [6,6,5,4,3,2,1]
const checkSameNumber = (lottos, win_nums) => lottos.filter((number)=> win_nums.includes(number)).length;

function solution(lottos, win_nums) {
    const numberOfSameNumber = checkSameNumber(lottos, win_nums);
    const numberOfZero = lottos.filter((number)=> number === 0).length;
    return [result[numberOfSameNumber+numberOfZero], result[numberOfSameNumber]];
}
