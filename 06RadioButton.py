from PySide6.QtWidgets import QApplication, QMainWindow, QRadioButton, QHBoxLayout, QWidget
from PySide6.QtWidgets import QButtonGroup, QLabel, QVBoxLayout

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("RadioButton 示例")

    # 创建一个中央窗口部件
    central_widget = QWidget()
    self.setCentralWidget(central_widget)

    # 为中央窗口部件创建一个布局
    layout = QVBoxLayout()

    # 创建一个标签，用于显示选中的选项
    self.label = QLabel("请选择一个选项:")
    layout.addWidget(self.label)

    # 创建一个按钮组，用于分组单选按钮（选项 1, 2, 3）
    button_group1 = QButtonGroup(self)

    # 创建单选按钮
    radio_button1 = QRadioButton("选项 1")
    radio_button2 = QRadioButton("选项 2")
    radio_button3 = QRadioButton("选项 3")

    # 将单选按钮添加到按钮组中
    button_group1.addButton(radio_button1)
    button_group1.addButton(radio_button2)
    button_group1.addButton(radio_button3)

    # 将单选按钮添加到布局中
    layout.addWidget(radio_button1)
    layout.addWidget(radio_button2)
    layout.addWidget(radio_button3)

    # 连接按钮组的信号到槽函数
    button_group1.buttonClicked.connect(self.on_radio_button_clicked)

    # 创建一个标签，用于显示编程语言选择
    self.language_label = QLabel("请选择一种编程语言:")
    layout.addWidget(self.language_label)

    # 创建另一个按钮组，用于分组编程语言单选按钮
    button_group2 = QButtonGroup(self)

    # 创建编程语言单选按钮
    lang_button1 = QRadioButton("Python")
    lang_button2 = QRadioButton("C++")
    lang_button3 = QRadioButton("Java")

    # 将编程语言单选按钮添加到按钮组中
    button_group2.addButton(lang_button1)
    button_group2.addButton(lang_button2)
    button_group2.addButton(lang_button3)

    # 将编程语言单选按钮添加到布局中
    layout.addWidget(lang_button1)
    layout.addWidget(lang_button2)
    layout.addWidget(lang_button3)

    # 连接按钮组的信号到槽函数
    button_group2.buttonClicked.connect(self.on_language_button_clicked)

    # 设置中央窗口部件的布局
    central_widget.setLayout(layout)

  def on_radio_button_clicked(self, button):
    """
    槽函数，用于处理选项 1, 2, 3 的单选按钮被点击时发出的信号。
    更新标签文本以显示选中的选项。
    """
    self.label.setText(f"选中: {button.text()}")

  def on_language_button_clicked(self, button):
    """
    槽函数，用于处理编程语言单选按钮被点击时发出的信号。
    更新标签文本以显示选中的编程语言。
    """
    self.language_label.setText(f"选中编程语言: {button.text()}")

if __name__ == "__main__":
  app = QApplication([])
  window = MainWindow()
  window.show()
  app.exec()
