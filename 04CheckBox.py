from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QBoxLayout, QCheckBox
from PySide6.QtCore import Qt

class MyWindow(QWidget):
  def __init__(self):
    super().__init__()

    mainlayout = QBoxLayout(QBoxLayout.TopToBottom, self)

    co = QCheckBox("Check", self)
    co.setChecked(True)
    co.stateChanged.connect(lambda: print(co.isChecked()))

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
