function solution(str1, str2) {
    const regex = /(?<string>[\w]*)/;
    const upperStr1 = str1.toUpperCase();
    const upperStr2 = str2.toUpperCase();
    const slicedStrings = {
        string1: [],
        string2: [],
    };
    [upperStr1, upperStr2].forEach((upperString, idx)=>{
        for (let i = 0 ; i < upperString.length -1 ; i ++) {
            const slicedString = upperString.slice(i,i+2);
            const string = regex.exec(slicedString).groups['string']; 
            if (string) {
                if (idx === 0) slicedStrings.string1.push(string);
                else slicedStrings.string2.push(string);
            } 
        }
    })
    
    const s1s = slicedStrings.string1.slice();
    const s2s = slicedStrings.string2.slice();
    
    const Sum = s1;
    s1.forEach((string)=>{
        const index = s2.findIndex((string2)=>string2===string);
        if (index !== -1) s2.splice(index,1);
    })
    const newSum = Sum.concat(s2);
    
    const common = [];
    s1s.forEach((string, index)=>{
        const s2Index = s2s.findIndex((s2String)=> s2String === string);
        if (s2Index !== -1) {
            common.push(s1s[index]);
            s1.splice(index,1,-1);
            s2s.splice(s2Index,1,-1);
        } 
    })
    return  common.length / newSum.length * 65536;
}
