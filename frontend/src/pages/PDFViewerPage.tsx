import React, { useState } from 'react';
import PDFViewer from '../components/PDFViewer';

const PDFViewerPage: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFile(e.target.files?.[0] || null);
  };

  return (
    <div style={{ maxWidth: 800, margin: '2rem auto', padding: 24, border: '1px solid #eee', borderRadius: 8 }}>
      <h2>PDF Viewer</h2>
      <input type="file" accept="application/pdf" onChange={handleFileChange} />
      <div style={{ marginTop: 24 }}>
        <PDFViewer file={file} />
      </div>
    </div>
  );
};

export default PDFViewerPage;
