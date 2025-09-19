import 'package:flutter/material.dart';

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
      home: const Scaffold(
        body: Center(child: Text('Live-Teacher Flutter App')),
      ),
    );
  }
}
