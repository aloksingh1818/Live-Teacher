
# Day 3: System Architecture Design (with Diagram)

This document provides the system architecture for the Live-Teacher app, including a high-level diagram, component breakdown, data flow, integration points, and security notes for easy reference.

---


## High-Level Architecture Diagram

```
+-------------------+        +-------------------+        +-------------------+
|   Web Browser     | <----> |   FastAPI Server  | <----> |     Firebase      |
| (React.js Frontend)|       |   (Python API)    |        | (Firestore/Auth)  |
+-------------------+        +-------------------+        +-------------------+
        |                          |                           |
        |                          |                           |
        v                          v                           v
+-------------------+    +-------------------+        +-------------------+
| Google Cloud TTS  |    |    PyMuPDF        |        | Firebase Hosting  |
+-------------------+    +-------------------+        +-------------------+
        |                          |                           |
        v                          v                           v
+-------------------+        +-------------------+        +-------------------+
|  OpenAI GPT (AI)  |        | Firebase Cloud Msg|        |   (Notifications) |
+-------------------+        +-------------------+        +-------------------+
```

---


## Component Breakdown

### React.js Web App (Frontend)
- User authentication (signup/login/logout)
- PDF upload and viewing (page-by-page, line-by-line)
- Page navigation, TTS controls (play, pause, speed, tone), progress tracking
- Teaching/reading mode switch, UI for advanced features
- Responsive web UI, accessible from any browser

### FastAPI Server (Backend)

- Handles API requests from React.js app
- Manages PDF processing (PyMuPDF/pdfminer)
- Integrates with Google Cloud TTS or Amazon Polly for audio
- Connects to OpenAI GPT for AI features (future)
- Communicates with Firebase for user data, progress, and authentication


### Firebase
- Firestore: Stores user data, progress, notes, etc.
- Auth: Manages user authentication and sessions
- Hosting: Hosts backend/frontend if needed
- Cloud Messaging: Sends push notifications (future/optional)


### TTS Provider (Google Cloud/Amazon Polly)
- Converts extracted text to speech audio
- Returns audio files/streams to backend and then to app


### PyMuPDF/pdfminer
- Extracts text from uploaded PDFs
- Handles OCR for scanned documents


### OpenAI GPT (Future/Advanced)
- Provides explanations, Q&A, summaries, and adaptive learning

---



## Data Flow Example (MVP)
1. User signs up/logs in via React.js web app (Firebase Auth)
2. User uploads PDF via web UI
3. PDF sent to FastAPI backend
4. FastAPI uses PyMuPDF/pdfminer to extract text
5. Text sent to Google Cloud TTS or Amazon Polly for audio
6. Audio returned to app for playback
7. User progress and preferences saved in Firestore
8. (Optional/future) Notifications sent via Firebase Cloud Messaging

---


## Integration Points
- React.js <-> FastAPI: REST API (HTTPS)
- FastAPI <-> Firebase: Python SDK/REST API
- FastAPI <-> Google Cloud TTS: REST API
- FastAPI <-> PyMuPDF: Local library call
- FastAPI <-> OpenAI GPT: REST API (future)
- Firebase Cloud Messaging: Push notifications to app

---


## Security & Scalability Notes
- All API endpoints secured with authentication tokens
- Sensitive data encrypted in transit and at rest
- Use environment variables for API keys/secrets
- Design for horizontal scaling of backend and database

---


## Next Steps
- Define backend API endpoints (Day 4)
- Define frontend component structure (Day 5)
