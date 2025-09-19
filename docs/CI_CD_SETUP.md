# Day 7: Set Up CI/CD Pipeline

This document describes the initial Continuous Integration and Continuous Deployment (CI/CD) setup for the Live-Teacher project, covering both backend (FastAPI) and frontend (Flutter) workflows.

---

## 1. Goals
- Automatically lint, test, and build code on every push or pull request
- Deploy backend and frontend to staging/production environments
- Ensure code quality and fast feedback for all contributors

---

## 2. Recommended Tools
- **GitHub Actions** (free, native to GitHub, easy to configure)
- **Alternative:** GitLab CI, CircleCI, Travis CI (if needed)

---

## 3. Example GitHub Actions Workflow Files

### A. Backend: `.github/workflows/backend.yml`
```yaml
name: Backend CI
on:
  push:
    paths:
      - 'backend/**'
  pull_request:
    paths:
      - 'backend/**'
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          cd backend
          pip install -r requirements.txt
      - name: Lint
        run: |
          cd backend
          flake8 .
      - name: Run tests
        run: |
          cd backend
          pytest
```

### B. Frontend: `.github/workflows/frontend.yml`
```yaml
name: Frontend CI
on:
  push:
    paths:
      - 'frontend/**'
  pull_request:
    paths:
      - 'frontend/**'
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Flutter
        uses: subosito/flutter-action@v2
        with:
          flutter-version: '3.19.0'
      - name: Install dependencies
        run: |
          cd frontend
          flutter pub get
      - name: Analyze
        run: |
          cd frontend
          flutter analyze
      - name: Run tests
        run: |
          cd frontend
          flutter test
```

---

## 4. Deployment (Optional for MVP)
- Add deploy steps to the above workflows for Firebase Hosting (frontend) and Google Cloud Run/App Engine (backend) when ready.
- Use secrets for API keys and deploy tokens.

---

## 5. Next Steps
- Add the above workflow files to `.github/workflows/`
- Test by pushing a commit to backend or frontend folders
- Monitor Actions tab in GitHub for build/test results
- Expand workflows as project grows (e.g., deploy, notify, etc.)
