function solution(numbers) {
    const fourLength = numbers.map((number)=>{
        const numberLength = String(number).length; 
        if (numberLength < 4) {
            let stringedNumber = String(number);
            for (let i = numberLength; i < 4 ; i++) stringedNumber += stringedNumber[numberLength-1]; 
            return stringedNumber;
        }
    })
    let answer = "";
    while (fourLength.length !==0) {
        const biggestIndex = getBiggestIndex(fourLength);
        answer += String(numbers[biggestIndex]);
        numbers.splice(biggestIndex,1);
        fourLength.splice(biggestIndex,1);
    }
    while (answer[0] === '0') answer = answer.slice(1);
    return answer === "" ? '0' : answer;
}

const getBiggestIndex = (array) => {
    let biggestIndex = 0;
    for (let i = 1; i < array.length ; i++) if (array[biggestIndex] < array[i]) biggestIndex = i;
    return biggestIndex;
}
