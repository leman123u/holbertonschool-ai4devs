# Prompt Use Cases

## Code Quality
- **Refactoring**
  - **Goal**: Improve readability and performance
  - **Input**: Source function in [LANGUAGE]
  - **Output**: Optimized code + explanation

- **Style Enforcement**
  - **Goal**: Enforce consistent naming and formatting
  - **Input**: Code block + style guide (e.g., PEP 8)
  - **Output**: Rewritten code with consistent style

- **Complexity Reduction**
  - **Goal**: Simplify nested logic and long functions
  - **Input**: Function with high complexity
  - **Output**: Smaller functions + summary of changes

## Debugging
- **Error Explanation**
  - **Goal**: Understand an error message or stack trace
  - **Input**: Error output + related code
  - **Output**: Root cause + suggested fix

- **Bug Localization**
  - **Goal**: Find where unexpected behavior comes from
  - **Input**: Code + expected vs. actual behavior
  - **Output**: Likely faulty lines + reasoning

- **Logging Strategy**
  - **Goal**: Add useful logs to trace an issue
  - **Input**: Function or module
  - **Output**: Code with targeted log statements

## Documentation
- **Docstring Generation**
  - **Goal**: Document functions consistently
  - **Input**: Function code in [LANGUAGE]
  - **Output**: Docstrings in the requested format

- **README Creation**
  - **Goal**: Produce a clear project README
  - **Input**: Project description + file structure
  - **Output**: README.md with setup, usage and examples

- **API Documentation**
  - **Goal**: Describe endpoints for API users
  - **Input**: Route or controller code
  - **Output**: Endpoint table with parameters and responses

## Testing
- **Unit Test Generation**
  - **Goal**: Cover a function with unit tests
  - **Input**: Function + test framework name
  - **Output**: Test file covering normal and edge cases

- **Edge Case Discovery**
  - **Goal**: Find inputs likely to break the code
  - **Input**: Function signature + description
  - **Output**: List of edge cases with expected results

- **Test Data Creation**
  - **Goal**: Generate realistic mock data
  - **Input**: Data schema
  - **Output**: Sample data in JSON or CSV