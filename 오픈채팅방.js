function solution(record) {
    const userList = {};
    let answer = [];
    record.forEach((line) => {
        const splittedLine = line.split(" ");
        const action = splittedLine[0]
        const uid = splittedLine[1];
        const name = splittedLine[2];
        if (name !== undefined) userList[uid] = name;
        
        if (action === 'Enter') {
            answer.push(`${uid} 님이 들어왔습니다.`)
        }
        else if (action === 'Leave') {
            answer.push(`${uid} 님이 나갔습니다.`)
        }
        else if (action === 'Change') {
            userList[uid] = name;
        }
    })
    return answer.map((event)=>{
        const chunks = event.split(" ");
        const userId = chunks[0];
        return userList[userId]+chunks[1]+ " " + chunks[2]; 
    })
}
