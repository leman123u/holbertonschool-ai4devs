## Bug 1 – bug1_fixed.py
- **Fix Applied**: Added the missing colon after `for price in prices`.
- **Test Method**: `assert` statements inside `bug1_fixed.py`, run with `python3 bug1_fixed.py`.
- **Input**: [10, 20, 30]
- **Expected Output**: 60
- **Actual Output**: 60 ✅
- **Input**: []
- **Expected Output**: 0
- **Actual Output**: 0 ✅
- **Input**: [5]
- **Expected Output**: 5
- **Actual Output**: 5 ✅
- **Terminal Output**:
```
Total: 60
All bug1 tests passed
```
- **Manual Tweaks**: None. The AI fix worked as suggested.

## Bug 2 – bug2_fixed.js
- **Fix Applied**: Divide by `numbers.length` instead of `numbers.length - 1`.
- **Test Method**: `assert.strictEqual` inside `bug2_fixed.js`, run with `node bug2_fixed.js`.
- **Input**: [80, 90, 100]
- **Expected Output**: 90
- **Actual Output**: 90 ✅
- **Input**: []
- **Expected Output**: 0
- **Actual Output**: 0 ✅
- **Input**: [7]
- **Expected Output**: 7
- **Actual Output**: 7 ✅
- **Terminal Output**:
```
Average: 90
All bug2 tests passed
```
- **Manual Tweaks**: Added an empty-array check that returns 0, because dividing by zero would give `NaN`.

## Bug 3 – bug3_fixed.py
- **Fix Applied**: Return `None` when the name is not in the dictionary instead of raising `KeyError`.
- **Test Method**: `assert` statements inside `bug3_fixed.py`, run with `python3 bug3_fixed.py`.
- **Input**: "alice"
- **Expected Output**: 30
- **Actual Output**: 30 ✅
- **Input**: "bob"
- **Expected Output**: 25
- **Actual Output**: 25 ✅
- **Input**: "charlie"
- **Expected Output**: None
- **Actual Output**: None ✅
- **Terminal Output**:
```
alice: 30
charlie: None
All bug3 tests passed
```
- **Manual Tweaks**: None. The AI fix worked as suggested.

## Bug 4 – bug4_fixed.c
- **Fix Applied**: Changed the loop condition from `i <= size` to `i < size`.
- **Test Method**: `assert()` calls inside `bug4_fixed.c`, compiled with `gcc -Wall -Wextra -Werror bug4_fixed.c -o bug4` and run with `./bug4`.
- **Input**: {1, 2, 3, 4, 5}, size 5
- **Expected Output**: 15
- **Actual Output**: 15 ✅
- **Input**: {42}, size 1
- **Expected Output**: 42
- **Actual Output**: 42 ✅
- **Input**: size 0
- **Expected Output**: 0
- **Actual Output**: 0 ✅
- **Terminal Output**:
```
Sum: 15
All bug4 tests passed
```
- **Manual Tweaks**: None. The AI fix worked as suggested.

## Bug 5 – bug5_fixed.js
- **Fix Applied**: Convert both values with `Number()` before adding them.
- **Test Method**: `assert.strictEqual` inside `bug5_fixed.js`, run with `node bug5_fixed.js`.
- **Input**: "50", 25
- **Expected Output**: 75
- **Actual Output**: 75 ✅
- **Input**: 50, 25
- **Expected Output**: 75
- **Actual Output**: 75 ✅
- **Input**: "10", "5"
- **Expected Output**: 15
- **Actual Output**: 15 ✅
- **Terminal Output**:
```
New total: 75
Free shipping!
All bug5 tests passed
```
- **Manual Tweaks**: Used `Number()` inside the function so it works even when both values are strings.