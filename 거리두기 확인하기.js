const getDistance = (p1, p2) => Math.abs(p1[0] - p2[0]) + Math.abs(p1[1] - p2[1]);
const getDirection = (p1, p2) => {
    if (p1[1] === p2[1]) return [1,[p1[0]+1,p1[1]]];
    else if (p1[0] === p2[0]) return [2,[p1[0],p1[1]+1]];
    else if (p1[0] - p2[0] === -1) return [3, [p1[0],p1[1]+1],[p1[0]+1,p1[1]]];
    else if (p1[0] - p2[0] === 1) return [4,  [p1[0],p1[1]-1],[p1[0]+1,p1[1]]];
}

function solution(places) {
    const answer = [];
    const usersPoisition = [];
    places.forEach((place)=>{
        const userPosition = [];
        place.forEach((row, rowIndex)=>{
            for (let colIndex = 0 ; colIndex < row.length ; colIndex ++) {
                if (row[colIndex] === "P") userPosition.push([rowIndex, colIndex]);
            }
        })
        usersPoisition.push(userPosition);
    })

    for (let i = 0 ; i < usersPoisition.length ; i ++) {
        if (usersPoisition[i].length === 0) answer.push(1)
        else {
            let index = 0 ;
            let flag = 1;
            while (index < usersPoisition[i].length - 1) {
                let nextIndex = index + 1;
                while (nextIndex < usersPoisition[i].length) {
                    const distance = getDistance(usersPoisition[i][index], usersPoisition[i][nextIndex]);
                    if (distance <= 2) {
                        const [direction, p1,p2] = getDirection(usersPoisition[i][index], usersPoisition[i][nextIndex]);
                        if (direction === 1 && ["P","O"].includes(places[i][p1[0]][p1[1]])) { 
                            flag = 0;
                            nextIndex = usersPoisition.length;
                            index = usersPoisition.length -1;
                        }
                        else if (distance === 2 && ["P","O"].includes(places[i][p1[0]][p1[1]])) {
                            flag = 0;
                            nextIndex = usersPoisition.length;
                            index = usersPoisition.length -1;
                        }
                        else if (distance === 3 && (["P","O"].includes(places[i][p1[0]][p1[1]]) || ["P","O"].includes(places[i][p2[0]][p2[1]]))) {
                            flag = 0;
                            nextIndex = usersPoisition.length;
                            index = usersPoisition.length -1;
                        }
                        else if (distance === 4 && (["P","O"].includes(places[i][p1[0]][p1[1]]) || ["P","O"].includes(places[i][p2[0]][p2[1]]))) {
                            flag = 0;
                            nextIndex = usersPoisition.length;
                            index = usersPoisition.length -1;
                        }
                        else nextIndex +=1;
                    } else nextIndex += 1;
                }
                index += 1;
            }
            answer.push(flag);
        }
    }
    return answer
}
