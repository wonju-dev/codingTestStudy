function solution(s) {
    const numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"];
    return s.split("").every((char)=> numbers.includes(char) ? true : false) 
    && (s.length == 4 || s.length == 6) ? true : false;
}
