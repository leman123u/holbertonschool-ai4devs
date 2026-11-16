# Bug Descriptions

## Bug 1 – bug1.py
**Intended Behavior**: Return the sum of all prices in a list.
**Issue Type**: Syntax error.
**Notes**: The `for` line is missing a colon, so the file does not run at all.

## Bug 2 – bug2.js
**Intended Behavior**: Return the average of an array of numbers.
**Issue Type**: Logical error.
**Notes**: Divides by `numbers.length - 1` instead of `numbers.length`, so the result is too high (135 instead of 90).

## Bug 3 – bug3.py
**Intended Behavior**: Return the age of a user by name.
**Issue Type**: Runtime exception.
**Notes**: Raises a `KeyError` when the name is not in the dictionary ("charlie").

## Bug 4 – bug4.c
**Intended Behavior**: Return the sum of all elements in an integer array.
**Issue Type**: Off-by-one error.
**Notes**: The loop uses `i <= size`, so it reads one element past the end of the array (undefined behavior).

## Bug 5 – bug5.js
**Intended Behavior**: Add an item price to the cart total and check for free shipping.
**Issue Type**: Misuse of data types.
**Notes**: `total` is a string, so `"50" + 25` gives `"5025"` (string concatenation) instead of `75`.