import React from 'react';
import { Document, Page, pdfjs } from 'react-pdf';

pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.js`;

interface PDFViewerProps {
  file: File | string | null;
}

const PDFViewer: React.FC<PDFViewerProps> = ({ file }) => {
  const [numPages, setNumPages] = React.useState<number | null>(null);
  const [pageNumber, setPageNumber] = React.useState(1);

  const onDocumentLoadSuccess = ({ numPages }: { numPages: number }) => {
    setNumPages(numPages);
    setPageNumber(1);
  };

  return (
    <div style={{ textAlign: 'center' }}>
      {file ? (
        <>
          <Document file={file} onLoadSuccess={onDocumentLoadSuccess}>
            <Page pageNumber={pageNumber} />
          </Document>
          <div style={{ marginTop: 8 }}>
            <button onClick={() => setPageNumber(p => Math.max(1, p - 1))} disabled={pageNumber <= 1}>
              Previous
            </button>
            <span style={{ margin: '0 12px' }}>
              Page {pageNumber} of {numPages}
            </span>
            <button onClick={() => setPageNumber(p => (numPages ? Math.min(numPages, p + 1) : p + 1))} disabled={numPages ? pageNumber >= numPages : true}>
              Next
            </button>
          </div>
        </>
      ) : (
        <div style={{ color: '#888' }}>No PDF selected.</div>
      )}
    </div>
  );
};

export default PDFViewer;
