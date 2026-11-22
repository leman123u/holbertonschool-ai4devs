
# Bug Descriptions

## bug1.py
- **Language:** Python
- **Intended Behavior:** Return the last n items from a given list.
- **Current Issue:** The slicing operation uses an incorrect end index, causing the last element to be excluded.
- **Bug Type:** Off-by-one error.

## bug2.js
- **Language:** JavaScript
- **Intended Behavior:** Calculate the total order price and apply a discount only when the discount parameter is true.
- **Current Issue:** The code uses assignment (=) instead of comparison (===), causing the condition to always evaluate as true.
- **Bug Type:** Assignment instead of comparison.

## bug3.java
- **Language:** Java
- **Intended Behavior:** Calculate the accurate average grade of students.
- **Current Issue:** Integer division removes the decimal part of the average.
- **Bug Type:** Incorrect numeric calculation.

## bug4.cpp
- **Language:** C++
- **Intended Behavior:** Find and return the maximum number in an array.
- **Current Issue:** The loop condition uses <= instead of <, causing an out-of-bounds array access.
- **Bug Type:** Array index out of bounds.

