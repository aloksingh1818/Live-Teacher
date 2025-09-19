import 'package:flutter/material.dart';
import 'package:pdfx/pdfx.dart';

class PDFViewerScreen extends StatefulWidget {
  final String filePath;
  const PDFViewerScreen({Key? key, required this.filePath}) : super(key: key);

  @override
  State<PDFViewerScreen> createState() => _PDFViewerScreenState();
}

class _PDFViewerScreenState extends State<PDFViewerScreen> {
  late PdfControllerPinch _pdfController;

  @override
  void initState() {
    super.initState();
    _pdfController = PdfControllerPinch(document: PdfDocument.openFile(widget.filePath));
  }

  @override
  void dispose() {
    _pdfController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('PDF Viewer')),
      body: PdfViewPinch(
        controller: _pdfController,
      ),
    );
  }
}
