function solution(id_list, report, k) {
    const reportList = {};
    id_list.forEach((id, index)=> reportList[id] = new Set())
    
    report.forEach((pair)=>{
        const [from, to] = pair.split(" ");
        reportList[to].add(from);
    })
    
    let answer = new Array(id_list.length);
    answer.fill(0);
    
    id_list.forEach((id)=>{
        if (reportList[id].size >= k) {
            for (let reporter of reportList[id]) {
                const index = id_list.findIndex((user)=> user === reporter);
                answer[index] +=1;
            }
        }
    }) 
    return answer;
}
