const CHUNK_REGEX = /\d{1,}[D,S,T]|[#,*]/g;
const getChunks = (dartResult) => [...dartResult.matchAll(CHUNK_REGEX)].map((chunk)=> chunk[0]);

const DIVIDE_REGEX = /\d{1,}|[D,S,T]/g;
const divide = (chunk) => {
    const tmp = [...chunk.matchAll(DIVIDE_REGEX)];
    return [tmp[0][0], tmp[1][0]];
}


function solution(dartResult) {
    const chunks = getChunks(dartResult);

    let i = 0;
    while (i < chunks.length) {
        if (chunks[i] === "*") {
            if (i-2 >= 0) chunks[i-2] = chunks[i-2] * 2;
            chunks[i-1] = chunks[i-1] * 2;
            chunks.splice(i,1);
            i --;
        }
        else if (chunks[i] === "#") {
            chunks[i-1] = chunks[i-1] * -1;
            chunks.splice(i,1);
            i --;
        }
        else {
            const [number, area] = divide(chunks[i]); 
            let num = 1;
            switch(area) {
                case "S":
                    num = 1;
                    break;
                case "D":
                    num = 2;
                    break;
                case "T":
                    num = 3;
                    break;
            }
            chunks[i] = number ** num;
        }
        i ++;
    }
    
    return chunks.reduce((a,b) => a + b);
}
