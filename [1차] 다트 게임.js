const CHUNK_REGEX = /\d{1,}[D,S,T]|[#,*]/g;
const getChunks = (dartResult) => [...dartResult.matchAll(CHUNK_REGEX)].map((chunk)=> chunk[0]);

const DIVIDE_REGEX = /\d{1,}|[D,S,T]/g;
const divide = (chunk) => {
    const tmp = [...chunk.matchAll(DIVIDE_REGEX)];
    return [tmp[0][0], tmp[1][0]];
}

const CHAR_MAP = {
    "*" : 2,
    "#" : -1
}

const SCORE_MAP = {
    "S" : 1,
    "D" : 2,
    "T" : 3
}

function solution(dartResult) {
    const chunks = getChunks(dartResult);

    let index = 0;
    while (index < chunks.length) {
        if (chunks[index] !== "*" && chunks[index] !== "#") {
            const [number, area] = divide(chunks[index]); 
            chunks[index] = number ** SCORE_MAP[area];
        } else {
            if (chunks[index] === "*" && index-2 >= 0) chunks[index-2] = chunks[index-2] * CHAR_MAP[chunks[index]];
            chunks[index-1] = chunks[index-1] * CHAR_MAP[chunks[index]];
            chunks.splice(index,1);
            index --;
        }
        index ++;
    }
    
    return chunks.reduce((a,b) => a + b);
}
