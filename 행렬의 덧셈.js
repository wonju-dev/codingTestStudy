function solution(arr1, arr2) {
    const answer = [[]];

    arr1.forEach((arrr1, index)=> {
        arrr1.forEach((num, index2)=>{
            if (answer[index] === undefined) answer[index] = [num + arr2[index][index2]]
            else answer[index].push(num+arr2[index][index2])
        })
    }) 
    return answer;
}
