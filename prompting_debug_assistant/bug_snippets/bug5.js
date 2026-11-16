function addToCart(currentTotal, itemPrice) {
  return currentTotal + itemPrice;
}

const total = "50";
const price = 25;

const newTotal = addToCart(total, price);
console.log("New total:", newTotal);

if (newTotal > 70) {
  console.log("Free shipping!");
}