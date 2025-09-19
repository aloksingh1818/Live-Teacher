# Day 5: Frontend Component Structure (Including Signup/Login Screens)

This document outlines the planned component structure for the Live-Teacher Flutter app, including all major screens, widgets, and navigation flows for MVP, advanced, and future features.

---

## 1. App Navigation Overview
- SplashScreen
- AuthFlow (Signup, Login, Forgot Password)
- MainApp (after login)
  - HomeScreen
  - PDFUploadScreen
  - PDFReaderScreen
  - TTSScreen (controls overlay)
  - TeachingModeScreen
  - ProgressScreen
  - SettingsScreen
  - ProfileScreen
  - NotificationsScreen
  - (Future) QuizScreen, SummaryScreen, QAScreen, GroupStudyScreen, DashboardScreen

---

## 2. Component Tree (MVP)

```
App
├── SplashScreen
├── AuthFlow
│   ├── SignupScreen
│   ├── LoginScreen
│   └── ForgotPasswordScreen
└── MainApp
    ├── HomeScreen
    │   ├── RecentBooksWidget
    │   └── UploadButton
    ├── PDFUploadScreen
    │   └── FilePickerWidget
    ├── PDFReaderScreen
    │   ├── PageViewWidget
    │   ├── TTSControlBar
    │   ├── ProgressBar
    │   └── ModeSwitch (Teaching/Reading)
    ├── TTSScreen (overlay/modal)
    ├── TeachingModeScreen
    │   ├── ExplanationWidget
    │   └── DifficultySelector
    ├── ProgressScreen
    │   └── ProgressListWidget
    ├── SettingsScreen
    │   ├── LanguageSelector
    │   ├── VoiceSelector
    │   └── SpeedSlider
    ├── ProfileScreen
    │   └── UserInfoWidget
    └── NotificationsScreen
        └── NotificationListWidget
```

---

## 3. Key Widget Descriptions
- **SignupScreen/LoginScreen:** Forms for user authentication (email/password, social login)
- **PDFUploadScreen:** File picker, upload progress, error handling
- **PDFReaderScreen:** Displays PDF, navigation, TTS controls, mode switch
- **TeachingModeScreen:** Shows explanations, difficulty selector, AI integration (future)
- **ProgressScreen:** Shows reading/bookmark progress, resume options
- **SettingsScreen:** Language, voice, speed, and app preferences
- **NotificationsScreen:** List of push notifications and alerts

---

## 4. Advanced/Future Screens (for expansion)
- **QuizScreen:** Auto-generated quizzes from content
- **SummaryScreen:** Chapter/page summaries
- **QAScreen:** Ask questions, get AI answers
- **GroupStudyScreen:** Real-time group reading, chat, moderation
- **DashboardScreen:** Analytics, reports, teacher/parent view

---

## 5. Navigation Flow (MVP)
1. SplashScreen → AuthFlow (Signup/Login)
2. On login success → MainApp (HomeScreen)
3. HomeScreen → PDFUploadScreen → PDFReaderScreen
4. PDFReaderScreen ↔ TTSScreen/TeachingModeScreen
5. MainApp menu → ProgressScreen, SettingsScreen, ProfileScreen, NotificationsScreen

---

## Next Steps
- Set up initial Flutter project structure (Day 9)
- Implement navigation and basic screens
- Integrate with backend API endpoints
