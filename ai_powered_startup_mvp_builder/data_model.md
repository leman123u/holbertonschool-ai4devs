
# Data Model

## Overview

The Feedback Collection App uses a simple data model to store feedback submissions and support CSV exports.

The data model contains three entities: Feedback, FeedbackForm and CSVExport.

## 1. Feedback Entity

Stores feedback submitted by users.

| Field | Type | Description |
|---|---|---|
| id | Integer | Primary key |
| form_id | Integer | Foreign key referencing FeedbackForm |
| message | Text | Feedback content |
| created_at | Timestamp | Submission date and time |

## 2. FeedbackForm Entity

Represents the feedback submission form.

| Field | Type | Description |
|---|---|---|
| id | Integer | Primary key |
| title | String | Form title |
| description | Text | Form description |
| created_at | Timestamp | Form creation date |

## 3. CSVExport Entity

Stores information about CSV export operations.

| Field | Type | Description |
|---|---|---|
| id | Integer | Primary key |
| file_name | String | Exported CSV file name |
| exported_at | Timestamp | Export date and time |
| record_count | Integer | Number of exported feedback entries |

## Entity Relationships

- One FeedbackForm can have many Feedback entries.
- Each Feedback entry belongs to one FeedbackForm.
- CSVExport records store information about exported feedback data.
- The application supports a maximum of 100 feedback entries.

## Database Relationships Diagram

```text
+----------------------+
|     FeedbackForm     |
+----------------------+
| id (PK)              |
| title                |
| description          |
| created_at           |
+----------------------+
           |
           | 1
           |
           | *
+----------------------+
|       Feedback       |
+----------------------+
| id (PK)              |
| form_id (FK)         |
| message              |
| created_at           |
+----------------------+

+----------------------+
|      CSVExport       |
+----------------------+
| id (PK)              |
| file_name            |
| exported_at          |
| record_count         |
+----------------------+
```

## Constraints

- Each feedback entry must have a unique ID.
- Feedback must be associated with a feedback form.
- A maximum of 100 feedback entries can be stored.
- CSV exports must contain the collected feedback data.
