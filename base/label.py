from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt

class MyWindow(QMainWindow):
  """
  MyWindow 是 QMainWindow 的子类，用作应用程序的主窗口。

  方法:
    __init__(): 初始化 MyWindow 实例并设置主窗口。
  """
  def __init__(self):
    super().__init__()
    lb = QLabel("我是一个标签", self)
    lb.setText("我被修改了")

    ## 对齐方式
    lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

if __name__ == '__main__':
  # 创建应用程序实例
  app = QApplication([])
  # 创建主窗口实例
  window = MyWindow()
  # 显示主窗口
  window.show()
  # 运行应用程序事件循环
  app.exec()
