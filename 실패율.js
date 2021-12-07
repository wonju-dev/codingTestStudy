function solution(N, stages) {
    const challengeMap = {}
    stages.forEach((stage) => !challengeMap[stage] ? challengeMap[stage] = 1 : challengeMap[stage] += 1);
    
    const failureRate = [];
    let numOfStagePeople = stages.length;
    for (let i = 0 ; i < N; i ++){
        let numOfPeople = challengeMap[`${i+1}`] ? challengeMap[`${i+1}`] : 0;
        failureRate[i] = numOfPeople/ numOfStagePeople
        numOfStagePeople -= numOfPeople;
    }
    
    const answer = [];
    for (let i = 0 ; i < N ; i ++){
        const maxIndex = getMaxIndex(failureRate);
        answer.push(Number(maxIndex+1));
        failureRate.splice(maxIndex,1,-1);
    }
    return answer;
}

const getMaxIndex = (array) => {
    let maxIndex = 0 ;
    let maxValue = array[0];
    for (let i = 1 ; i < array.length ; i++){
        if (maxValue < array[i]){
            maxIndex = i;
            maxValue = array[i];
        }
    }
    return maxIndex;
}
