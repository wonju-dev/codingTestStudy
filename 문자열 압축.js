function solution(s) {
    const chunks = {};
    var answer = {};
    for (let i = 1 ; i <= s.length ; i++) {
        chunks[i] = [];
        for (let j = 0 ; j < s.length ; j += i){
            chunks[i].push(s.slice(j,j+i));
        }
    }
    const counter = {} ;
    for (let i = 1 ; i <= s.length ; i++) {
        counter[i] = 0;
        let number = 1;
        for (let j = 0; j < chunks[i].length ; j ++){
            if (chunks[i][j] !== chunks[i][j+1]) {
                if (number === 1) {
                    if (j === chunks[i].length -1) counter[i] += chunks[i][j].length;
                    else counter[i] += i;
                }
                else {
                    counter[i] += i+1;
                    number = 1;
                }
            }
            else number +=1
        }
    }
    return Math.min(...Object.values(counter));
}
