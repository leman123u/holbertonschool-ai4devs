# Cross-Language Specification - Log Analyzer

## 1. Project Overview

The Log Analyzer is a program designed to parse Apache web server log files and calculate important statistics about server activity.

The goal is to implement the same functionality in multiple programming languages while maintaining consistent input, output, and behavior.

## 2. Algorithm

The program must read and analyze Apache log files and calculate the following statistics:

- **Total Requests:** Count the total number of valid requests in the log file.
- **Unique Visitors:** Count the number of distinct IP addresses.
- **Error Rate:** Calculate the percentage of requests that resulted in HTTP error responses (4xx and 5xx status codes).

### Error Rate Formula

Error Rate = (Number of Error Requests / Total Valid Requests) × 100

If there are no valid requests, the error rate must be 0%.

## 3. Inputs

The program accepts:

- Apache access log files in plain text format.
- Each log entry should contain an IP address and an HTTP status code.
- Multiple log files may be provided for testing.

## 4. Outputs

The program must generate a JSON object containing the following statistics:

```json
{
  "total_requests": 100,
  "unique_visitors": 25,
  "error_rate": 20.0
}
```

The output must follow the same JSON structure in every supported programming language.

## 5. Edge Cases

The implementation must correctly handle the following situations:

- **Empty File:** Return 0 requests, 0 unique visitors, and 0% error rate.
- **Malformed Entry:** Skip invalid log entries without crashing.
- **Invalid IP Address:** Ignore entries containing invalid IP addresses.
- **Missing Status Code:** Skip entries without a valid HTTP status code.
- **No Errors:** Return an error rate of 0%.
- **All Errors:** Return an error rate of 100% if every valid request has an error status code.

## 6. Test Cases

| Test File | Expected Result |
|---|---|
| `log_small.txt` | 100 requests, 20 errors |
| `log_empty.txt` | 0 requests, 0 errors |

### Expected Results

**Test Case 1: log_small.txt**

- Total Requests: 100
- Error Requests: 20
- Unique Visitors: Calculated from distinct valid IP addresses
- Error Rate: 20%

**Test Case 2: log_empty.txt**

- Total Requests: 0
- Unique Visitors: 0
- Error Rate: 0%

## 7. Cross-Language Requirements

All implementations must:

- Follow the same algorithm and validation rules.
- Produce identical results for the same input files.
- Use JSON as the output format.
- Handle edge cases consistently.
- Include appropriate error handling.

## 8. Success Criteria

The project is considered successful when all supported language implementations produce consistent and accurate statistics for the provided test files.