function solution(n) {
    const particles = [];
    while (n > 3) {
        if (n%3 === 0) {
            particles.push(3)
            n = n/3 -1;
        }
        else{
            particles.push(n%3);
            n = Math.floor(n/3);
        }
    }
    particles.push(n);
    
    let answer = "";
    for (let i = particles.length -1 ; i >= 0 ; i--){
        if (particles[i] === 3) answer += '4'
        else answer += particles[i]
    }
    return answer;
}
