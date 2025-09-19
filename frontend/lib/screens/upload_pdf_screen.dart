import 'package:flutter/material.dart';
import 'package:file_picker/file_picker.dart';
import 'dart:io';
import 'package:http/http.dart' as http;
import 'pdf_viewer_screen.dart';

class UploadPDFScreen extends StatefulWidget {
  const UploadPDFScreen({Key? key}) : super(key: key);

  @override
  State<UploadPDFScreen> createState() => _UploadPDFScreenState();
}

class _UploadPDFScreenState extends State<UploadPDFScreen> {
  String? _result;
  bool _loading = false;
  String? _selectedFilePath;

  Future<void> _pickAndUploadPDF() async {
    setState(() {
      _loading = true;
      _result = null;
      _selectedFilePath = null;
    });
    FilePickerResult? result = await FilePicker.platform.pickFiles(type: FileType.custom, allowedExtensions: ['pdf']);
    if (result != null && result.files.single.path != null) {
      File file = File(result.files.single.path!);
      _selectedFilePath = file.path;
      var request = http.MultipartRequest('POST', Uri.parse('http://localhost:8000/upload-pdf/'));
      request.files.add(await http.MultipartFile.fromPath('file', file.path));
      try {
        var response = await request.send();
        if (response.statusCode == 200) {
          var respStr = await response.stream.bytesToString();
          setState(() {
            _result = respStr;
          });
        } else {
          setState(() {
            _result = 'Error: ${response.statusCode}';
          });
        }
      } catch (e) {
        setState(() {
          _result = 'Error: $e';
        });
      }
    } else {
      setState(() {
        _result = 'No file selected.';
      });
    }
    setState(() {
      _loading = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Upload PDF')),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              ElevatedButton(
                onPressed: _loading ? null : _pickAndUploadPDF,
                child: const Text('Select and Upload PDF'),
              ),
              if (_selectedFilePath != null)
                ElevatedButton(
                  onPressed: _loading
                      ? null
                      : () {
                          Navigator.push(
                            context,
                            MaterialPageRoute(
                              builder: (context) => PDFViewerScreen(filePath: _selectedFilePath!),
                            ),
                          );
                        },
                  child: const Text('View Selected PDF'),
                ),
              const SizedBox(height: 24),
              if (_loading) const CircularProgressIndicator(),
              if (_result != null) ...[
                const SizedBox(height: 16),
                Text(_result!, style: const TextStyle(fontSize: 14)),
              ],
            ],
          ),
        ),
      ),
    );
  }
}
