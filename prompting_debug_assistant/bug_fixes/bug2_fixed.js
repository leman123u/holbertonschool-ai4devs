const assert = require("assert");

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

assert.strictEqual(average([80, 90, 100]), 90);
assert.strictEqual(average([]), 0);
assert.strictEqual(average([7]), 7);
console.log("Average:", average([80, 90, 100]));
console.log("All bug2 tests passed");