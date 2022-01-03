function solution(price, money, count) {
    let expectedFee = 0;
    for (let i = 1; i <= count; i++) expectedFee += i * price;
    return expectedFee - money < 0 ? 0 : expectedFee - money; 
}
