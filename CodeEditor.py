import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QFileDialog, QLabel
from PyQt6.QtGui import QFont, QColor, QPalette, QLinearGradient, QBrush
from PyQt6.QtCore import Qt

class CodeEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("🔥 Stylish Code Editor 🔥")
        self.setGeometry(100, 100, 700, 500)
        
        # Gradient Background
        palette = QPalette()
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0.0, QColor("#1e3c72"))  # Dark Blue
        gradient.setColorAt(1.0, QColor("#2a5298"))  # Light Blue
        palette.setBrush(QPalette.ColorRole.Window, QBrush(gradient))
        self.setPalette(palette)
        
        self.layout = QVBoxLayout()
        
        # Header Label
        self.header = QLabel("🔥 Super Cool Code Editor 🔥")
        self.header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.header.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        self.header.setStyleSheet("color: white; padding: 10px; background-color: rgba(0, 0, 0, 0.5); border-radius: 10px;")
        self.layout.addWidget(self.header)
        
        # Text Editor
        self.text_editor = QTextEdit()
        self.text_editor.setFont(QFont("Courier", 12))
        self.text_editor.setStyleSheet("background-color: #1e1e1e; color: #dcdcdc; padding: 10px; border-radius: 5px;")
        self.layout.addWidget(self.text_editor)
        
        # Buttons
        button_style = "border: none; padding: 10px; font-size: 14px; color: white; font-weight: bold; border-radius: 8px;"
        
        self.open_button = QPushButton("📂 Open File")
        self.open_button.setStyleSheet(button_style + "background: linear-gradient(to right, #ff416c, #ff4b2b);")
        self.open_button.clicked.connect(self.open_file)
        self.layout.addWidget(self.open_button)
        
        self.save_button = QPushButton("💾 Save File")
        self.save_button.setStyleSheet(button_style + "background: linear-gradient(to right, #56ab2f, #a8e063);")
        self.save_button.clicked.connect(self.save_file)
        self.layout.addWidget(self.save_button)
        
        self.setLayout(self.layout)
    
    def open_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Python Files (*.py)", options=options)
        if file_path:
            with open(file_path, "r") as file:
                self.text_editor.setText(file.read())
    
    def save_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "All Files (*);;Python Files (*.py)", options=options)
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_editor.toPlainText())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CodeEditor()
    window.show()
    sys.exit(app.exec())

