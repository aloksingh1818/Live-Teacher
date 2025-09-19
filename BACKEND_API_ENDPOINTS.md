# Day 4: Define Backend API Endpoints (Including Authentication)

This document lists the planned REST API endpoints for the Live-Teacher backend (FastAPI), including authentication, PDF handling, TTS, and user progress. Each endpoint includes a description, method, route, request/response structure, and authentication requirements.

---

## 1. Authentication Endpoints

| Method | Route           | Description                | Auth Required | Request Body / Params         | Response                |
|--------|-----------------|---------------------------|--------------|-------------------------------|-------------------------|
| POST   | /auth/signup    | Register new user         | No           | email, password               | user info, token        |
| POST   | /auth/login     | User login                | No           | email, password               | user info, token        |
| POST   | /auth/logout    | Logout user (invalidate)  | Yes          | token                         | success/fail            |
| GET    | /auth/me        | Get current user info     | Yes          | token (header)                | user info               |

---

## 2. PDF Handling Endpoints

| Method | Route           | Description                | Auth Required | Request Body / Params         | Response                |
|--------|-----------------|---------------------------|--------------|-------------------------------|-------------------------|
| POST   | /pdf/upload     | Upload PDF for processing  | Yes          | file (PDF)                    | pdf_id, meta            |
| GET    | /pdf/{pdf_id}   | Get PDF metadata/status    | Yes          | pdf_id                        | meta, status            |
| DELETE | /pdf/{pdf_id}   | Delete uploaded PDF        | Yes          | pdf_id                        | success/fail            |

---

## 3. Text Extraction & TTS Endpoints

| Method | Route                   | Description                        | Auth Required | Request Body / Params         | Response                |
|--------|-------------------------|-------------------------------------|--------------|-------------------------------|-------------------------|
| GET    | /pdf/{pdf_id}/text      | Get extracted text (by page/line)   | Yes          | pdf_id, page/line             | text                    |
| POST   | /tts/generate           | Generate TTS audio for text         | Yes          | text, language, speed, voice  | audio file/stream       |

---

## 4. User Progress & Bookmarks

| Method | Route                   | Description                        | Auth Required | Request Body / Params         | Response                |
|--------|-------------------------|-------------------------------------|--------------|-------------------------------|-------------------------|
| POST   | /progress/save          | Save user progress                  | Yes          | pdf_id, page, line, percent   | success/fail            |
| GET    | /progress/{pdf_id}      | Get user progress for a PDF         | Yes          | pdf_id                        | progress info           |

---

## 5. (Future) AI/Advanced Features

| Method | Route                   | Description                        | Auth Required | Request Body / Params         | Response                |
|--------|-------------------------|-------------------------------------|--------------|-------------------------------|-------------------------|
| POST   | /ai/explain             | Get AI explanation for text         | Yes          | text, difficulty              | explanation             |
| POST   | /ai/quiz                | Generate quiz from content          | Yes          | pdf_id, page/chapter          | quiz questions          |
| POST   | /ai/qa                  | Ask question, get answer            | Yes          | pdf_id, question              | answer                  |

---

## Notes
- All endpoints use JWT or Firebase Auth tokens for authentication (except signup/login).
- File uploads use multipart/form-data.
- Error responses follow a standard format: `{ "error": "message" }`
- Endpoints can be expanded as features grow (see advanced/future section).

---

## Next Steps
- Define frontend component structure (Day 5)
- Set up initial backend project structure (Day 8)
- Document API contracts and data models
