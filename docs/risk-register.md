# Risk Register – FOURTIFY

| Risk | Likelihood (1-5) | Impact (1-5) | Score (L * I) | Mitigation | Owner |
|------|-----------------|--------------|---------------|------------|-------|
| Team member unavailable due to illness | 4 | 4 | 16 | Cross-train members; document all code; weekly backups | Nomeben |
| GitHub merge conflicts | 3 | 3 | 9 | Daily pulls; feature branches; code reviews before merge | Ayyah |
| Authentication API failure (Firebase down) | 2 | 5 | 10 | Implement fallback local auth; monitor status page | Hakima |
| Browser compatibility issues | 3 | 3 | 9 | Test on Chrome, Firefox, Edge; use responsive design | Karl |
| Scope creep (too many features) | 4 | 4 | 16 | Strict backlog prioritization; weekly scope review | Nomeben |
| Late deployment due to environment issues | 3 | 4 | 12 | CI/CD pipeline from Week 9; staging environment | Ayyah |
| Data loss (user tasks) | 2 | 5 | 10 | Automatic backups; database snapshots daily | Hakima |
| Poor test coverage leading to bugs | 4 | 3 | 12 | Minimum 80% coverage; peer review tests | Karl |
| Mobile responsiveness fails | 3 | 3 | 9 | Mobile-first design; test on multiple devices | Ayyah |
| Missed sprint deadline | 4 | 4 | 16 | Realistic story points; daily standups; buffer tasks | Nomeben |

**Risk Score Key:**
- 1-5: Low
- 6-12: Medium
- 13-16: High
- 20-25: Critical
| Email delivery failure (SMTP/API) | 3 | 3 | 9 | Use reliable email service (SendGrid); retry logic; log failures | Hakima |

print("✅ Risk register updated")

| Token theft / session hijacking | 3 | 5 | 15 | HTTP-only cookies, short expiry (1 hour), HTTPS only | Nomeben |
| Input injection (XSS/SQL) | 4 | 4 | 16 | Input sanitization, parameterized queries, output encoding | Hakima |
| Dependency vulnerability (supply chain) | 3 | 4 | 12 | Weekly pip-audit scans, automated dependency updates | Ayyah |
