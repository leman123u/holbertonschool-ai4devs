
# Data Model

## Overview

The application uses a relational database to store users, startup projects and AI-generated MVP plans.

The data model contains three main entities: User, Project and MVPPlan.

## 1. User Entity

Stores information about registered users.

| Field | Type | Description |
|---|---|---|
| id | UUID | Primary key |
| name | String | User's full name |
| email | String | Unique email address |
| password_hash | String | Encrypted password hash |
| created_at | Timestamp | Account creation date |

## 2. Project Entity

Stores startup ideas submitted by users.

| Field | Type | Description |
|---|---|---|
| id | UUID | Primary key |
| user_id | UUID | Foreign key referencing User |
| title | String | Startup project title |
| description | Text | Startup idea description |
| target_audience | Text | Intended users |
| created_at | Timestamp | Project creation date |

## 3. MVPPlan Entity

Stores AI-generated MVP plans.

| Field | Type | Description |
|---|---|---|
| id | UUID | Primary key |
| project_id | UUID | Foreign key referencing Project |
| core_features | JSON | List of essential features |
| user_stories | Text | Generated user stories |
| architecture | Text | System architecture description |
| status | String | Current plan status |
| created_at | Timestamp | Plan generation date |

## Entity Relationships

- One User can have many Projects.
- Each Project belongs to one User.
- One Project can have many MVPPlans.
- Each MVPPlan belongs to one Project.

## Database Relationships Diagram

```text
+------------------+
|       User       |
+------------------+
| id (PK)          |
| name             |
| email            |
| password_hash    |
| created_at       |
+------------------+
         |
         | 1
         |
         | *
+------------------+
|     Project      |
+------------------+
| id (PK)          |
| user_id (FK)     |
| title            |
| description      |
| target_audience  |
| created_at       |
+------------------+
         |
         | 1
         |
         | *
+------------------+
|     MVPPlan      |
+------------------+
| id (PK)          |
| project_id (FK)  |
| core_features    |
| user_stories     |
| architecture     |
| status           |
| created_at       |
+------------------+
```
