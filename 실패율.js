const init = (N) => {
    const mother = new Array(N);
    const child = new Array(N);
    for (let i = 0 ; i < N ; i++){
        mother[i] = 0;
        child[i] = 0;
    }
    return [mother, child];
}

function solution(N, stages) {
    const [mother, child] = init(N);    
    
    stages.forEach((stage)=>{
        if (stage > N) for (let i = 0; i < stage-1 ; i++) mother[i] += 1;
        else {
            for (let i = 0; i < stage ; i++) mother[i] += 1;
            child[stage-1] +=1;
        }
    })
    
    const rate = mother.map((bot, index) => child[index] / bot);

    const answer = [];
    while (rate.reduce((a,b)=>a+b) !== -1 * N) {
        let maxIndex = 0;
        for (let i = 1 ; i < rate.length ; i++){
            if (rate[i] > rate[maxIndex]) maxIndex = i; 
        }
        answer.push(maxIndex+1);
        rate[maxIndex] = -1;
    }
    
    return answer;
}

/*
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
*/
