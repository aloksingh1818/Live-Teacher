
import 'package:flutter/material.dart';
import 'screens/upload_pdf_screen.dart';

void main() {
  runApp(const LiveTeacherApp());
}

class LiveTeacherApp extends StatelessWidget {
  const LiveTeacherApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Live-Teacher',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      initialRoute: '/upload',
      routes: {
        '/upload': (context) => const UploadPDFScreen(),
        // PDFViewerScreen is navigated to via MaterialPageRoute
      },
    );
  }
}
