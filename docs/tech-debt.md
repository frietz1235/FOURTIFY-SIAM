# Technical Debt Log - FOURTIFY

## What is Technical Debt?
Technical debt refers to code that works but is suboptimal - hard to maintain, inefficient, or duplicated. This log tracks debts and prioritizes fixes.

---

## Technical Debt Items

| ID | Description | Location | Severity | Estimated Effort | Status |
|----|-------------|----------|----------|------------------|--------|
| TD-001 | Duplicate validation logic across methods | `task_manager.py` - multiple methods | Medium | 30 min | Open |
| TD-002 | Hardcoded priority levels (High/Medium/Low) - should be configurable | `task_manager.py` - Priority strings | Low | 45 min | Open |
| TD-003 | No input validation on task dates (accepts invalid dates) | `task_manager.py` - add_task() | High | 1 hour | Open |
| TD-004 | get_overdue_tasks() inefficient - loops through all tasks every time | `task_manager.py` - line ~70 | Medium | 30 min | Open |
| TD-005 | Missing type hints (Python type annotations) | Entire `task_manager.py` | Low | 20 min | Open |
| TD-006 | get_completion_percentage() called multiple times - could cache result | `task_manager.py` - line ~60 | Low | 25 min | Open |

---

## Detailed Descriptions

### TD-001: Duplicate Validation Logic
**Location:** `task_manager.py` - add_task(), mark_task_complete(), delete_task()

**Problem:** Each method checks if task exists separately. Could be extracted to a helper method.

```python
# Current (duplicated)
def mark_task_complete(self, task_id):
    task = self.get_task(task_id)
    if task:
        task.mark_complete()
        return True
    return False

# Should be refactored to use a helper
```

---

### TD-002: Hardcoded Priority Levels
**Location:** `task_manager.py` - Task.__init__(), get_tasks_by_priority()

**Problem:** Priority values are strings ("High", "Medium", "Low") hardcoded everywhere. Changes require code modification.

**Fix:** Define constants or Enum at top of file.

---

### TD-003: No Input Validation on Dates
**Location:** `task_manager.py` - add_task()

**Problem:** Accepts any string as due_date. No validation for format or future date.

**Risk:** User could enter "tomorrow" or "invalid" causing comparison errors.

**Fix:** Parse and validate date format (YYYY-MM-DD).

---

### TD-004: Inefficient Overdue Tasks Calculation
**Location:** `task_manager.py` - get_overdue_tasks()

**Problem:** Scans ALL tasks every time. For 1000+ tasks, this is slow.

**Potential Fix:** Maintain separate overdue index or use list comprehension optimization (already used, but could cache).

---

### TD-005: Missing Type Hints
**Location:** Entire `task_manager.py`

**Problem:** No type annotations makes code harder to understand and IDE support limited.

**Example Current:**
```python
def add_task(self, title, description, due_date, priority="Medium"):
```

**Should be:**
```python
def add_task(self, title: str, description: str, due_date: str, priority: str = "Medium") -> int:
```

---

### TD-006: Redundant Completion Percentage Calls
**Location:** Any method that calls get_completion_percentage() repeatedly

**Problem:** If called 10 times in a row, calculates average 10 times. Could cache result and update only when tasks change.

**Fix:** Add cached_percentage attribute, update on add/delete/mark_complete.

---

## Prioritization for Refactoring

| Priority | Debt ID | Reason |
|----------|---------|--------|
| 1 | TD-003 | Input validation prevents crashes |
| 2 | TD-001 | Improves code maintainability |
| 3 | TD-005 | Quick win, low effort |
| 4 | TD-004 | Performance improvement |
| 5 | TD-002 | Nice to have |
| 6 | TD-006 | Future optimization |

**Selected for refactoring in Phase 7:** TD-003 (Input validation on dates) + TD-001 (Duplicate validation logic) + TD-005 (Type hints)