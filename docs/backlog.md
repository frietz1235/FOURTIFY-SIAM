
# Product Backlog – FOURTIFY

## Project: Student Task & Progress Manager (Web App)
*Realistic for 15 weeks – includes auth, tasks, progress tracking, basic reports*

---

### Story 1 (High – 3 pts)
**As a** student,  
**I want to** create an account and log in securely,  
**so that** my tasks and progress are private.

**Acceptance Criteria:**
- User can register with email/password
- User can log in/log out
- Wrong credentials show error message
- Session persists until logout

---

### Story 2 (High – 5 pts)
**As a** student,  
**I want to** add, edit, and delete tasks,  
**so that** I can manage my coursework.

**Acceptance Criteria:**
- Add task with title, description, due date
- Edit existing task fields
- Delete task with confirmation dialog
- Tasks saved to database per user

---

### Story 3 (High – 3 pts)
**As a** student,  
**I want to** mark tasks as complete/incomplete,  
**so that** I track my real progress.

**Acceptance Criteria:**
- Checkbox to toggle task completion
- Completed tasks visually distinct (strikethrough)
- Completion status persists after refresh

---

### Story 4 (Medium – 5 pts)
**As a** student,  
**I want to** see my task completion percentage,  
**so that** I know how close I am to finishing.

**Acceptance Criteria:**
- Dashboard shows % complete
- Updates instantly when task is marked done
- Formula: (completed tasks / total tasks) × 100

---

### Story 5 (High – 8 pts)
**As a** student,  
**I want to** set priority levels for tasks (High/Med/Low),  
**so that** I focus on important work first.

**Acceptance Criteria:**
- Priority dropdown when adding/editing task
- Sort/filter tasks by priority
- High-priority tasks highlighted in red

---

### Story 6 (Medium – 5 pts)
**As a** student,  
**I want to** add due dates and see overdue tasks,  
**so that** I don’t miss deadlines.

**Acceptance Criteria:**
- Due date picker (calendar)
- Overdue tasks shown in red with warning
- Sort by due date (earliest first)

---

### Story 7 (Low – 2 pts)
**As a** student,  
**I want to** search tasks by keyword,  
**so that** I find specific tasks quickly.

**Acceptance Criteria:**
- Search bar filters task titles/descriptions
- Real-time filtering (no page reload)
- Clear search button

---

### Story 8 (Medium – 3 pts)
**As a** student,  
**I want to** see a simple bar chart of my weekly progress,  
**so that** I stay motivated.

**Acceptance Criteria:**
- Show tasks completed per day (last 7 days)
- Simple bar chart (Chart.js or similar)
- Updates when tasks change

---

### Story 9 (Low – 2 pts)
**As a** student,  
**I want to** export my task list as a text file,  
**so that** I can share or print it.

**Acceptance Criteria:**
- “Export” button downloads .txt or .csv
- Includes title, due date, status, priority
- Works in all modern browsers

---

### Story 10 (Medium – 5 pts)
**As a** student,  
**I want to** set daily/weekly task reminders,  
**so that** I don’t forget pending tasks.

**Acceptance Criteria:**
- User sets reminder time in settings
- Browser notification or email reminder
- Sends only for incomplete tasks

---

### Story 11 (Low – 3 pts)
**As a** instructor/group member,  
**I want to** see anonymized task completion trends,  
**so that** I understand team productivity.

**Acceptance Criteria:**
- Aggregate completion rate (no names)
- Show average completion time per priority
- Only visible if user is in “viewer” role

---

### Story 12 (Low – 2 pts)
**As a** student using a phone,  
**I want to** use the task manager easily on small screen,  
**so that** I work from anywhere.

**Acceptance Criteria:**
- Responsive layout (mobile-first)
- Buttons big enough to tap
- No horizontal scroll on phone
