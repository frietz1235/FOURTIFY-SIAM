# Ethics Impact Assessment - FOURTIFY

## Project: Student Task & Progress Manager

## Date: May 7, 2026

---

## 1. Stakeholders

| Stakeholder | Role | Interest |
|-------------|------|----------|
| Students | Primary users | Track coursework, manage deadlines, reduce stress |
| Instructors | Secondary users | Monitor class progress, identify at-risk students |
| University Admin | Institutional | Ensure academic integrity, data compliance |
| Development Team | FOURTIFY | Build, maintain, improve the system |
| Future Employers | External | May view completed tasks as portfolio |

---

## 2. Potential Harms & Risks

### 2.1 Privacy Harms

| Risk | Severity | Likelihood | Mitigation |
|------|----------|------------|------------|
| Student task data exposed | High | Low | Encryption at rest, HTTPS only |
| Academic progress visible to unauthorized parties | High | Low | Authentication required, role-based access |
| Data retention beyond needed period | Medium | Medium | 30-day retention policy |

### 2.2 Mental Health Harms

| Risk | Severity | Likelihood | Mitigation |
|------|----------|------------|------------|
| Increased anxiety from deadline tracking | Medium | Medium | Positive notifications, no shaming for overdue tasks |
| Comparison between students | Medium | Low | No public leaderboards, anonymized only for instructors |

### 2.3 Equity & Access Harms

| Risk | Severity | Likelihood | Mitigation |
|------|----------|------------|------------|
| Students without reliable internet | High | Medium | Offline mode (planned), mobile-friendly design |
| Accessibility barriers for disabled students | High | Medium | WCAG 2.1 compliance, screen reader support |

---

## 3. Ethical Principles Applied

| Principle | Implementation |
|-----------|----------------|
| **Privacy by Design** | Minimal data collection, data anonymization |
| **Transparency** | Clear privacy notice, open source code |
| **User Control** | Users can export/delete their data |
| **Non-maleficence (Do no harm)** | No selling of data, no dark patterns |
| **Beneficence (Do good)** | Helps students organize, reduces academic stress |
| **Justice** | Free for students, no premium features |

---

## 4. Mitigation Measures

### Active Mitigations

- [x] Input validation to prevent injection attacks
- [x] Authentication required for all data access
- [x] HTTPS enforced (GitHub Pages)
- [x] No third-party tracking cookies

### Planned Mitigations

- [ ] Data export feature (Sprint 3)
- [ ] "Do not track" option
- [ ] Anonymous usage statistics (opt-in only)

---

## 5. Ethical Review Sign-off

| Role | Name | Date |
|------|------|------|
| PM/Scrum | Nomeben Clarin | May 7, 2026 |
| QA Lead | Hakima Abdulkarim | May 7, 2026 |
| DevOps Lead | Ayyah Ampuan | May 7, 2026 |
| Docs Lead | Karl Simon | May 7, 2026 |

---

## 6. Continuous Ethics Monitoring

- **Quarterly review** of ethical risks
- **User feedback channel** (GitHub Issues)
- **Incident response plan** for data breaches
