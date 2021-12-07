function solution(N, stages) {
    const top = new Array(N+1);
    const bottom = new Array(N+1);
    for (let i = 1 ; i <= N ; i++){
        top[i] = 0;
        bottom[i] = 0;
    }
    stages.forEach((stage)=>{
        for (let i = 1 ; i <= N ; i ++) {
            if (stage >= i) bottom[i] += 1;
            if (stage === i) top[i] += 1;
        }
    })
    let failure = bottom.map((bot,index)=>{
        if (index !== 0) return Number(top[index] / bot)
    })
    failure = failure.slice(1,N+1);
    const answer = [];
    for (let i = 0 ; i < N ; i++){
        const maxIndex = getMaxIndex(failure);
        answer.push(Number(maxIndex+1));
        failure.splice(maxIndex,1);
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
