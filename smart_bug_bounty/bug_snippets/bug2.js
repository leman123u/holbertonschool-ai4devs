
function calculateOrderTotal(price, quantity, discount) {
    if (price < 0 || quantity < 0) {
        return "Invalid order";
    }

    let total = price * quantity;

    if (discount = true) {
        total = total - 10;
    }

    if (total < 0) {
        total = 0;
    }

    return total;
}

const order1 = calculateOrderTotal(20, 2, false);
const order2 = calculateOrderTotal(15, 3, true);

console.log("Order 1:", order1);
console.log("Order 2:", order2);
