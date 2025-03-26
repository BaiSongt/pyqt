from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MyWindow(QMainWindow):
  """
  MyWindow 是 QMainWindow 的子类，用作应用程序的主窗口。

  方法:
    __init__(): 初始化 MyWindow 实例并设置主窗口。
  """
  def __init__(self):
    super().__init__()
    btn = QPushButton("按钮 点一下",self)
    btn.setGeometry(0,0,100,50)
    btn.setToolTip("点我有惊喜")
    btn.setText("我被重新设置了")

if __name__ == '__main__':
  # 创建应用程序实例
  app = QApplication([])
  # 创建主窗口实例
  window = MyWindow()
  # 显示主窗口
  window.show()
  # 运行应用程序事件循环
  app.exec()
