from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit
from PySide6.QtCore import Qt
from 翻译_ui import Ui_Form

class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("LLM 翻译")

        ## TODO：添加LLM翻译功能

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
