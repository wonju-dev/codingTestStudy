function solution(s) {
  let answer = 1;
  let index = 0;
  while (index < s.length) {
    if (s[index + 1] === undefined) {
      answer = 0;
    }
    console.log(s[index], s[index + 1]);
    if (s[index] === s[index + 1]) {
      s = s.slice(0, index) + s.slice(index + 2);
      console.log(s);
      if (index !== 0) index -= 1;
    } else index += 1;
  }
  return answer;
}
