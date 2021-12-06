const FOR_LEFT = {
	1: 4,
	4: 3,
	7: 2
};
const FOR_RIGHT = {
	3: 4,
	6: 3,
	9: 2
};
const FOR_BOTH = {
	2: 4,
	5: 3,
	8: 2,
	0: 1
};

function solution(numbers, hand) {
	let answer = '';
	let lY = 1;
	let lX = 0;
	let rY = 1;
	let rX = 2;
	numbers.forEach((number, index) => {
		if (FOR_LEFT[Number(number)]) {
			answer += 'L';
			lY = FOR_LEFT[Number(number)];
			lX = 0;
		} else if (FOR_RIGHT[Number(number)]) {
			answer += 'R';
			rY = FOR_RIGHT[Number(number)];
			rX = 2;
		} else {
			const level = FOR_BOTH[number];
			const { leftDistance, rightDistance } = getDifference(level, lY, lX, rY, rX);
			if (leftDistance > rightDistance) {
				answer += 'R';
				rY = FOR_BOTH[Number(number)];
				rX = 1;
			} else if (leftDistance < rightDistance) {
				answer += 'L';
				lY = FOR_BOTH[Number(number)];
				lX = 1;
			} else {
				if (hand === 'right') {
					answer += 'R';
					rY = FOR_BOTH[Number(number)];
					rX = 1;
				} else {
					answer += 'L';
					lY = FOR_BOTH[Number(number)];
					lX = 1;
				}
			}
		}
	});
	return answer;
}

const getDifference = (numberLevel, lY, lX, rY, rX) => {
	const leftDistance = Math.abs(numberLevel - lY) + Math.abs(1 - lX);
	const rightDistance = Math.abs(numberLevel - rY) + Math.abs(1 - rX);
	return { leftDistance, rightDistance };
};
