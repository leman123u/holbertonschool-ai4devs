# Cross-Language Specification - Log Analyzer

## 1. Project Overview

The Log Analyzer is a program designed to parse Apache web server access log files and calculate important statistics about server activity.

The project aims to implement the same functionality in multiple programming languages while ensuring consistent input processing, output formatting, and behavior.

## 2. Algorithm

The program must read and analyze Apache access log files and calculate the following statistics:

- **Total Requests:** Count the total number of valid requests.
- **Unique Visitors:** Count the number of distinct valid IP addresses.
- **Error Requests:** Count requests with HTTP status codes between 400 and 599.
- **Error Rate:** Calculate the percentage of valid requests that resulted in HTTP errors.

### Error Rate Formula

Error Rate = (Error Requests / Total Requests) × 100

If the total number of valid requests is zero, the error rate must be 0%.

### Processing Steps

1. Read the Apache log file line by line.
2. Extract the IP address and HTTP status code from each entry.
3. Validate the IP address and HTTP status code.
4. Skip malformed or invalid entries.
5. Count all valid requests.
6. Count unique IP addresses.
7. Count HTTP error responses (4xx and 5xx).
8. Calculate the error rate.
9. Generate the final statistics in JSON format.

## 3. Inputs

The program accepts:

- Apache access log files in plain text format.
- Each valid log entry must contain an IP address and an HTTP status code.
- Multiple log files may be provided for testing.

### Example Input

```text
192.168.1.10 - - [19/Nov/2026:10:00:00 +0000] "GET /index.html HTTP/1.1" 200 1024
192.168.1.11 - - [19/Nov/2026:10:01:00 +0000] "GET /about.html HTTP/1.1" 404 512
192.168.1.10 - - [19/Nov/2026:10:02:00 +0000] "POST /login HTTP/1.1" 500 256
```

## 4. Outputs

The program must generate a JSON object containing the calculated statistics.

### Example Output

```json
{
  "total_requests": 3,
  "unique_visitors": 2,
  "error_requests": 2,
  "error_rate": 66.67
}
```

All supported programming languages must produce the same JSON structure and equivalent results.

## 5. Edge Cases

The implementation must correctly handle the following situations:

- **Empty File:** Return 0 requests, 0 unique visitors, 0 error requests, and 0% error rate.
- **Malformed Entry:** Skip invalid log entries without crashing.
- **Invalid IP Address:** Ignore entries containing invalid IP addresses.
- **Missing Status Code:** Skip entries without a valid HTTP status code.
- **No Errors:** Return an error rate of 0% when there are no error responses.
- **All Errors:** Return an error rate of 100% when every valid request has an error status code.
- **Duplicate Visitors:** Count repeated IP addresses only once when calculating unique visitors.
- **Boundary Status Codes:** Treat HTTP status codes 400 and 599 as errors.

## 6. Test Cases

The implementation must pass at least the following five test cases.

| Test File | Total Requests | Unique Visitors | Error Requests | Error Rate |
|---|---:|---:|---:|---:|
| `log_small.txt` | 100 | 25 | 20 | 20.00% |
| `log_empty.txt` | 0 | 0 | 0 | 0.00% |
| `log_no_errors.txt` | 10 | 3 | 0 | 0.00% |
| `log_all_errors.txt` | 5 | 2 | 5 | 100.00% |
| `log_malformed.txt` | 3 | 2 | 1 | 33.33% |

### Detailed Expected Results

**Test Case 1: log_small.txt**
- Total Requests: 100
- Unique Visitors: 25
- Error Requests: 20
- Error Rate: 20.00%

**Test Case 2: log_empty.txt**
- Total Requests: 0
- Unique Visitors: 0
- Error Requests: 0
- Error Rate: 0.00%

**Test Case 3: log_no_errors.txt**
- Total Requests: 10
- Unique Visitors: 3
- Error Requests: 0
- Error Rate: 0.00%

**Test Case 4: log_all_errors.txt**
- Total Requests: 5
- Unique Visitors: 2
- Error Requests: 5
- Error Rate: 100.00%

**Test Case 5: log_malformed.txt**
- Total Requests: 3
- Unique Visitors: 2
- Error Requests: 1
- Error Rate: 33.33%

Malformed entries must be skipped and must not affect the calculated statistics.

## 7. Cross-Language Requirements

All implementations must:

- Follow the same algorithm and validation rules.
- Produce equivalent results for identical input files.
- Use JSON as the output format.
- Maintain consistent field names and data types.
- Handle edge cases consistently.
- Include appropriate error handling.
- Calculate error rates using the same rounding rules.

## 8. Success Criteria

The project is considered successful when:

- All five test cases pass.
- All supported programming languages produce consistent results.
- Invalid entries are handled without crashing.
- The output follows the specified JSON structure.
- All edge cases are handled correctly.