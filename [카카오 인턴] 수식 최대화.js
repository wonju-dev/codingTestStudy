function solution(expression) {
    const regex = /[\-\*\+]/g;
    // 1. 주어진 수식의 숫자, 연산 기호를 분리
    const operators = expression.match(regex);
    const operands = expression.split(regex);
    // 2. 분리한 연산 기호들의 실행 순서 순열 만듦 (아놔 3개만 고려하면 됐자너~~~~)
    const CASESE = [['+','-','*'],['+','*','-'],['-','+','*'],['-','*','+'],['*','-','+'],['*','+','-']]
    // 3. 경우를 하나씩 돌리기
    let biggestNumber = 0;
    CASESE.forEach((operatorCase)=>{
        const copyOperands = operands.slice();
        const copyOperators = operators.slice();
        operatorCase.forEach((operator)=>{
            while (copyOperators.includes(operator)) {
                const index = copyOperators.findIndex((operand)=>operand)
                copyOperators.splice(index,1);
                copyOperands[index+1] = eval(`${copyOperands[index]} ${operator} ${copyOperands[index+1]}`);
            }
            const number = copyOperands[operatorCase.length-1]
            if (biggestNumber < number) biggestNumber = number;
        })
    })
    return biggestNumber;   
}
