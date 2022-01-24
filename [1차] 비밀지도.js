const toBinary = (n, number) => {
    const binary = [];
    
    while (number > 1) {
        binary.push(String(number % 2));
        number = Number.parseInt(number / 2);
    }
    binary.push(String(number));
    
    while (binary.length < n) binary.push("0");
    
    return binary.reverse();
}

const getCommonArray = (n, ar1, ar2) => {
    const returnArray = [];
    
    for (let i = 0 ; i < n ; i++) {
        if (ar1[i] === '1' | ar2[i] === '1') returnArray[i] = "#";
        else returnArray[i] = " ";
    }
    
    return returnArray;
}

function solution(n, arr1, arr2) {
    const answer = new Array(n);
    
    for (let i = 0 ; i < n ; i++) {
        const ar1 = toBinary(n, arr1[i]);
        const ar2 = toBinary(n, arr2[i]);
        const commonArray = getCommonArray(n, ar1, ar2);
        answer[i] = commonArray.join("");
    }
    
    return answer;
}
