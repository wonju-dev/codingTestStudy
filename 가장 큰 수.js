function solution(numbers) {
    let answer = "";
    let flag = new Array(numbers.length);
    for (let i = 0 ; i < flag.length ; i++) flag[i] = false;
    while (flag.includes(false)) {
        const biggestArray = findBiggest(numbers);
        if (biggestArray.length === 1) {
            const index = numbers.findIndex((number)=>number === biggestArray[0])
            numbers[index] = -1;
            flag[index] = true;
            answer += String(biggestArray[0]);
        }
        else {
            const biggest = compareNextDigit(biggestArray);
            const index = numbers.findIndex((number)=> number === Number(biggest));
            numbers[index] = -1;
            flag[index] = true;
            answer += String(biggest);
        }
    }
    return answer;
}

const compareNextDigit = (array) => {
    let longest = String(array[0]).length;
    for (let i = 1 ; i < array.length ; i++) {
        const nextLength = String(array[i]).length; 
        if (nextLength > longest) longest = nextLength;
    }
    const processedArray = array.map((number)=>{
        let stringNumber = String(number);
        if (String(number).length < longest) {
            let lastNumber = stringNumber[stringNumber.length-1];
            while (stringNumber.length !== longest) {
                stringNumber += lastNumber;
            }
        }
        return Number(stringNumber);
    })
    let biggestIndex = 0;
    for (let i = 0 ; i < processedArray.length ; i++) {
        if (processedArray[biggestIndex] < processedArray[i]) biggestIndex = i;
    }
    return array[biggestIndex];
}

const findBiggest = (numbers) => {
    let answer = [numbers[0]];
    const firstNumbers = numbers.map((number)=> number < 0 ? 0 : Number(String(number)[0]));
    let biggest = firstNumbers[0];
    for (let i = 1; i < firstNumbers.length ; i++) {
        if (biggest < firstNumbers[i]) {
            answer = []
            biggest = firstNumbers[i];
            answer.push(numbers[i]);
        } else if (biggest === firstNumbers[i]) {
            answer.push(numbers[i]);
        }
    }
    return answer;
}
