# Deployment Plan - FOURTIFY

## Project: Student Task & Progress Manager

---

## 1. Target Environment

| Component | Technology | Platform |
|-----------|------------|----------|
| Backend API | Python + Flask (to be added) | PythonAnywhere (free tier) |
| Frontend | HTML/CSS/JS | GitHub Pages |
| Database | SQLite / PostgreSQL | PythonAnywhere |
| Version Control | Git | GitHub |

---

## 2. Deployment Strategy

**Chosen Strategy:** Blue-Green Deployment (simplified for student project)

- **Blue environment:** Current production (live)
- **Green environment:** Staging for testing
- **Switch:** Update DNS or redeploy after testing

**Why this strategy:**
- Zero downtime during deployment
- Easy rollback by switching back to Blue
- Affordable for student project

---

## 3. Deployment Steps

### Pre-deployment Checklist
- [ ] All unit tests pass (7/7)
- [ ] CI workflow passes (if implemented)
- [ ] Code reviewed and merged to main
- [ ] Version tagged (e.g., v0.5-scm)

### Deployment Process

#### Step 1: Build
```bash
git checkout main
git pull origin main
python -m pytest tests/ -v
```

#### Step 2: Deploy to Staging (Green)
- Push code to staging branch
- Deploy to PythonAnywhere staging instance
- Run smoke tests (login, add task, mark complete)

#### Step 3: Smoke Testing
- [ ] Can user register/login?
- [ ] Can user add a task?
- [ ] Can user mark task complete?
- [ ] Does completion percentage calculate correctly?
- [ ] Can user delete a task?

#### Step 4: Deploy to Production
- Promote staging to production
- Update environment variables
- Verify production URL works

#### Step 5: Post-deployment
- Monitor logs for errors (first 30 minutes)
- Notify team of successful deployment

---

## 4. Rollback Steps

**When to rollback:**
- Critical bug found (S1 severity)
- Test suite fails after deployment
- User reports major feature broken

**Rollback Procedure:**

| Step | Action | Command/Action |
|------|--------|----------------|
| 1 | Identify previous working version | `git tag -l` (find last stable tag) |
| 2 | Revert to previous tag | `git checkout v0.4-stable` |
| 3 | Redeploy previous version | Repeat deployment steps with old code |
| 4 | Verify rollback works | Run smoke tests |
| 5 | Notify team | Post in team chat |

**Emergency rollback (if automated fails):**
```bash
# Manual rollback to previous tag
git checkout v0.4-stable
git push origin main --force
```

---

## 5. Environment Variables

| Variable | Purpose | Example |
|----------|---------|---------|
| `SECRET_KEY` | Session encryption | `your-secret-key` |
| `DATABASE_URL` | Database connection | `sqlite:///tasks.db` |
| `ENVIRONMENT` | dev/staging/prod | `production` |

---

## 6. Deployment Timeline

| Phase | Duration | Owner |
|-------|----------|-------|
| Build & Test | 10 min | Nomeben |
| Deploy to Staging | 15 min | Ayyah |
| Smoke Testing | 10 min | Hakima |
| Deploy to Production | 10 min | Ayyah |
| Post-deployment Check | 15 min | Everyone |
| **Total** | **~60 minutes** | |

---

## 7. Deployment Tools

- **Version Control:** GitHub
- **CI/CD:** GitHub Actions (Phase 5)
- **Hosting:** PythonAnywhere (backend) + GitHub Pages (frontend/docs)
- **Monitoring:** UptimeRobot (free tier)

---

## 8. Current Deployment Status (Week 7)

| Component | Status | URL |
|-----------|--------|-----|
| Documentation | Deployed | https://frietz1235.github.io/FOURTIFY-SIAM/ |
| Backend API | In Progress | (to be added Sprint 3) |
| Frontend App | Planned | (to be added Sprint 4) |