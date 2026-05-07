# System Architecture - FOURTIFY

## Project: Student Task & Progress Manager

## Date: May 7, 2026

---

## 1. High-Level Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           USER (Student/Instructor)                        │
└─────────────────────────────────────┬───────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                              GitHub Pages                                   │
│                         (Frontend Hosting - HTTPS)                          │
│                    https://frietz1235.github.io/FOURTIFY-SIAM/              │
└─────────────────────────────────────┬───────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                            GitHub Repository                                │
│                         (Code Storage & Version Control)                    │
│                      https://github.com/frietz1235/FOURTIFY-SIAM           │
└─────────────────────────────────────┬───────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           GitHub Actions (CI/CD)                           │
│                                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │    Test     │───▶│   Build     │───▶│   Deploy    │───▶│  Smoke Test │  │
│  │ (pytest)    │    │ (Artifacts) │    │ (gh-pages)  │    │ (HTTP 200)  │  │
│  └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           Developer Workstation                            │
│                         (Google Colab / Local IDE)                          │
│                                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐                      │
│  │  Feature    │───▶│  Pull       │───▶│  Code       │                      │
│  │  Branch     │    │  Request    │    │  Review     │                      │
│  └─────────────┘    └─────────────┘    └─────────────┘                      │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Component Description

| Component | Technology | Purpose |
|-----------|------------|---------|
| Frontend | HTML/CSS/JS + GitHub Pages | User interface, documentation hosting |
| Backend Logic | Python (TaskManager class) | Business logic, task operations |
| CI/CD Pipeline | GitHub Actions | Automated testing, building, deployment |
| Version Control | Git + GitHub | Source code management, collaboration |
| Testing | pytest | Unit testing, smoke testing |
| Monitoring | GitHub Actions logs + UptimeRobot | System health, deployment status |

---

## 3. Data Flow

```
User Input → Frontend (GitHub Pages) → TaskManager (Python)
                                                      │
                                                      ▼
                                    In-memory Storage (Dict)
                                                      │
                                                      ▼
                                    JSON Export (planned) / Database (future)
```

### Step-by-Step Flow
1. User interacts with the application (CLI or future web UI)
2. TaskManager processes requests (add, delete, mark complete)
3. Data is stored in memory (Dictionary structure)
4. CI/CD pipeline automatically tests changes on push
5. Successful changes deploy to GitHub Pages
6. Monitoring checks system health continuously

---

## 4. Deployment Architecture

```
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│   GitHub Repo    │────▶│  GitHub Actions  │────▶│   GitHub Pages   │
│   (main branch)  │     │   (CI/CD)        │     │   (Production)   │
└──────────────────┘     └──────────────────┘     └──────────────────┘
         │                                              │
         │                                              │
         ▼                                              ▼
┌──────────────────┐                     ┌──────────────────┐
│  Feature Branch  │                     │   gh-pages       │
│  (development)   │                     │   Branch         │
└──────────────────┘                     └──────────────────┘
```

---

## 5. Technology Stack

| Layer | Technology | Version |
|-------|------------|---------|
| Frontend | HTML5/CSS3 | - |
| Backend | Python | 3.12 |
| CI/CD | GitHub Actions | YAML workflows |
| Testing | pytest | 8.4.2 |
| Hosting | GitHub Pages | Free tier |
| VCS | Git | 2.x |

---

## 6. Security Architecture

| Layer | Measure |
|-------|---------|
| Transport | HTTPS (GitHub Pages) |
| Authentication | Token-based (planned for web UI) |
| Input Validation | Sanitization functions |
| Dependencies | Regular pip-audit scans |
