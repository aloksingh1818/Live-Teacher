import React, { useState } from 'react';

const UploadPage: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [result, setResult] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFile(e.target.files?.[0] || null);
    setResult(null);
    setError(null);
  };

  const handleUpload = async () => {
    if (!file) {
      setError('Please select a PDF file.');
      console.error('No file selected for upload.');
      return;
    }
    setLoading(true);
    setError(null);
    setResult(null);
    const formData = new FormData();
    formData.append('file', file);
    const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000';
    console.log('[UploadPage] Using API URL:', apiUrl);
    try {
      console.log('[UploadPage] Sending POST to', `${apiUrl}/pdf/upload`);
      const response = await fetch(`${apiUrl}/pdf/upload`, {
        method: 'POST',
        body: formData,
      });
      console.log('[UploadPage] Response status:', response.status);
      let data = null;
      try {
        data = await response.json();
        console.log('[UploadPage] Response JSON:', data);
      } catch (jsonErr) {
        console.error('[UploadPage] Failed to parse JSON:', jsonErr);
      }
      if (!response.ok) {
        const detail = data && data.detail ? data.detail : response.statusText;
        console.error('[UploadPage] Upload failed:', detail);
        throw new Error(detail || 'Upload failed');
      }
      setResult(data && data.text ? data.text : '[No text returned]');
    } catch (err: any) {
      setError(err.message || 'Unknown error');
      console.error('[UploadPage] Upload error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: 600, margin: '2rem auto', padding: 24, border: '1px solid #eee', borderRadius: 8 }}>
      <h2>Upload PDF for Text Extraction</h2>
      <input type="file" accept="application/pdf" onChange={handleFileChange} />
      <button onClick={handleUpload} disabled={loading} style={{ marginLeft: 8 }}>
        {loading ? 'Uploading...' : 'Upload'}
      </button>
      {error && <div style={{ color: 'red', marginTop: 16 }}>{error}</div>}
      {result && (
        <div style={{ marginTop: 24 }}>
          <h3>Extracted Text:</h3>
          <pre style={{ background: '#f8f8f8', padding: 12, borderRadius: 4, maxHeight: 300, overflow: 'auto' }}>{result}</pre>
        </div>
      )}
    </div>
  );
};

export default UploadPage;
