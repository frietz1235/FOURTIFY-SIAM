# Quality Assurance Plan – FOURTIFY

## Project: Student Task & Progress Manager (Web App)

---

## 1. Test Levels

### Unit Testing
- **Scope:** Individual functions (add_task, delete_task, mark_complete, calculate_progress)
- **Tools:** Pytest
- **Who:** Developers
- **When:** After each code change, before commit

### Integration Testing
- **Scope:** API endpoints, database interactions, authentication flow
- **Tools:** Pytest with fixtures
- **Who:** QA Lead (Hakima)
- **When:** After unit tests pass, before merging feature branch

### System Testing
- **Scope:** Full application flow (login → add task → mark complete → view progress)
- **Tools:** Manual testing + Selenium (optional)
- **Who:** QA Lead + team
- **When:** Before each sprint review

### Acceptance Testing
- **Scope:** User story validation against acceptance criteria
- **Tools:** Manual testing
- **Who:** Product Owner (Nomeben)
- **When:** Sprint demo day

---

## 2. Entry & Exit Criteria

### Unit Testing
| Entry | Exit |
|-------|------|
| Code written and compiles | 100% of unit tests pass |
| Test file created | Code coverage ≥ 80% |

### Integration Testing
| Entry | Exit |
|-------|------|
| Unit tests pass | All critical paths work |
| Feature branch merged to develop | No regression bugs |

### System Testing
| Entry | Exit |
|-------|------|
| Integration tests pass | All user stories meet acceptance criteria |
| Staging environment deployed | No S1/S2 bugs remain |

---

## 3. Severity Levels

| Severity | Code | Definition | Response Time |
|----------|------|------------|---------------|
| **S1 - Critical** | 🔴 | System crash, data loss, security breach | Fix within 4 hours |
| **S2 - High** | 🟠 | Major feature broken, no workaround | Fix within 24 hours |
| **S3 - Medium** | 🟡 | Minor feature broken, workaround exists | Fix within 1 week |
| **S4 - Low** | 🔵 | UI glitch, typo, cosmetic issue | Fix next sprint |

---

## 4. Test Environment

- **OS:** Ubuntu 22.04 (Colab environment)
- **Python:** 3.12+
- **Database:** SQLite (dev), PostgreSQL (prod)
- **CI/CD:** GitHub Actions (Phase 5)

---

## 5. Test Data Strategy

- Use fixtures for repeatable test data
- Each test should be independent
- Clean up test data after each run

---

## 6. Tools

| Tool | Purpose |
|------|---------|
| Pytest | Unit/integration testing |
| Pytest-cov | Code coverage reporting |
| GitHub Issues | Defect tracking |
| Manual testing | UI/UX validation |

---

## 7. Roles & Responsibilities

| Role | Name | QA Responsibility |
|------|------|-------------------|
| QA Lead | Hakima S. Abdulkarim | Write test cases, manage defect log, sign-off on releases |
| DevOps Lead | Ayyah M. Ampuan | Maintain CI pipeline, test automation |
| PM/Scrum | Nomeben Clarin | Approve exit criteria, prioritize bug fixes |
| Docs Lead | Karl Simon | Document test results, maintain QA plan |

---

## 8. Definition of Done (QA Edition)

A feature is **QA Complete** when:
- [ ] Unit tests written and passing
- [ ] Integration tests pass
- [ ] No S1 or S2 bugs open
- [ ] Code coverage ≥ 80%
- [ ] Manual testing signed off by QA Lead
