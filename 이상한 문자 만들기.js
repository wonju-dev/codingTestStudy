function solution(s) {
    let answer = [];
    
    const devidedWords = s.split(" ");
    for (let word of devidedWords) {
        const splitedWord = word.split("");
        
        answer.push(splitedWord.map((alphabet, index)=> {
            return index % 2 === 0 ? alphabet.toUpperCase() : alphabet.toLowerCase();
        }).join(""));
    } 
    return answer.join(" ");
}
