const getCombinations = function (arr, selectNumber) {
  const results = [];
  if (selectNumber === 1) return arr.map((value) => [value]); 

  arr.forEach((fixed, index, origin) => {
    const rest = origin.slice(index + 1); 
    const combinations = getCombinations(rest, selectNumber - 1); 
    const attached = combinations.map((combination) => [fixed, ...combination]); 
    results.push(...attached);
  });

  return results; 
}


function solution(orders, course) {
    const menuList = {};
    orders.forEach((order)=>{
        const splittedOrder = order.split('').sort();
        const possibleCombinations = getCombinations(splittedOrder,2);
        possibleCombinations.forEach((combination)=>{
            const joinedMenu = combination.join('')
            if (menuList[joinedMenu]) menuList[joinedMenu] +=1;
            else menuList[joinedMenu] = 1;
        })
    })
    const tmp = Object.keys(menuList).filter((menu)=> menuList[menu] >= 2);
    
    const answer = {};
    orders.forEach((order, index)=>{
        tmp.forEach((subMenu)=>{
            if (course.includes(order.length) && order.includes(subMenu)) answer[index] =order ;
        })
    })
    return Object.values(answer).sort();
}
