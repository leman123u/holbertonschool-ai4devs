## Bug 1 – bug1_fixed.py
- **Fix Applied**: Added the missing colon after `for price in prices`.
- **Test Command**: `python3 bug1_fixed.py`
- **Test 1 Input**: [10, 20, 30]
- **Expected Output**: Total: 60
- **Actual Output**: Total: 60 ✅
- **Test 2 Input**: [] (empty list)
- **Expected Output**: Empty: 0
- **Actual Output**: Empty: 0 ✅
- **Terminal Output**:
```
Total: 60
Empty: 0
```
- **Status**: PASS

## Bug 2 – bug2_fixed.js
- **Fix Applied**: Divide by `numbers.length` instead of `numbers.length - 1`. Added a check that returns 0 for an empty array.
- **Test Command**: `node bug2_fixed.js`
- **Test 1 Input**: [80, 90, 100]
- **Expected Output**: Average: 90
- **Actual Output**: Average: 90 ✅
- **Test 2 Input**: [] (empty array)
- **Expected Output**: Empty: 0
- **Actual Output**: Empty: 0 ✅
- **Terminal Output**:
```
Average: 90
Empty: 0
```
- **Status**: PASS

## Bug 3 – bug3_fixed.py
- **Fix Applied**: Return `None` if the name is not in the dictionary instead of crashing.
- **Test Command**: `python3 bug3_fixed.py`
- **Test 1 Input**: users, "alice"
- **Expected Output**: 30
- **Actual Output**: 30 ✅
- **Test 2 Input**: users, "charlie"
- **Expected Output**: None
- **Actual Output**: None ✅
- **Terminal Output**:
```
30
None
```
- **Status**: PASS

## Bug 4 – bug4_fixed.c
- **Fix Applied**: Changed the loop condition from `i <= size` to `i < size`.
- **Test Command**: `gcc -Wall -Wextra -Werror bug4_fixed.c -o bug4 && ./bug4`
- **Test 1 Input**: {1, 2, 3, 4, 5}, size = 5
- **Expected Output**: Sum: 15
- **Actual Output**: Sum: 15 ✅
- **Test 2 Input**: Compile with strict warnings
- **Expected Output**: No warnings or errors
- **Actual Output**: No warnings or errors ✅
- **Terminal Output**:
```
Sum: 15
```
- **Status**: PASS

## Bug 5 – bug5_fixed.js
- **Fix Applied**: Convert both values with `Number()` before adding.
- **Test Command**: `node bug5_fixed.js`
- **Test 1 Input**: total = "50", price = 25
- **Expected Output**: New total: 75
- **Actual Output**: New total: 75 ✅
- **Test 2 Input**: Free shipping check (75 > 70)
- **Expected Output**: Free shipping!
- **Actual Output**: Free shipping! ✅
- **Terminal Output**:
```
New total: 75
Free shipping!
```
- **Status**: PASS