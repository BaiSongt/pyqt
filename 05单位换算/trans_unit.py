from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QBoxLayout
from PySide6.QtCore import Qt
from trans_unit_ui import Ui_Form

class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bind()

    def bind(self):
        top_lable = self.label
        top_lable.setText("hello !")

        usr_lable = self.label_2
        usr_lable.setText("World!!!!!!")

        unit_1 = self.comboBox
        unit_1.addItem("nm 纳米")
        unit_1.addItem("um 微米")
        unit_1.addItem("mm 毫米")
        unit_1.addItem("cm 厘米")
        unit_1.addItem("m  米")
        unit_1.addItem("km 千米")

        unit_2 = self.comboBox_2
        unit_2.addItem("nm 纳米")
        unit_2.addItem("um 微米")
        unit_2.addItem("mm 毫米")
        unit_2.addItem("cm 厘米")
        unit_2.addItem("m  米")
        unit_2.addItem("km 千米")

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
