import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget
from 计算器_布局_ui import Ui_Form

class MyWindow(QWidget, Ui_Form):
  """
  MyWindow 是一个自定义的 QWidget 类，集成了 Ui_Form 界面。

  该类作为应用程序的主窗口，继承自 QWidget 和 Ui_Form。
  它通过调用 Ui_Form 类的 setupUi 方法来初始化用户界面。

  方法:
    __init__(): 初始化 MyWindow 实例并设置用户界面。
  """
  def __init__(self):
    super().__init__()
    self.setupUi(self)


if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = MyWindow()
  window.show()
  sys.exit(app.exec_())
