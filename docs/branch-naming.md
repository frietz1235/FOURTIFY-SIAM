# Git Branch Naming Conventions - FOURTIFY

## Branch Types

| Prefix | Purpose | Example |
|--------|---------|---------|
| feature/ | New features or enhancements | feature/email-notifications |
| bugfix/ | Fixing non-critical bugs | bugfix/completion-percentage |
| hotfix/ | Critical production fixes | hotfix/login-crash |
| docs/ | Documentation only changes | docs/update-readme |
| release/ | Release preparation | release/v0.5 |

## Rules
1. Use lowercase letters
2. Use hyphens - to separate words (not underscores)
3. Keep names short but descriptive
4. Reference issue number if applicable: feature/task-priorities-issue12

## Example Workflow
```
main
  └── develop
       ├── feature/user-auth
       ├── feature/task-crud
       └── bugfix/percentage-fix
```

## Protected Branches
- main - Production-ready code only
- develop - Integration branch for features

## Pull Request Requirements
- Minimum 1 reviewer approval
- All CI checks must pass
- No merge conflicts before merge