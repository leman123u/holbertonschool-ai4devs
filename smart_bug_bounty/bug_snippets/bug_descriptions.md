
# Bug Descriptions

## bug1.py
- **Language:** Python
- **Intended Behavior:** Return the last n items from a given list.
- **Current Issue:** The slicing operation uses an incorrect end index (`len(items) - 1`), causing the last element to be excluded.
- **Bug Type:** Off-by-one error.
- **Observed Output:** `Last items: [30, 40]` (expected `[30, 40, 50]`).

## bug2.js
- **Language:** JavaScript
- **Intended Behavior:** Calculate the total order price and apply a discount only when the discount parameter is true.
- **Current Issue:** The code uses assignment (`=`) instead of comparison (`===`), causing the condition to always evaluate as true.
- **Bug Type:** Assignment instead of comparison.
- **Observed Output:** `Order 1: 30` (expected 40) and `Order 2: 35`.

## bug3.java
- **Language:** Java
- **Intended Behavior:** Calculate the accurate average grade of students.
- **Current Issue:** Integer division removes the decimal part of the average.
- **Bug Type:** Incorrect numeric calculation.
- **Observed Output:** `Average grade: 81.0` (expected 81.666...).

## bug4.py
- **Language:** Python
- **Intended Behavior:** Find and return the maximum number in a list.
- **Current Issue:** The loop uses `range(1, len(numbers) + 1)`, causing an out-of-range list access on the last iteration.
- **Bug Type:** Array index out of bounds.
- **Observed Output:** Crashes with `IndexError: list index out of range`.
