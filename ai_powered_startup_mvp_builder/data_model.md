
# Data Model - Feedback Collection App

## 1. User Entity

Stores information about users who submit feedback.

| Field | Data Type | Description |
|---|---|---|
| id | Integer | Unique user identifier |
| name | String | User's full name |
| email | String | User's email address |
| created_at | DateTime | Account creation date |

## 2. Feedback Entity

Stores feedback submitted by users.

| Field | Data Type | Description |
|---|---|---|
| id | Integer | Unique feedback identifier |
| user_id | Integer | ID of the user who submitted feedback |
| title | String | Feedback title |
| description | Text | Detailed feedback message |
| category | String | Feedback category |
| status | String | Feedback status (Pending, Reviewed, Completed) |
| created_at | DateTime | Feedback submission date |

## 3. Message Entity

Stores chat messages between users and team members.

| Field | Data Type | Description |
|---|---|---|
| id | Integer | Unique message identifier |
| user_id | Integer | ID of the sender |
| content | Text | Message content |
| created_at | DateTime | Message creation date |

## 4. Relationships

- One user can submit multiple feedback entries.
- Each feedback entry belongs to one user.
- One user can send multiple chat messages.
- Each message belongs to one user.

## 5. Constraints

- Every entity has a unique ID.
- User email addresses must be unique.
- Feedback must have a title and description.
- Feedback status must be Pending, Reviewed, or Completed.
- Every feedback entry must be associated with a user.
