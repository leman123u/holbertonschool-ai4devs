## Bug Report – bug1.py
- **File**: `bug_snippets/bug1.py` → fixed in `bug_fixes/bug1_fixed.py`
- **Summary**: Syntax error. The program does not run at all.
- **Root Cause**: The `for` statement is missing a colon at the end of the line.
- **Before**: `for price in prices`
- **After**: `for price in prices:`
- **Resolution (AI Suggestion)**: Add the missing colon after the `for` statement.
- **Resolution (Manual Edits)**: Added `assert` tests for a normal list, an empty list and a single item.
- **Lesson Learned**: Read the line number in a `SyntaxError` carefully; small typos stop the whole file from running.

## Bug Report – bug2.js
- **File**: `bug_snippets/bug2.js` → fixed in `bug_fixes/bug2_fixed.js`
- **Summary**: Logical error. The average is wrong (135 instead of 90).
- **Root Cause**: The sum is divided by `numbers.length - 1` instead of `numbers.length`.
- **Before**: `return sum / (numbers.length - 1);`
- **After**: `return sum / numbers.length;`
- **Resolution (AI Suggestion)**: Divide by `numbers.length`.
- **Resolution (Manual Edits)**: Added a check that returns 0 for an empty array to avoid `NaN`, plus `assert.strictEqual` tests.
- **Lesson Learned**: Code that runs without errors can still be wrong; always compare the output with a result calculated by hand.

## Bug Report – bug3.py
- **File**: `bug_snippets/bug3.py` → fixed in `bug_fixes/bug3_fixed.py`
- **Summary**: Runtime exception. The program crashes with `KeyError: 'charlie'`.
- **Root Cause**: The function reads `users[name]` without checking whether the key exists.
- **Before**: `return users[name]["age"]`
- **After**: `if name not in users: return None` then `return users[name]["age"]`
- **Resolution (AI Suggestion)**: Check that the name exists before reading it (alternatives: `dict.get()` or `try/except`).
- **Resolution (Manual Edits)**: Chose the `if` check for readability and added `assert` tests for existing and missing users.
- **Lesson Learned**: Never assume input data is complete; handle missing keys explicitly.

## Bug Report – bug4.c
- **File**: `bug_snippets/bug4.c` → fixed in `bug_fixes/bug4_fixed.c`
- **Summary**: Off-by-one error. The sum is wrong or random.
- **Root Cause**: The loop condition `i <= size` reads `arr[5]`, one element past the end of the array (undefined behavior).
- **Before**: `for (i = 0; i <= size; i++)`
- **After**: `for (i = 0; i < size; i++)`
- **Resolution (AI Suggestion)**: Change `<=` to `<` in the loop condition.
- **Resolution (Manual Edits)**: Added `assert()` tests and compiled with `-Wall -Wextra -Werror` to confirm there are no warnings.
- **Lesson Learned**: Array indexes go from 0 to size - 1; always check loop boundaries.

## Bug Report – bug5.js
- **File**: `bug_snippets/bug5.js` → fixed in `bug_fixes/bug5_fixed.js`
- **Summary**: Data type misuse. The total is `"5025"` instead of `75`.
- **Root Cause**: `total` is a string, so `+` joins text instead of adding numbers.
- **Before**: `return currentTotal + itemPrice;`
- **After**: `return Number(currentTotal) + Number(itemPrice);`
- **Resolution (AI Suggestion)**: Convert the values to numbers with `Number()` or `parseFloat()`.
- **Resolution (Manual Edits)**: Put `Number()` inside the function so it works even if both values are strings, and added `assert.strictEqual` tests.
- **Lesson Learned**: In JavaScript, check data types before using `+`; values from inputs or APIs are often strings.