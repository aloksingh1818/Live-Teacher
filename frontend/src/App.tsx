import React from 'react';
import { Routes, Route } from 'react-router-dom';

import LoginPage from './pages/LoginPage';
import SignupPage from './pages/SignupPage';
import HomePage from './pages/HomePage';
import UploadPage from './pages/UploadPage';
import PDFViewerPage from './pages/PDFViewerPage';


const App: React.FC = () => (
  <Routes>
    <Route path="/" element={<HomePage />} />
    <Route path="/login" element={<LoginPage />} />
    <Route path="/signup" element={<SignupPage />} />
  <Route path="/upload" element={<UploadPage />} />
  <Route path="/view" element={<PDFViewerPage />} />
  </Routes>
);

export default App;
