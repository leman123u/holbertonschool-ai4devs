# User Stories - TaskFlow: AI-Assisted Task Manager

These stories cover the five core features in `mvp_concept.md` for the target users
(students, employees and freelancers). The MVP is single-user with no authentication.

Priority scale (MoSCoW): **Must** = required for the MVP, **Should** = important, **Could** = nice to have.

## Feature 1: Task CRUD

## User Story 1 - Create a task (Must)
As a user, I want to create a task with a title, description, due date and priority so that I can capture everything I need to do in one place.

**Acceptance Criteria:**
- The title is required and the other fields are optional.
- Priority can be Low, Medium or High (default: Medium).
- The new task appears in the task list immediately after saving.
- An error message is shown if the title is empty.

## User Story 2 - Edit a task (Must)
As a user, I want to edit an existing task so that I can update its details when plans change.

**Acceptance Criteria:**
- All task fields can be changed.
- Changes are saved and visible in the list without reloading the page.
- The same validation rules as task creation apply.

## User Story 3 - Delete a task (Must)
As a user, I want to delete a task so that I can remove activities that are no longer relevant.

**Acceptance Criteria:**
- A confirmation prompt is shown before deleting.
- A deleted task is removed from the list and from the database.

## Feature 2: Status tracking

## User Story 4 - Update task status (Must)
As a user, I want to mark a task as To Do, In Progress or Done so that I can track where each task stands.

**Acceptance Criteria:**
- New tasks start as To Do.
- The status can be changed in one click from the list.
- Done tasks are visually distinct (for example, struck through).

## User Story 5 - View progress (Should)
As a user, I want to see my progress as a percentage so that I know how much work I have completed.

**Acceptance Criteria:**
- Progress = Done tasks / total tasks, shown as a percentage on the dashboard.
- The value updates immediately when a task status changes.
- With zero tasks, progress shows 0% (no error).

## Feature 3: Filtering and search

## User Story 6 - Filter tasks (Must)
As a user, I want to filter tasks by status, priority or due date so that I can focus on what matters now.

**Acceptance Criteria:**
- Filters can be combined (for example, status = To Do and priority = High).
- A "clear filters" action restores the full list.
- An empty-state message is shown when no tasks match.

## User Story 7 - Search tasks (Should)
As a user, I want to search tasks by keyword so that I can quickly find a specific task.

**Acceptance Criteria:**
- The search matches the title and description, case-insensitively.
- Results update as I type.

## Feature 4: AI priority suggestions

## User Story 8 - Get AI priority suggestions (Must)
As a user, I want the AI to rank my open tasks and recommend the top 3 for today so that I do not waste time deciding what to work on first.

**Acceptance Criteria:**
- Only tasks that are not Done are considered.
- Ranking is based on deadline and importance (priority).
- The result shows exactly 3 tasks (or fewer if fewer open tasks exist), each with a short reason.
- One LLM API call is made per suggestion request.
- A loading indicator is shown during the request, and a clear error message if the AI service fails.
- The task list keeps working if the AI service is unavailable.

## Feature 5: Deadline reminders

## User Story 9 - See overdue and due-today tasks (Must)
As a user, I want overdue and due-today tasks highlighted on the dashboard so that I never miss a deadline.

**Acceptance Criteria:**
- Overdue tasks (due date in the past, not Done) are shown in red.
- Tasks due today are shown in orange.
- Done tasks are never highlighted.

## Dashboard and organization

## User Story 10 - Dashboard overview (Should)
As a user, I want to see all my tasks, progress and highlighted deadlines on one dashboard so that I can manage my activities easily.

**Acceptance Criteria:**
- The dashboard shows the task list, progress percentage, AI top 3 and deadline highlights.
- The layout is responsive and works on phone and desktop screens.

## User Story 11 - Organize tasks into projects (Could)
As a freelancer, I want to group tasks by project or client so that I can keep work for different clients separate.

**Acceptance Criteria:**
- A task can optionally belong to one project.
- Tasks can be filtered by project.

## Constraints Reflected in the Stories
- No sign-up or login: one user, data stored in a single database.
- A maximum of 500 tasks is allowed; a clear message is shown when the limit is reached.
- Responsive web app only, with no native mobile app.
