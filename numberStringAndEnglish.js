const MAP = {
    zero : '0',
    one : '1',
    two: '2',
    three:'3',
    four:'4',
    five:'5',
    six:'6',
    seven:'7',
    eight:'8',
    nine:'9'
}

const getKey = (array) => {
    if (array.length === 0) return false;
    
    const key = array.reduce((a,b)=> a+=b); 
    if (MAP[key] === undefined) return false;
    else return key;
}

let strings = [];
function solution(s) {
    let answer = "";
    const NUMBERS = Object.values(MAP)
    for (let i = 0 ; i < s.length ; i++){
        if (NUMBERS.includes(s[i])) answer += s[i];
        else strings.push(s[i]);
        const key = getKey(strings);
        if (key) {
            answer += MAP[key]
            strings = [];
        };
    }
    return Number(answer);
}
