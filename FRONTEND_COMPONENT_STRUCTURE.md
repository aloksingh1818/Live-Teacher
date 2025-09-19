# Day 5: Frontend Component Structure (Including Signup/Login Screens)


This document outlines the planned component structure for the Live-Teacher web app (React.js), including all major pages, components, and navigation flows for MVP, advanced, and future features. The structure is designed for a modern, responsive web application with clear separation of concerns and easy extensibility.

---

## 1. App Navigation Overview
- SplashPage
- AuthFlow (Signup, Login, Forgot Password)
- MainApp (after login)
  - HomePage
  - PDFUploadPage
  - PDFReaderPage
  - TTSControls (overlay/modal)
  - TeachingModePage
  - ProgressPage
  - SettingsPage
  - ProfilePage
  - NotificationsPage
  - (Future) QuizPage, SummaryPage, QAPage, GroupStudyPage, DashboardPage

---

## 2. Component Tree (MVP)

```
App
├── SplashPage
├── AuthFlow
│   ├── SignupPage
│   │   └── SignupForm
│   ├── LoginPage
│   │   └── LoginForm
│   └── ForgotPasswordPage
│       └── ForgotPasswordForm
└── MainApp
  ├── HomePage
  │   ├── RecentBooks
  │   └── UploadButton
  ├── PDFUploadPage
  │   └── FilePicker
  ├── PDFReaderPage
  │   ├── PageView
  │   ├── TTSControlBar
  │   ├── ProgressBar
  │   └── ModeSwitch (Teaching/Reading)
  ├── TTSControls (overlay/modal)
  ├── TeachingModePage
  │   ├── Explanation
  │   └── DifficultySelector
  ├── ProgressPage
  │   └── ProgressList
  ├── SettingsPage
  │   ├── LanguageSelector
  │   ├── VoiceSelector
  │   └── SpeedSlider
  ├── ProfilePage
  │   └── UserInfo
  └── NotificationsPage
    └── NotificationList
```

---

## 3. Key Component Descriptions
- **SignupPage/LoginPage:** Contain SignupForm/LoginForm for user authentication (email/password, social login)
- **ForgotPasswordPage:** Contains ForgotPasswordForm for password reset
- **PDFUploadPage:** FilePicker for selecting/uploading PDFs, shows upload progress and errors
- **PDFReaderPage:** Displays PDF content, navigation, TTS controls, mode switch
- **TeachingModePage:** Shows explanations, difficulty selector, AI integration (future)
- **ProgressPage:** Shows reading/bookmark progress, resume options
- **SettingsPage:** Language, voice, speed, and app preferences
- **NotificationsPage:** List of push notifications and alerts

---

## 4. Advanced/Future Pages (for expansion)
- **QuizPage:** Auto-generated quizzes from content
- **SummaryPage:** Chapter/page summaries
- **QAPage:** Ask questions, get AI answers
- **GroupStudyPage:** Real-time group reading, chat, moderation
- **DashboardPage:** Analytics, reports, teacher/parent view

---

## 5. Navigation Flow (MVP)
1. SplashPage → AuthFlow (Signup/Login/ForgotPassword)
2. On login success → MainApp (HomePage)
3. HomePage → PDFUploadPage → PDFReaderPage
4. PDFReaderPage ↔ TTSControls/TeachingModePage
5. MainApp menu → ProgressPage, SettingsPage, ProfilePage, NotificationsPage

---

## Next Steps
- Scaffold initial React.js project structure (e.g., using Create React App or Vite)
- Implement routing and basic pages/components
- Integrate with backend API endpoints
