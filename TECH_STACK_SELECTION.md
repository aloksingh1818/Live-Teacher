# Day 2: Tech Stack Research and Selection

This document summarizes the research and selection process for the technology stack for the Live-Teacher MVP and future expansion.

---

## 1. Frontend
- **Framework:** React.js (web application)
- **Rationale:** Modern, component-based, large ecosystem, ideal for responsive web apps, fast development, strong community

## 2. Backend
- **Framework:** Python (FastAPI)
- **Rationale:** Modern, async, easy to use, great for REST APIs, integrates well with AI/ML

## 3. Database, Auth, Hosting, Notifications
- **Service:** Firebase (Firestore for database, Auth for authentication, Hosting for backend/frontend, Cloud Messaging for notifications)
- **Rationale:** No server management, real-time sync, easy integration with Flutter, built-in authentication, hosting, and notifications

## 4. PDF Handling
- **Library:** PyMuPDF (fitz)
- **Rationale:** Simple API, robust for text extraction, good documentation, works well for MVP

## 5. Text-to-Speech (TTS)
- **Service:** Google Cloud TTS
- **Rationale:** High-quality voices, easy API, supports multiple languages

## 6. AI/NLP (Future/Advanced)
- **Service:** OpenAI GPT API (for future AI features)
- **Rationale:** Best-in-class for explanations, Q&A, summaries. Use for advanced features after MVP.



---

## Summary Table
| Component         | Selected Tech           | Reasoning/Notes                       |
|-------------------|------------------------|---------------------------------------|
| Frontend          | React.js                | Modern web app, fast dev, responsive  |
| Backend           | FastAPI (Python)       | Async, modern, AI/ML friendly         |
| Database/Auth     | Firebase Firestore/Auth| Real-time, easy, scalable, secure     |
| Hosting           | Firebase Hosting       | Easy deploy, integrates with Firebase |
| Notifications     | Firebase Cloud Msg     | Native, easy                          |
| PDF Handling      | PyMuPDF                | Robust, simple API                    |
| TTS               | Google Cloud TTS       | High-quality, multi-language          |
| AI/NLP            | OpenAI GPT (future)    | Best for explanations, Q&A            |

---

## Next Steps
- Document architecture and integration points
- Begin system architecture design (Day 3)
- Set up initial project structure and repos
- Scaffold React.js frontend project structure
