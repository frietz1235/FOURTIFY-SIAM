# Defect Log – FOURTIFY

## Severity Levels
| Code | Meaning |
|------|---------|
| S1 | Critical - System crash/data loss |
| S2 | High - Major feature broken |
| S3 | Medium - Minor feature broken |
| S4 | Low - Cosmetic issue |

---

## Open Defects
*No open defects at this time*

---

## Closed Defects

| Bug ID | Description | Severity | Status | Date Found | Date Closed | PR Link |
|--------|-------------|----------|--------|------------|-------------|---------|
| BUG-001 | get_completion_percentage() returns decimal (0.5) instead of percentage (50) | S3 - Medium | Closed | 2026-04-23 | 2026-04-23 | [PR #1](https://github.com/frietz1235/FOURTIFY-SIAM/pull/1) |

---

## Bug Details

### BUG-001: Incorrect completion percentage calculation

**File:** src/task_manager.py
**Function:** get_completion_percentage()

**Current (buggy) code:**
```python
return completed_count / len(self.tasks)
```

**Expected code:**
```python
return (completed_count / len(self.tasks)) * 100
```

**Root cause:** Missing multiplication by 100

**Fix PR:** [Link to PR](https://github.com/frietz1235/FOURTIFY-SIAM/pull/1)