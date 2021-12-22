function solution(nums) {
    const number = nums.length / 2;
    const array = [...new Set(nums)];
    let answer = 0;
    for (let i = 0 ; i < number; i ++){
        if (array[i] === undefined) break;
        answer +=1;
    }
    return answer;
}
