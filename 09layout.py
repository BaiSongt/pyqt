from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLabel, QLineEdit

# 创建主窗口类
class ComplexLayoutExample(QWidget):
  def __init__(self):
    super().__init__()
    self.init_ui()

  def init_ui(self):
    # 设置窗口标题
    self.setWindowTitle("复杂布局示例 - PySide6")

    # 创建主垂直布局
    main_vbox = QVBoxLayout()

    # 添加一个标签到主垂直布局
    label = QLabel("这是一个复杂布局示例")
    main_vbox.addWidget(label)

    # 创建一个水平布局
    hbox = QHBoxLayout()
    hbox.addWidget(QPushButton("按钮1"))
    hbox.addWidget(QPushButton("按钮2"))
    hbox.addWidget(QPushButton("按钮3"))

    # 将水平布局添加到主垂直布局
    main_vbox.addLayout(hbox)

    # 创建一个网格布局
    grid = QGridLayout()
    grid.addWidget(QLabel("姓名:"), 0, 0)
    grid.addWidget(QLineEdit(), 0, 1)
    grid.addWidget(QLabel("年龄:"), 1, 0)
    grid.addWidget(QLineEdit(), 1, 1)
    grid.addWidget(QPushButton("提交"), 2, 0, 1, 2)

    # 将网格布局添加到主垂直布局
    main_vbox.addLayout(grid)

    # 设置主窗口的布局
    self.setLayout(main_vbox)

# 主程序入口
if __name__ == "__main__":
  app = QApplication([])
  window = ComplexLayoutExample()
  window.show()
  app.exec()
