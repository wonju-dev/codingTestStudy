// 이전에는 아무도 도착하지 못한 Stage를 고려하지 않았다

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
    
    const rate = mother.map((bot, index) => {
        if (child[index] !== 0) return child[index] / bot;
        else return 0;
    });

    const answer = [];
    for (let i = 0 ; i < N ; i++) {
        let maxIndex = 0;
        for (let i = 1 ; i < rate.length ; i++){
            if (rate[i] > rate[maxIndex]) maxIndex = i; 
        }
        answer.push(maxIndex+1);
        rate[maxIndex] = -1;
    }
    return answer;
}
