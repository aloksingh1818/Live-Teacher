# Live-Teacher Backend API Endpoints (MVP)

This document defines the core REST API endpoints for the Live-Teacher backend (FastAPI), including authentication, PDF upload, text extraction, TTS, and progress tracking.

---

## 1. Authentication (Firebase Auth)
- **/auth/login** (POST): User login (handled on frontend, backend validates token)
- **/auth/signup** (POST): User signup (handled on frontend, backend validates token)
- **/auth/verify** (POST): Verify Firebase ID token, return user info

## 2. PDF Upload & Management
- **/pdf/upload** (POST): Upload a PDF file
  - Request: multipart/form-data (file)
  - Response: PDF ID, metadata
- **/pdf/{pdf_id}/extract** (GET): Extract text from a PDF (after upload)
  - Request: PDF ID
  - Response: Extracted text (by page/line)

## 3. Text-to-Speech (TTS)
- **/tts/speak** (POST): Generate TTS audio for given text
  - Request: { text, language, voice, speed, pitch }
  - Response: Audio file/stream URL

## 4. Progress Tracking
- **/progress/save** (POST): Save user reading progress
  - Request: { pdf_id, page, line, percent }
  - Response: Success
- **/progress/get** (GET): Get user progress for a PDF
  - Request: { pdf_id }
  - Response: { page, line, percent }

## 5. Teaching Mode (Basic Explanation)
- **/teach/explain** (POST): Get explanation for a line/section
  - Request: { text, difficulty }
  - Response: Explanation text

---

## Notes
- All endpoints require authentication (Firebase ID token in header)
- File uploads and TTS responses may use presigned URLs or direct streaming
- Advanced endpoints (summaries, quizzes, Q&A) are out of MVP scope

---

## Example Request Flow
1. User logs in (frontend gets Firebase token)
2. User uploads PDF (/pdf/upload)
3. Backend extracts text (/pdf/{pdf_id}/extract)
4. User requests TTS for a section (/tts/speak)
5. User saves progress (/progress/save)
6. User requests explanation (/teach/explain)

---

## Next Steps
- Implement these endpoints in FastAPI
- Define data models and validation
- Integrate with Firebase and TTS providers
