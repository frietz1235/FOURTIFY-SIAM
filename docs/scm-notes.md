# Software Configuration Management Notes - FOURTIFY

## Branching Strategy

We use Git Flow-inspired branching:
- main: Production-ready code
- feature/*: New features
- bugfix/*: Bug fixes
- hotfix/*: Critical production fixes

## Merge Conflict Simulation

### Date: 2026-04-23

### What caused the conflict?
Two branches (conflict-simulation and conflict-other) modified the same line in src/task_manager.py - the docstring of get_completion_percentage().

### Conflict Markers Seen:
<<<<<<< HEAD
    """Calculate percentage (CONFLICT BRANCH VERSION)"""
=======
    """Calculate percentage (OTHER BRANCH VERSION)"""
>>>>>>> conflict-other

### How It Was Resolved:
1. Identified the conflicting lines between <<<<<<< HEAD and >>>>>>>
2. Chose to keep the original docstring
3. Removed conflict markers
4. Staged the resolved file: git add src/task_manager.py
5. Completed merge: git commit

### Resolution Strategy:
Kept simple docstring: "Calculate percentage of completed tasks"

## Best Practices Learned
1. Always pull latest main before creating feature branches
2. Keep branches short-lived (max 2-3 days)
3. Use descriptive commit messages
4. Resolve conflicts locally before pushing
5. Always test after resolving conflicts