
# Sprint 1 Plan – FOURTIFY

**Sprint Goal:**  
Build the core user authentication + task CRUD + basic completion tracking.

**Duration:** 2 weeks (Week 1–2 of project)

---

## Selected Stories (6 stories – 23 story points)

| Story ID | Description | Story Pts | Owner |
|----------|-------------|-----------|-------|
| Story 1 | Create account & log in securely | 3 | Nomeben (PM/Scrum) |
| Story 2 | Add, edit, delete tasks | 5 | Hakima |
| Story 3 | Mark tasks as complete/incomplete | 3 | Ayyah |
| Story 4 | See task completion percentage | 5 | Karl |
| Story 5 | Set priority levels (H/M/L) | 8 | Nomeben + Ayyah |
| Story 6 | Due dates + overdue warning | 5 | Hakima |

**Total story points:** 29 (adjusted after refinement)

---

## Sprint Backlog (Tasks broken down)

### Story 1 (Nomeben)
- Set up Firebase or Django auth
- Create register/login UI
- Store session in localStorage or cookies
- Write logout logic

### Story 2 (Hakima)
- Design task model (title, desc, due date, priority, status)
- Build “Add task” form + backend save
- Edit task (populate form, update DB)
- Delete task with confirmation

### Story 3 (Ayyah)
- Add checkbox next to each task
- Toggle status in database
- Update UI instantly (no refresh)
- Style completed tasks (strikethrough)

### Story 4 (Karl)
- Calculate % = completed/total
- Display on dashboard
- Subscribe to task changes (reactive update)
- Handle division by zero (0 tasks = 0%)

### Story 5 (Nomeben + Ayyah)
- Add priority dropdown (H/M/L) to add/edit form
- Save priority to DB
- Color-code tasks: red=High, yellow=Med, green=Low
- Sort tasks by priority (High first)

### Story 6 (Hakima)
- Add date picker to add/edit form
- Compare due date vs today
- Show “Overdue!” in red if past due
- Sort by due date (earliest first)

---

## Definition of Done (DoD)
- Code committed to GitHub/Colab repo
- Peer-reviewed by at least one team member
- No console errors or crashes
- Acceptance criteria met
- Added to `docs/change-log.md` (from Phase 5)

---

## Sprint 1 Meeting Dates
- **Sprint Planning:** Day 1  
- **Daily Standups:** Every day at 9 PM (online)  
- **Sprint Review + Retro:** End of Week 2
