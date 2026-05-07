# Support Plan – FOURTIFY

## Project: Student Task & Progress Manager

---

## 1. Support Channels

| Channel | Purpose | Availability |
|---------|---------|--------------|
| GitHub Issues | Bug reports, feature requests | 24/7 (async) |
| Team Email | escalations@fourtify.com | Mon-Fri, 9am-5pm |
| Weekly Standup | Team sync, blocker resolution | Daily, 9pm |
| Google Meet | Emergency meetings | By appointment |

---

## 2. Issue Reporting Process

### Step 1: User Reports Issue
- User goes to GitHub Issues
- Selects "Bug Report" template
- Fills in: description, steps to reproduce, screenshots

### Step 2: Triage (Within 4 hours)
- QA Lead (Hakima) reviews issue
- Assigns severity (S1-S4)
- Labels issue (bug, enhancement, documentation)

### Step 3: Assignment
- QA Lead assigns to appropriate team member
- Developer acknowledges within 24 hours

### Step 4: Resolution
- Developer creates bugfix branch
- Implements fix
- Writes/updates tests
- Creates Pull Request

### Step 5: Verification
- QA Lead tests fix
- If passes, approves PR
- If fails, returns to developer

### Step 6: Deployment
- PR merged to main
- Deployed (within next deployment window)
- Issue closed

---

## 3. Severity Levels & Response Times

| Severity | Definition | Response Time | Resolution Time |
|----------|------------|---------------|-----------------|
| **S1 - Critical** | System crash, data loss, security breach | 1 hour | 4 hours |
| **S2 - High** | Major feature broken, no workaround | 4 hours | 24 hours |
| **S3 - Medium** | Minor feature broken, workaround exists | 24 hours | 1 week |
| **S4 - Low** | UI glitch, typo, cosmetic issue | 48 hours | Next sprint |

---

## 4. Escalation Path

| Level | Person | Contact | When |
|-------|--------|---------|------|
| Level 1 | QA Lead (Hakima) | GitHub Issue | First point of contact |
| Level 2 | PM/Scrum (Nomeben) | Team chat, email | Issue unresolved after 24h |
| Level 3 | DevOps Lead (Ayyah) | Direct message | Deployment/CI issues |
| Level 4 | Full Team | Emergency meeting | S1/Critical issues |

---

## 5. Common Issues & Solutions

| Issue | Symptom | Solution |
|-------|---------|----------|
| **Test fails locally** | "AssertionError" | Check test output, verify code changes, run `pytest -v` |
| **Git push rejected** | "non-fast-forward" | Pull latest: `git pull origin main --rebase` |
| **PR has conflicts** | "Can't automatically merge" | Resolve locally: `git merge main`, fix conflicts, push |
| **Deployment fails** | "Build error" | Check logs, verify environment variables, retry |

---

## 6. Support Rotation Schedule

| Week | Primary Support | Backup Support |
|------|----------------|----------------|
| Week 7-8 | Hakima (QA Lead) | Nomeben |
| Week 9-10 | Ayyah (DevOps) | Karl |
| Week 11-12 | Karl (Docs Lead) | Hakima |
| Week 13-14 | Nomeben (PM) | Ayyah |

---

## 7. Monitoring & Alerts

- **Uptime monitoring:** UptimeRobot (checks every 5 min)
- **Error tracking:** Manual review during standup
- **Performance monitoring:** Lighthouse scores (frontend)

---

## 8. Support Escalation Example

**Scenario:** User reports cannot add new tasks (S2 severity)

1. **0h:** User submits GitHub Issue with screenshots
2. **1h:** QA Lead triages as S2, assigns to developer
3. **4h:** Developer creates bugfix branch, writes fix
4. **8h:** PR created, QA Lead tests
5. **12h:** PR approved and merged
6. **24h:** Deployed, user notified, issue closed

---

## 9. Post-Mortem Process (For S1/S2 issues)

After major incident:
1. Document what happened (timeline, impact, root cause)
2. Identify how to prevent recurrence
3. Add regression tests
4. Update risk register
5. Share learnings with team

---

## 10. Support Contact Information

| Role | Name | GitHub Username |
|------|------|-----------------|
| PM/Scrum | Nomeben Clarin | @frietz1235 |
| QA Lead | Hakima Abdulkarim | @HakimaAbdulkarim |
| DevOps Lead | Ayyah Ampuan | @AyyahAmpuan |
| Docs Lead | Karl Simon | @KarlSimon |

**Emergency Contact:** Team chat (daily standup at 9pm)
