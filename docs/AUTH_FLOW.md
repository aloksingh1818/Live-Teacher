# Authentication Flow (Live-Teacher)

This document describes the authentication flow for the Live-Teacher app (Flutter + FastAPI + Firebase Auth).

---

## 1. Signup
- User enters email and password in the Flutter app
- App calls Firebase Auth to create a new user
- On success, user is logged in and receives a JWT/session token
- User info is stored in Firestore (if needed)

## 2. Login
- User enters email and password
- App calls Firebase Auth to authenticate
- On success, user receives a JWT/session token
- Session is managed in the app (auto-login, logout, etc.)

## 3. Authenticated Requests
- All API requests from the app include the Firebase Auth token in the header
- FastAPI backend verifies the token using firebase-admin SDK
- If valid, request is processed; if not, returns 401 Unauthorized

## 4. Logout
- User logs out in the app
- Session token is cleared from the app

---

## Notes
- Social login (Google, Apple, etc.) can be added later
- Password reset handled via Firebase Auth
- All sensitive data is encrypted in transit (HTTPS)
