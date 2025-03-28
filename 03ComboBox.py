from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QBoxLayout, QComboBox
from PySide6.QtCore import Qt

class MyWindow(QWidget):
  def __init__(self):
    super().__init__()

    mainlayout = QBoxLayout(QBoxLayout.TopToBottom, self)

    co = QComboBox(self)
    co.addItems(["选项1", "选项2", "选项3"])
    # co.setEditable(True)
    co.currentIndexChanged.connect(lambda: print(co.currentText()))
    co.currentIndexChanged.connect(lambda: print(co.currentIndex()))

    mainlayout.addWidget(co)
    self.setLayout(mainlayout)

  def hello(self):
    print("hello world!")


if __name__ == '__main__':
  # 创建应用程序实例
  app = QApplication([])
  # 创建主窗口实例
  window = MyWindow()
  # 显示主窗口
  window.show()
  # 运行应用程序事件循环
  app.exec()
