# Security Checklist - FOURTIFY

## Project: Student Task & Progress Manager

---

## 1. Input Validation

| Check | Status | Location |
|-------|--------|----------|
| Sanitize user inputs | ✅ Implemented | `_sanitize_input()` |
| Validate title length (3-100 chars) | ✅ Implemented | `add_task_secure()` |
| Validate description length (max 500) | ✅ Implemented | `add_task_secure()` |
| Validate date format (YYYY-MM-DD) | ✅ Implemented | `_validate_date()` |
| Validate priority values | ✅ Implemented | `_validate_priority()` |
| Validate task ID is positive integer | ✅ Implemented | `_validate_task_id()` |

---

## 2. Authentication & Authorization

| Check | Status | Location |
|-------|--------|----------|
| Password hashing (SHA-256) | ✅ Implemented | `auth.py` |
| Token-based authentication | ✅ Implemented | `authenticate()` |
| Token expiry (1 hour) | ✅ Implemented | `_token_expiry_seconds` |
| Secure token generation | ✅ Implemented | `secrets.token_urlsafe()` |
| Token verification | ✅ Implemented | `verify_token()` |
| Token revocation (logout) | ✅ Implemented | `revoke_token()` |

---

## 3. Sensitive Data Protection

| Check | Status | Location |
|-------|--------|----------|
| No hardcoded secrets | ✅ Implemented | `.env.example` |
| .env in .gitignore | ✅ Implemented | `.gitignore` |
| Environment variables template | ✅ Implemented | `.env.example` |
| Password hashing (not plaintext) | ✅ Implemented | `_hash_password()` |

---

## 4. Dependency Security

| Check | Status | Tool |
|-------|--------|------|
| Dependency vulnerability scan | ✅ Implemented | pip-audit |
| Regular updates | 🔄 Planned | Weekly |
| Pin dependency versions | 📋 Recommended | requirements.txt |

---

## 5. Security Headers (for web deployment)

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS enforced | ✅ Enabled | GitHub Pages |
| Content Security Policy | ⚠️ Not yet | Add via meta tags |

---

## 6. Logging & Monitoring

| Check | Status |
|-------|--------|
| Authentication attempts | 📋 Planned |
| Failed login tracking | 📋 Planned |
| Security event logging | 📋 Planned |

---

## 7. Least Privilege Principle

| Check | Status |
|-------|--------|
| CI/CD token limited scope | ✅ workflow + repo |
| Read-only access for docs | ✅ GitHub Pages |

---

## 8. Security Risks Added to Risk Register

See `docs/risk-register.md` for newly added security risks:

| Risk | Severity | Mitigation |
|------|----------|------------|
| Unauthorized access via token theft | High | Token expiry + HTTPS |
| Input injection attacks | Medium | Input sanitization |
| Dependency vulnerabilities | Medium | Weekly audit scans |

---

## Last Updated: May 7, 2026
**Reviewed by:** Nomeben Clarin (PM/Scrum)
