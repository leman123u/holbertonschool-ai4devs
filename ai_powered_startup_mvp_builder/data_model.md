
# Data Model - AI-Powered Personal Knowledge Organizer

## 1. User Entity

Stores information about application users.

| Field | Data Type | Description |
|---|---|---|
| id | Integer | Unique user identifier |
| name | String | User's full name |
| email | String | User's email address |
| created_at | DateTime | Account creation date |

## 2. Note Entity

Stores personal notes created by users.

| Field | Data Type | Description |
|---|---|---|
| id | Integer | Unique note identifier |
| user_id | Integer | ID of the note owner |
| title | String | Note title |
| content | Text | Note content |
| summary | Text | AI-generated summary |
| is_favorite | Boolean | Favorite status |
| created_at | DateTime | Note creation date |
| updated_at | DateTime | Last update date |

## 3. Tag Entity

Stores tags used to organize notes.

| Field | Data Type | Description |
|---|---|---|
| id | Integer | Unique tag identifier |
| name | String | Tag name |
| created_at | DateTime | Tag creation date |

## 4. NoteTag Entity

Connects notes with tags.

| Field | Data Type | Description |
|---|---|---|
| id | Integer | Unique relationship identifier |
| note_id | Integer | Related note ID |
| tag_id | Integer | Related tag ID |

## 5. Relationships

- One user can create multiple notes.
- Each note belongs to one user.
- One note can have multiple tags.
- One tag can be assigned to multiple notes.
- NoteTag connects notes and tags through a many-to-many relationship.

## 6. Constraints

- Every entity has a unique ID.
- User email addresses must be unique.
- Every note must have a title and content.
- Every note must belong to a user.
- Tag names should not be empty.
- Each note-tag relationship must reference an existing note and tag.
- Favorite status is stored as a Boolean value.
