# Authentication Flow (Live-Teacher Frontend)

This document describes the planned authentication flow for the Live-Teacher web application.

## Overview
- Uses Firebase Authentication for user management (signup, login, logout, session)
- Frontend communicates with Firebase Auth directly for authentication
- Backend endpoints require a valid Firebase ID token for protected routes

## User Journey
1. **Signup**
   - User visits `/signup` page
   - Enters email, password, and (optionally) display name
   - Frontend calls Firebase Auth API to create user
   - On success, user is redirected to the main dashboard
2. **Login**
   - User visits `/login` page
   - Enters email and password
   - Frontend calls Firebase Auth API to sign in
   - On success, user is redirected to the main dashboard
3. **Session Management**
   - Firebase manages session tokens in the browser
   - On page reload, user remains logged in if token is valid
   - If token expires, user is redirected to `/login`
4. **Logout**
   - User clicks logout button
   - Frontend calls Firebase Auth signOut
   - User is redirected to `/login`

## Protected Routes
- All routes except `/login` and `/signup` require authentication
- Use a React context/provider to manage auth state
- Redirect unauthenticated users to `/login`

## Backend Integration
- Frontend sends Firebase ID token in `Authorization: Bearer <token>` header for API requests
- Backend verifies token before processing protected endpoints

## Next Steps
- Implement Firebase Auth integration in frontend
- Add auth context/provider and route guards
- Connect backend to verify Firebase tokens

---
See also: `/frontend/src/pages/LoginPage.tsx`, `/frontend/src/pages/SignupPage.tsx` for UI entry points.
