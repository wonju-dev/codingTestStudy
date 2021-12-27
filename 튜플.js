const parseString = (string) => {
    const numbers = [];
    let chunk = '';
    let isInBraket = false;
    for (let i = 0 ; i < string.length ; i++) {
        if (string[i] === '{') {
            isInBraket = true;
            chunk += '[';
        }
        else if (string[i] === '}' && isInBraket === true) {
            isInBraket = false;
            numbers.push(eval(chunk + ']'));
            chunk = '';
        }
        else if (isInBraket === true) chunk += string[i]
    }
    return numbers;
}

function solution(s) {
    const numberArrays = parseString(s.slice(1, s.length-1));
    const ranking = {};
    numberArrays.forEach((numberArray)=>{
        numberArray.forEach((number)=>{
            if (ranking[number] !== undefined) ranking[number] += 1
            else ranking[number] = 1;
        })
    })
    const counts = Object.values(ranking);
    counts.sort((a,b) => a-b);
    const elements = Object.keys(ranking);
    const answer = [];
    while (counts.length !== 0) {
        const biggest = counts.pop();
        elements.forEach((element)=>{
            if (ranking[element] === biggest) {
                answer.push(Number(element));
            } 
        })
    }
    return answer;
}
