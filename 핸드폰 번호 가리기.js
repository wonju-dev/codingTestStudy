function solution(phone_number) {
    return phone_number.split('').map((number, index)=> 
        index <= phone_number.length - 5 ? "*" : number
     ).join("");
}
