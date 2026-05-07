# Demo Script - FOURTIFY Capstone Presentation

## Duration: 5-7 minutes

---

## Slide 1: Problem (1 minute)

**What we say:**
"Students struggle to track coursework, deadlines, and progress across multiple classes. Existing solutions are either too complex, expensive, or don't provide progress analytics."

**Key pain points:**
- Missed deadlines
- No visibility into progress
- Stress from disorganization

---

## Slide 2: Solution - FOURTIFY (1 minute)

**What we say:**
"FOURTIFY is a student task and progress manager that helps students track tasks, deadlines, and completion progress."

**Features:**
- Add/edit/delete tasks
- Mark tasks complete/incomplete
- View completion percentage
- Priority levels (High/Medium/Low)
- Due dates with overdue warnings

**Demo URL:** https://frietz1235.github.io/FOURTIFY-SIAM/

---

## Slide 3: CI/CD Pipeline (1.5 minutes)

**What we say:**
"Our CI/CD pipeline automates testing and deployment using GitHub Actions."

**Pipeline stages:**
```
Push → Unit Tests (12 tests) → Build → Deploy → Smoke Tests → Live
```

**Metrics:**
- Pipeline time: 30-45 seconds
- Deployment frequency: 4x/week
- Test pass rate: 100%

**Demo:** Show Actions tab with green checks

---

## Slide 4: Deployment Architecture (1 minute)

**What we say:**
"We use GitHub Pages for hosting, GitHub Actions for CI/CD, and pytest for testing."

**Architecture diagram:**
```
GitHub Repo → GitHub Actions → GitHub Pages → User
     ↑              ↓              ↓
  Developer      Tests         Smoke Tests
```

**Live demo:** https://frietz1235.github.io/FOURTIFY-SIAM/

---

## Slide 5: Metrics & KPIs (1 minute)

**What we say:**
"We tracked key metrics throughout the project."

| KPI | Current | Target |
|-----|---------|--------|
| Deployment Frequency | 4/week | 2-3/week |
| Lead Time | 5-7 min | <10 min |
| Test Pass Rate | 100% | 95% |
| Availability | 99.9% | 99.5% |

**Cost-Benefit:**
- Development: $21,750
- Annual ops: $3,362
- Annual benefits: $49,000
- ROI: 95% (1-year), 362% (3-year)

---

## Slide 6: Lessons Learned (1 minute)

**What we say:**
"We encountered and overcame several challenges."

| Challenge | Solution |
|-----------|----------|
| GitHub Actions permissions | Added workflow scope |
| Deploy action failing (exit 128) | Used native git commands |
| Smoke test failures | Adjusted content checks |
| Test dependencies missing | Added explicit pip install |

**Key takeaways:**
- CI/CD automation saves time
- Smoke tests catch deployment issues
- Documentation is critical
- DevOps practices improve quality

---

## Slide 7: Q&A (30 seconds)

**Be prepared to answer:**
- Why did you choose GitHub Actions?
- How would you scale this?
- What would you add next?
- How did you handle security?
