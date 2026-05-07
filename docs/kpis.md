# Key Performance Indicators (KPIs) - FOURTIFY

## Project: Student Task & Progress Manager

## Date: May 7, 2026

---

## KPI Definitions

### KPI 1: Deployment Frequency

| Metric | Value |
|--------|-------|
| Definition | Number of deployments to production per week |
| Target | 2-3 deployments per week |
| Current | 4 deployments in last 7 days |
| Measurement Source | GitHub Actions workflow runs |

---

### KPI 2: Lead Time for Changes

| Metric | Value |
|--------|-------|
| Definition | Time from commit to successful deployment |
| Target | Less than 10 minutes |
| Current | Average 5-7 minutes |
| Measurement Source | GitHub Actions start to finish time |

---

### KPI 3: Unit Test Pass Rate

| Metric | Value |
|--------|-------|
| Definition | Percentage of unit tests passing |
| Target | 95% or higher |
| Current | 100% (12/12 tests passing) |
| Measurement Source | pytest results in CI pipeline |

---

### KPI 4: System Availability (Uptime)

| Metric | Value |
|--------|-------|
| Definition | Percentage of time system is accessible |
| Target | 99.5% or higher |
| Current | 99.9% (GitHub Pages) |
| Measurement Source | Uptime monitoring |

---

### KPI 5: Defect Rate (Post-Deployment)

| Metric | Value |
|--------|-------|
| Definition | Number of bugs found after deployment |
| Target | Less than 2 per sprint |
| Current | 1 bug (BUG-001 - fixed) |
| Measurement Source | Defect log (docs/defect-log.md) |

---

### KPI 6: Test Coverage (Additional)

| Metric | Value |
|--------|-------|
| Definition | Percentage of code covered by tests |
| Target | 80% or higher |
| Current | Estimated 85% |
| Measurement Source | pytest-cov (planned) |

---

## KPI Summary Dashboard

| KPI | Current | Target | Status |
|-----|---------|--------|--------|
| Deployment Frequency | 4/week | 2-3/week | ✅ Exceeding |
| Lead Time for Changes | 5-7 min | <10 min | ✅ On Target |
| Unit Test Pass Rate | 100% | 95% | ✅ Exceeding |
| System Availability | 99.9% | 99.5% | ✅ On Target |
| Defect Rate | 1 bug | <2 bugs | ✅ On Target |

---

## KPI Tracking Method

| KPI | Tool | Frequency |
|-----|------|-----------|
| Deployment Frequency | GitHub Actions | Weekly |
| Lead Time | GitHub Actions | Per deployment |
| Test Pass Rate | pytest CI | Per commit |
| Availability | UptimeRobot | Daily |
| Defect Rate | GitHub Issues | Weekly review |
