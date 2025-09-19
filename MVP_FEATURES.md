
# Live-Teacher MVP, Advanced, and Upcoming Features Checklist

This document lists all must-have features for the Minimum Viable Product (MVP), as well as advanced and upcoming features for the Live-Teacher app. Each feature includes a description, acceptance criteria, and notes for clarity.

---

## 🟢 MVP Feature List (Core Foundation)

| Feature                        | Description                                                      | Acceptance Criteria                                      | Notes                |
|------------------------------- |------------------------------------------------------------------|----------------------------------------------------------|----------------------|
| **User Signup & Login**        | Secure account creation and login for users                      | Users can sign up, log in, log out; sessions managed     | Firebase Auth        |
| **PDF Upload**                 | User can upload book/notes PDF                                   | Uploads PDF successfully; supports common formats        | Local upload only    |
| **PDF Text Extraction**        | Extract text from uploaded PDF (with OCR if scanned)             | Extracts text from all pages; handles scanned PDFs       | Use PyMuPDF/pdfminer |
| **Page-by-Page Reading**       | Read PDF line by line, page by page                              | User can navigate pages; text displayed clearly          |                      |
| **Text-to-Speech (TTS)**       | Natural voice reading in English, Hindi, Hinglish                | TTS reads selected text/page; user can play/pause        | Google/Amazon Polly  |
| **Adjustable Speed & Tone**    | User can adjust TTS speed and tone                               | Speed/tone controls work and update TTS in real time     |                      |
| **Teaching Mode**              | Reads each line and explains in detail (simple/medium/advanced)  | User selects difficulty; receives detailed explanations  | Basic explanations   |
| **Reading Mode**               | Plain audiobook-style reading (no explanations)                  | User can switch to reading mode; no explanations given   |                      |
| **Pause & Resume**             | User can pause and resume reading at any time                    | App resumes from same page/line after pause              |                      |
| **Progress Tracking**          | Save last page and position; show % completion                   | Progress saved and restored; % completion displayed      |                      |

---

## 🔵 Advanced Features (Post-MVP)

| Feature                        | Description                                                      | Acceptance Criteria                                      | Notes                |
|------------------------------- |------------------------------------------------------------------|----------------------------------------------------------|----------------------|
| **Summary Mode**               | Gives chapter/page summaries, highlights key terms               | Summaries generated for each chapter/page                |                      |
| **Quiz Mode**                  | Auto-generates MCQs, True/False, Short Qs from content           | Quizzes generated and scored; instant feedback           |                      |
| **Doubt Mode (Q&A)**           | Student asks questions anytime (text/voice), AI answers          | AI answers in context of book                            |                      |
| **Translation Mode**           | Reads in one language, shows translation (Eng ↔ Hindi)           | Accurate translation and TTS in both languages           |                      |
| **Search & Navigation**        | Jump to chapter, keyword, or page                                | User can search and jump instantly                       |                      |
| **Note-Taking & Highlighting** | Students can highlight lines, add notes linked to text           | Notes and highlights saved and retrievable               |                      |
| **Offline Mode**               | Download book + explanations for offline study                   | App works without internet for downloaded content        |                      |

---

## 🟣 Future/Upcoming Features (Cutting-Edge)

| Feature                        | Description                                                      | Acceptance Criteria                                      | Notes                |
|------------------------------- |------------------------------------------------------------------|----------------------------------------------------------|----------------------|
| **Interactive Whiteboard**     | AI draws diagrams, charts, or mind maps while explaining         | Diagrams generated and shown during explanations         |                      |
| **Adaptive Learning**          | AI adjusts explanations to student level                         | Explanations adapt to user performance                   |                      |
| **Multiple Teaching Styles**   | Strict, friendly, exam-prep teacher tones                       | User can select style; TTS/AI adapts tone                |                      |
| **Concept Linking**            | AI connects current line with previous chapters/examples         | Links shown in explanations                              |                      |
| **Student Reports**            | Weekly learning progress, weak/strong areas                     | Reports generated and accessible                         |                      |
| **Voice Commands**             | Control app by voice ("Next page", etc.)                        | Voice commands recognized and executed                   |                      |
| **Parent/Teacher Dashboard**   | Parents/teachers can see student progress                       | Dashboard accessible with relevant data                  |                      |
| **AI Tutor Avatar**            | 3D/animated teacher face/avatar on screen                       | Avatar appears and interacts with user                   |                      |
| **Gamified Learning**          | Points, badges, streaks, leaderboards                           | Gamification elements visible and functional             |                      |
| **Multi-Student Classroom**    | AI teaches multiple students live, takes quizzes                | Group sessions supported                                 |                      |
| **Handwriting Recognition**    | Upload handwritten notes, AI reads/explains                     | Handwriting recognized and explained                     |                      |
| **AR/VR Teaching**             | AR/VR mode for immersive learning                               | AR/VR features functional                                |                      |
| **Personal Mentor Mode**       | AI adapts to learning style, remembers progress                  | Personalized suggestions and tracking                    |                      |
| **Exam Prep Mode**             | Past-year question analysis, mock tests, predictions             | Exam prep features available                             |                      |
| **Voice Emotion AI**           | Teacher’s voice changes with context                            | Voice tone adapts to content                             |                      |

---

## Assumptions & Constraints
- MVP is mobile-first (Flutter), backend in Python (FastAPI)
- Only local PDF upload and storage for MVP
- TTS uses third-party APIs (Google/Amazon)
- OCR for scanned PDFs is basic, not advanced handwriting
- Authentication uses Firebase Auth (or similar)

---

## Next Steps
- Review and confirm this checklist with stakeholders
- Create user stories and tasks for each feature
- Begin technical design and implementation
