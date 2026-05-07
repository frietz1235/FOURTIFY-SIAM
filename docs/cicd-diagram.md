# CI/CD Pipeline Diagram - FOURTIFY

## Pipeline Stages

1. **Test** - Unit tests run on push/PR
2. **Deploy** - Deploys to GitHub Pages (main branch only)
3. **Smoke Test** - Verifies deployed site works

## Pipeline Flow
```
Push to main → Test → Deploy → Smoke Test → ✅ Live
```

## Live URL
https://frietz1235.github.io/FOURTIFY-SIAM/