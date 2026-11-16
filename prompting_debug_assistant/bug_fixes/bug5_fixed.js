const assert = require("assert");

function addToCart(currentTotal, itemPrice) {
  return Number(currentTotal) + Number(itemPrice);
}

assert.strictEqual(addToCart("50", 25), 75);
assert.strictEqual(addToCart(50, 25), 75);
assert.strictEqual(addToCart("10", "5"), 15);

const newTotal = addToCart("50", 25);
console.log("New total:", newTotal);
if (newTotal > 70) {
  console.log("Free shipping!");
}
console.log("All bug5 tests passed");