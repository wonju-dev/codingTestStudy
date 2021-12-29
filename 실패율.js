const getChallengingParticipants = (N, stages) => {
    const child = new Array(N);
    for (let i = 0 ; i < N ; i++) child[i] = 0;
    stages.forEach((stage)=> stage <= N ? child[stage-1] += 1 : "");
    return child;
}

const getFinishParticipants = (child, NUMBER_OF_PARTICIPANTS) => {
    return child.map((number,index)=>{
        let beforeNumber = 0;
        for (let i = 0 ; i < index ; i++) beforeNumber += child[i];
        return NUMBER_OF_PARTICIPANTS-beforeNumber;
    })
}

const calculateFinishRate = (mother, child) => {
    return mother.map((bot, index) => {
        if (child[index] !== 0) return child[index] / bot;
        else return 0;
    });
}

const getSortedRating = (rate, N) => {
    const answer = [];
    
    for (let i = 0 ; i < N ; i++) {
        let maxIndex = 0;
        for (let i = 1 ; i < rate.length ; i++) rate[i] > rate[maxIndex] ? maxIndex = i : ""; 
        answer.push(maxIndex+1);
        rate[maxIndex] = -1;
    }
    return answer;
}

function solution(N, stages) {
    const NUMBER_OF_PARTICIPANTS = stages.length;
    
    const child = getChallengingParticipants(N, stages);
    const mother = getFinishParticipants(child, NUMBER_OF_PARTICIPANTS);
    const rate = calculateFinishRate(mother, child);

    const answer = getSortedRating(rate, N);
    return answer;
}
