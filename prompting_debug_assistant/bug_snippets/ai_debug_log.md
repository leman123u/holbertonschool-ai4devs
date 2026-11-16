## Bug 1 – bug1.py
**Prompt Used**: "This code throws an error. Can you identify and explain the issue and how to fix it?"
**Error**: `SyntaxError: expected ':'` on line 3.
**AI Diagnosis**: The `for` statement is missing a colon at the end. Python requires a colon after `for`, `if`, `def` and similar statements, so the file cannot run at all.
**Suggested Fix**: Change `for price in prices` to `for price in prices:`.
**Alternative Fixes Tested**: Replacing the loop with `return sum(prices)`. Both versions work.
**Result**: Fix works as expected. Output: `Total: 60`.

## Bug 2 – bug2.js
**Prompt Used**: "This code doesn't behave as expected. Can you identify and explain the issue and how to fix it?"
**Error**: No error, but the output is `Average: 135` instead of `Average: 90`.
**AI Diagnosis**: The function divides the sum by `numbers.length - 1` instead of `numbers.length`. With 3 numbers it divides 270 by 2 instead of 3, so the average is too high.
**Suggested Fix**: Change `return sum / (numbers.length - 1);` to `return sum / numbers.length;`.
**Alternative Fixes Tested**: Using `numbers.reduce((a, b) => a + b, 0) / numbers.length`. Both versions work.
**Result**: Fix works as expected. Output: `Average: 90`.

## Bug 3 – bug3.py
**Prompt Used**: "This code throws an error. Can you identify and explain the issue and how to fix it?"
**Error**: `KeyError: 'charlie'`.
**AI Diagnosis**: The function reads `users[name]` without checking whether the name exists. "charlie" is not in the dictionary, so Python raises a `KeyError` and the program crashes.
**Suggested Fix**: Check first: `if name not in users: return None`, then return `users[name]["age"]`.
**Alternative Fixes Tested**: Using `users.get(name, {}).get("age")`, and wrapping the lookup in `try/except KeyError`. All three work; the `if` check was chosen because it is the clearest.
**Result**: Fix works as expected. Output: `30` then `None`.

## Bug 4 – bug4.c
**Prompt Used**: "This code doesn't behave as expected. Can you identify and explain the issue and how to fix it?"
**Error**: No compile error, but the sum is wrong or random (for example `Sum: 32782` instead of `Sum: 15`).
**AI Diagnosis**: The loop condition `i <= size` runs one extra time and reads `arr[5]`, which is outside the array (valid indexes are 0 to 4). This is an off-by-one error and undefined behavior.
**Suggested Fix**: Change `i <= size` to `i < size`.
**Alternative Fixes Tested**: Looping with `i <= size - 1`. Both work, but `i < size` is the standard style.
**Result**: Fix works as expected. Output: `Sum: 15`.

## Bug 5 – bug5.js
**Prompt Used**: "This code doesn't behave as expected. Can you identify and explain the issue and how to fix it?"
**Error**: No error, but the output is `New total: 5025` instead of `New total: 75`.
**AI Diagnosis**: `total` is the string `"50"`, not a number. In JavaScript, `+` with a string joins text instead of adding, so `"50" + 25` becomes `"5025"`.
**Suggested Fix**: Store the total as a number: `const total = 50;`.
**Alternative Fixes Tested**: Converting inside the function with `Number(currentTotal) + Number(itemPrice)`, and with `parseFloat`. All work; `Number()` inside the function is safest because it also handles string input.
**Result**: Fix works as expected. Output: `New total: 75` and `Free shipping!`.