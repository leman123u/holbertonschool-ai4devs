## Bug 1 – bug1_fixed.py
- **Fix Applied**: Added the missing colon after `for price in prices`.
- **Test 1 Input**: [10, 20, 30]
- **Expected Output**: 60
- **Actual Output**: 60 ✅
- **Test 2 Input**: [] (empty list)
- **Expected Output**: 0
- **Actual Output**: 0 ✅
- **Manual Tweaks**: None beyond the AI suggestion.

## Bug 2 – bug2_fixed.js
- **Fix Applied**: Divide by `numbers.length` instead of `numbers.length - 1`.
- **Test 1 Input**: [80, 90, 100]
- **Expected Output**: 90
- **Actual Output**: 90 ✅
- **Test 2 Input**: [] (empty array)
- **Expected Output**: 0
- **Actual Output**: 0 ✅
- **Manual Tweaks**: Added an empty-array check to avoid dividing by zero (returns `NaN` otherwise).

## Bug 3 – bug3_fixed.py
- **Fix Applied**: Check if the name exists before reading it from the dictionary.
- **Test 1 Input**: users, "alice"
- **Expected Output**: 30
- **Actual Output**: 30 ✅
- **Test 2 Input**: users, "charlie" (missing user)
- **Expected Output**: None (no crash)
- **Actual Output**: None ✅
- **Manual Tweaks**: None beyond the AI suggestion.

## Bug 4 – bug4_fixed.c
- **Fix Applied**: Changed the loop condition from `i <= size` to `i < size`.
- **Test 1 Input**: {1, 2, 3, 4, 5}, size = 5
- **Expected Output**: Sum: 15
- **Actual Output**: Sum: 15 ✅
- **Test 2 Input**: Compiled with `gcc -Wall -Wextra -Werror`
- **Expected Output**: No warnings or errors
- **Actual Output**: No warnings or errors ✅
- **Manual Tweaks**: None beyond the AI suggestion.

## Bug 5 – bug5_fixed.js
- **Fix Applied**: Convert both values with `Number()` before adding.
- **Test 1 Input**: total = "50", price = 25
- **Expected Output**: New total: 75
- **Actual Output**: New total: 75 ✅
- **Test 2 Input**: Free shipping check (75 > 70)
- **Expected Output**: Free shipping!
- **Actual Output**: Free shipping! ✅
- **Manual Tweaks**: Chose `Number()` inside the function so it also works if both values are strings.