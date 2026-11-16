function average(numbers) {
  if (numbers.length === 0) {
    return 0;
  }
  let sum = 0;
  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
  }
  return sum / numbers.length;
}

const scores = [80, 90, 100];
console.log("Average:", average(scores));
console.log("Empty:", average([]));