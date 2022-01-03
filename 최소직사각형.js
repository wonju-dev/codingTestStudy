function solution(sizes) {
    let w = 0, h = 0; 
    sizes.forEach((size)=>{
        const sortedSize = size.sort((a, b)=> a - b);
        if (sortedSize[0] > w) w = sortedSize[0];
        if (sortedSize[1] > h) h = sortedSize[1];
    })
    return w * h
}
