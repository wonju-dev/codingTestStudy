function solution(str1, str2) {
    const regex = /([A-Z]{2})/;
    const upperStr1 = str1.toUpperCase();
    const upperStr2 = str2.toUpperCase();
    const slicedStrings = {
        string1: [],
        string2: [],
    };
    [upperStr1, upperStr2].forEach((upperString, idx)=>{
        for (let i = 0 ; i < upperString.length -1 ; i ++) {
            const slicedString = upperString.slice(i,i+2);
            const string = regex.exec(slicedString);
            if (string) {
                if (idx === 0) slicedStrings.string1.push(string[0]);
                else slicedStrings.string2.push(string[0]);
            } 
        }
    })
    
    const copyString1 = slicedStrings.string1.slice();
    const copyString2 = slicedStrings.string2.slice();
    // 교집합
    const intersection = [];
    slicedStrings.string1.forEach((chunk1, string1Index) => {
        const string2Index = slicedStrings.string2.findIndex((chunk2) => chunk2 === chunk1);
        if (string2Index !== -1) {
            intersection.push(chunk1);
            slicedStrings.string1.splice(string1Index,1,-1);
            slicedStrings.string2.splice(string2Index,1,-1);
        }
    })
    // 합집합
    let union = [].concat(copyString1);
    copyString1.forEach((chunk1, string1Index) => {
        const string2Index = copyString2.findIndex((chunk2) => chunk2 === chunk1);
        if (string2Index !== -1){
            copyString2.splice(string2Index,1);
        }
    })
    union = union.concat(copyString2);
    if (intersection.length === 0 && union.length === 0) return 65536;
    return Math.floor(intersection.length / union.length * 65536);
}
