function average(numbers) {
  let sum = 0;
  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
  }
  return sum / (numbers.length - 1);
}

const scores = [80, 90, 100];
console.log("Average:", average(scores));