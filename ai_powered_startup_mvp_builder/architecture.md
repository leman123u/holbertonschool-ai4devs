
# System Architecture

## Overview

The Feedback Collection App is a simple web application that allows users to submit feedback and enables product teams to review, search and export collected feedback.

## High-Level System Diagram

```text
+----------------------+
|        User          |
+----------------------+
           |
           v
+----------------------+
|     Feedback Form    |
|     (Frontend UI)    |
+----------------------+
           |
           v
+----------------------+
|      Backend API     |
|   Input Validation   |
+----------------------+
           |
           v
+----------------------+
|      Database        |
|  Maximum 100 Entries |
+----------------------+
           |
           v
+----------------------+
|   Feedback Dashboard |
|  View and Search     |
+----------------------+
           |
           v
+----------------------+
|     CSV Export       |
+----------------------+
```

## Main Components

### 1. Frontend
Provides a simple interface for submitting feedback and viewing the feedback dashboard.

### 2. Backend API
Receives feedback submissions, validates input and handles requests from the dashboard.

### 3. Database
Stores feedback entries. The MVP supports a maximum of 100 feedback records.

### 4. Feedback Dashboard
Displays submitted feedback and allows product managers to search for specific entries.

### 5. CSV Export
Allows product managers to download collected feedback in CSV format.

## Data Flow

1. A user opens the feedback form.
2. The user submits feedback.
3. The frontend sends the feedback to the backend API.
4. The backend validates the submitted information.
5. The feedback is stored in the database if the 100-entry limit has not been reached.
6. Product managers view and search feedback through the dashboard.
7. Feedback can be exported as a CSV file.

## Constraints

- No user authentication is required.
- The database is limited to 100 feedback entries.
- The interface must remain simple and user-friendly.
- Only essential feedback collection features are included.
- Advanced analytics and complex reporting are excluded.
