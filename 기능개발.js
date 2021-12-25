function solution(progresses, speeds) {
  const answer = [];
  const inQueue = [];
  for (let i = 0; i < progresses.length; i++) inQueue.push(false);
  let finishedTask = [];
  let nextPublishVersion = 0;

  while (inQueue.includes(false)) {
    let publishCount = 0;
    progresses.forEach((_, index) => {
      if (progresses[index] <= 100) progresses[index] += speeds[index];
      if (progresses[index] >= 100 && speeds[index] !== 0) {
        speeds[index] = 0;
        finishedTask.push(index);
        inQueue[index] = true;
      }
    });

    finishedTask.sort((a, b) => a - b);

    for (let i = 0; i < finishedTask.length; i++) {
      if (finishedTask[i] === nextPublishVersion) {
        nextPublishVersion += 1;
        publishCount += 1;
      } else break;
    }
    if (publishCount !== 0) {
      answer.push(publishCount);
      finishedTask.splice(0, publishCount);
    }
  }
  return answer;
}
