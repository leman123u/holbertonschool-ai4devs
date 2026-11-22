
# Fix Validation Report

## bug1_fixed.py
- **Original Issue:** Off-by-one error in list slicing.
- **Fix Applied:** Changed the slicing operation to items[start:].
- **Test Case 1:** Get the last 3 items. Expected: [30, 40, 50].
- **Test Case 2:** Get the last 1 item. Expected: [50].
- **Test Case 3:** Request 0 items. Expected: [].
- **Test Results:** All 3 test cases are expected to pass.

## bug2_fixed.js
- **Original Issue:** Assignment operator used instead of comparison.
- **Fix Applied:** Replaced = with ===.
- **Test Case 1:** Calculate order without discount. Expected: 40.
- **Test Case 2:** Calculate order with discount. Expected: 35.
- **Test Case 3:** Apply discount to a small order. Expected: 0.
- **Test Results:** All 3 test cases are expected to pass.

## bug3_fixed.java
- **Original Issue:** Integer division caused inaccurate average calculation.
- **Fix Applied:** Used double division to preserve decimal values.
- **Test Case 1:** Calculate average of 75, 80 and 90. Expected: 81.666666...
- **Test Case 2:** Calculate average of 10 and 20. Expected: 15.0.
- **Test Case 3:** Empty array. Expected: 0.0.
- **Test Results:** All 3 test cases are expected to pass.

## bug4_fixed.cpp
- **Original Issue:** Array index out of bounds.
- **Fix Applied:** Changed loop condition from i <= size to i < size.
- **Test Case 1:** Find maximum in {12, 45, 23, 67, 34}. Expected: 67.
- **Test Case 2:** Find maximum in {-5, -2, -10}. Expected: -2.
- **Test Case 3:** Single element array {100}. Expected: 100.
- **Test Results:** All 3 test cases are expected to pass.

## bug5_fixed.py
- **Original Issue:** Incorrect password validation logic.
- **Fix Applied:** Return False when password requirements are not satisfied.
- **Test Case 1:** "hello123". Expected: False.
- **Test Case 2:** "HELLO123". Expected: True.
- **Test Case 3:** "HelloWorld". Expected: False.
- **Test Case 4:** "Hello123". Expected: True.

## Conclusion
4 buggy code snippets were corrected.
Test cases were prepared to verify the fixes.
All fixes should be executed and verified before final submission.
