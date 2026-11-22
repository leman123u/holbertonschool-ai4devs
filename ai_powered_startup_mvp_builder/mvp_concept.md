# MVP Concept - TaskFlow: AI-Assisted Task Manager

## Problem Statement
Students, employees and freelancers juggle tasks across notes apps, chats and paper lists.
Tasks get forgotten, deadlines slip, and people waste time deciding what to work on next.
Existing tools (Jira, Asana) are too complex for personal use, while simple to-do apps
offer no help with prioritization. TaskFlow provides a lightweight task list that
suggests what to do first.

## Target Users
- **Students** – track assignments and exam deadlines across multiple courses
- **Employees** – manage daily work items and meeting follow-ups
- **Freelancers** – organize tasks across several clients and projects

## Core Features
1. **Task CRUD** – create, edit and delete tasks with title, description, due date and priority
2. **Status tracking** – mark tasks as To Do / In Progress / Done; view progress percentage
3. **Filtering & search** – filter by status, priority or due date; keyword search
4. **AI priority suggestions** – AI ranks open tasks by deadline and importance and recommends the top 3 for today
5. **Deadline reminders** – highlight overdue and due-today tasks on the dashboard

## Constraints
- **Timeline:** MVP built in a 2-week sprint by one developer
- **No authentication:** single-user, data stored locally / in one database
- **Scale:** limited to 500 tasks per user
- **Tech stack:** React + Tailwind (frontend), FastAPI (backend), SQLite/Supabase (database)
- **AI usage:** one LLM API call per suggestion request to keep costs low
- **Platform:** responsive web app only, with no native mobile app