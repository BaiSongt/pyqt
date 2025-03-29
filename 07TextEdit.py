from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit
from PySide6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TextEdit 示例")

        # 创建一个垂直布局
        layout = QVBoxLayout()

        # 创建一个 QTextEdit 控件
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("请输入文本...")  # 设置占位符文本

        # 将 QTextEdit 添加到布局中
        layout.addWidget(self.text_edit)

        # 设置布局
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
