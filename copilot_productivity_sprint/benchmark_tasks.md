# Benchmark Tasks – Personal Budget Manager

## Task 1 – Create Income Endpoint

**Requirements**: Implement POST /api/incomes to add a new income record with validation.

**Inputs**: JSON {amount, source, date}

**Outputs**: Created income record with a unique ID.

**Acceptance Criteria**:
- Returns 201 when income is created successfully.
- Returns 400 if the amount is missing or invalid.
- Returns the created income record in the response.

## Task 2 – Create Expense Endpoint

**Requirements**: Implement POST /api/expenses to add a new expense record.

**Inputs**: JSON {amount, category, description, date}

**Outputs**: Created expense record with a unique ID.

**Acceptance Criteria**:
- Returns 201 when the expense is created successfully.
- Returns 400 if the amount is invalid or required fields are missing.
- Saves the expense with the correct category and date.

## Task 3 – Retrieve Transactions

**Requirements**: Implement GET /api/transactions to retrieve user transactions.

**Inputs**: Optional query parameters {startDate, endDate, category}

**Outputs**: A list of matching income and expense transactions.

**Acceptance Criteria**:
- Returns 200 when transactions are retrieved successfully.
- Filters transactions by date range when dates are provided.
- Returns an empty list when no transactions match the filters.

## Task 4 – Update Monthly Budget

**Requirements**: Implement PUT /api/budgets/{id} to update an existing monthly budget.

**Inputs**: JSON {category, limit, month}

**Outputs**: Updated budget information.

**Acceptance Criteria**:
- Returns 200 when the budget is updated successfully.
- Returns 400 if the budget limit is invalid.
- Returns 404 if the budget does not exist.

## Task 5 – Generate Financial Summary

**Requirements**: Implement GET /api/reports/summary to calculate the user's financial summary.

**Inputs**: Query parameters {startDate, endDate}

**Outputs**: JSON {totalIncome, totalExpenses, balance}

**Acceptance Criteria**:
- Returns 200 with the financial summary.
- Calculates balance as total income minus total expenses.
- Returns correct totals for the selected date range.