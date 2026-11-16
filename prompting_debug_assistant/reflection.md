# Reflection on AI-Assisted Debugging

## Introduction
In this project I created five buggy snippets in Python, JavaScript and C, covering a syntax error, a logical error, a runtime exception, an off-by-one loop and a data type misuse. I asked an AI assistant to identify and explain each bug, applied its fixes in `bug_fixes/`, and validated them with assertion tests. The goal was to measure how much the AI really helps and where a developer still has to think for themselves.

## AI Strengths
The easiest bugs for the AI were the ones with a clear error message. For `bug1.py`, the `SyntaxError` pointed straight to line 3, and the AI answered immediately: "The `for` statement is missing a colon at the end." For `bug3.py`, the `KeyError: 'charlie'` made the cause obvious, and the AI suggested three valid fixes (`if` check, `dict.get()` and `try/except`). The AI was also good at explaining *why* a bug happens, not only how to fix it. Its explanation of `"50" + 25` becoming `"5025"` in `bug5.js` was clear enough to teach the concept, not just patch the line.

## AI Weaknesses
The hardest bugs were the silent ones. `bug2.js` and `bug4.c` produced no error at all, so the AI depended entirely on my description of the expected output. In `bug4.c`, the out-of-bounds read sometimes printed a correct-looking sum, so without the hint "the result is sometimes random", the AI could easily miss it. The AI also did not think about edge cases on its own. Its fix for `bug2.js` changed `numbers.length - 1` to `numbers.length`, but it did not mention that an empty array would now return `NaN`. My trust level is therefore medium: I trust the AI's diagnosis when there is a stack trace, but I always verify its fixes with tests before accepting them.

## Human Role
Human intuition was required in three places. First, writing a good prompt: including the error message, the expected output and the actual output made the AI's answers much more accurate. Second, choosing between alternative fixes. For `bug3.py` I picked the `if` check for readability, and for `bug5.js` I placed `Number()` inside the function so it handles strings from any caller. Third, testing: I added `assert` statements and compiled the C code with `-Wall -Wextra -Werror` to prove each fix worked, including on edge cases the AI never mentioned.

## Conclusion
Overall, the AI made debugging faster, especially for explaining errors and suggesting fixes in seconds. However, it works best as an assistant, not as a replacement for the developer. The AI is strong at pattern recognition and explanation, but weak at understanding intent and edge cases. In real-world debugging, the best workflow is to give the AI rich context, treat its answer as a hypothesis, and confirm every fix with tests. The final responsibility for correct code stays with the human.