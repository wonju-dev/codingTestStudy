function solution(expression) {
    const regex = /[\-\*\+]/g;
    // 1. 주어진 수식의 숫자, 연산 기호를 분리
    const operators = expression.match(regex);
    const operands = expression.split(regex);
    // 2. 분리한 연산 기호들의 실행 순서 순열 만듦
    const CASESE = [['+','-','*'],['+','*','-'],['-','+','*'],['-','*','+'],['*','-','+'],['*','+','-']]
    // 3. 경우를 하나씩 돌리기
    let biggestNumber = 0;
    CASESE.forEach((operatorCase)=>{
        const copyOperands = operands.slice();
        const copyOperators = operators.slice();
        operatorCase.forEach((targetOperator)=>{
            while (copyOperators.includes(targetOperator)) {
                const index = copyOperators.findIndex((operator)=>operator === targetOperator);
                copyOperands[index] = eval(`${copyOperands[index]} ${targetOperator} ${copyOperands[index+1]}`);
                copyOperators.splice(index,1);
                copyOperands.splice(index+1,1);
            }
        })
        const number = Math.abs(copyOperands[0]);
        if (biggestNumber < number) biggestNumber = number;
    })
    return biggestNumber;   
}
