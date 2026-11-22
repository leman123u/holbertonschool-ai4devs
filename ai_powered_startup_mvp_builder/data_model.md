
# Data Model - Task Management App

## Entity 1: Project

| Field | Type |
|---|---|
| id | Integer |
| name | String |
| description | Text |
| created_at | DateTime |

## Entity 2: Category

| Field | Type |
|---|---|
| id | Integer |
| name | String |
| color | String |

## Entity 3: Task

| Field | Type |
|---|---|
| id | Integer |
| title | String |
| description | Text |
| status | String |
| priority | String |
| deadline | DateTime |
| project_id | Integer |
| category_id | Integer |

## Relationships

- One Project can have many Tasks.
- One Category can have many Tasks.
- Each Task belongs to one Project.
- Each Task belongs to one Category.
