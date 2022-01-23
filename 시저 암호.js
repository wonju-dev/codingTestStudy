const isInAlphabetBound = (ascii, n) => ((ascii >= 65 & ascii <= 90) & ascii + n <= 90) | ((ascii >= 97 & ascii <= 122) & ascii + n <= 122);

function solution(s, n) {
    let chars = s.split("");
    
    chars = chars.map((char)=>{
        if (char === " ") return " ";
        
        const ascii = char.charCodeAt(0);
        if (isInAlphabetBound(ascii, n)) return String.fromCharCode(ascii + n);
        else return String.fromCharCode(ascii + n - 26);
    });
    
    return chars.join("");
}
