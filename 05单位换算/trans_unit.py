from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QBoxLayout
from PySide6.QtCore import Qt
from trans_unit_ui import Ui_Form

class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lengthVar = {"nm": 1e-9, "um": 1e-6, "mm": 1e-3, "cm": 1e-2, "m": 1, "km": 1e3}
        self.wightVar = {"g": 1, "kg": 1e3, "mg": 1e-3, "t": 1e6}
        self.timeVar = {"s": 1, "min": 60, "h": 3600}
        self.typeDict = {"length": self.lengthVar, "weight": self.wightVar, "time": self.timeVar}

        self.bind()

    def bind(self):
        # 绑定按钮事件
        self.input_lable_1.setText("0")
        self.input_lable_1.setPlaceholderText("请输入数值")
        self.input_lable_2.setPlaceholderText("转换结果")

        for unit_type in self.typeDict.keys():
            self.comboBox_unit_type.addItem(unit_type)
        for unit in self.lengthVar.keys():
            self.comboBox_unit_1.addItem(unit)
            self.comboBox_unit_2.addItem(unit)

        # 显示当前转换结果
        # self.currentShow()
        self.comboBox_unit_1.currentTextChanged.connect(self.currentShow)
        self.comboBox_unit_2.currentTextChanged.connect(self.currentShow)
        self.input_lable_1.textChanged.connect(self.currentShow)
        self.input_lable_2.textChanged.connect(self.currentShow)

    def changeUnitType(self):
        # 清空下拉框
        self.comboBox_unit_1.clear()
        self.comboBox_unit_2.clear()
        # 获取单位类型
        unit_type = self.comboBox_unit_type.currentText()
        # 获取单位字典
        unit_dict = self.typeDict[unit_type]
        # 添加单位到下拉框
        for unit in unit_dict.keys():
            self.comboBox_unit_1.addItem(unit)
            self.comboBox_unit_2.addItem(unit)
        # 设置下拉框默认值
        self.hello()
        self.comboBox_unit_1.setCurrentIndex(0)
        self.comboBox_unit_2.setCurrentIndex(0)


    def currentShow(self):
        if self.input_lable_1.text() != "":
            self.calculate()
        self.label.setText(self.input_lable_1.text() + " " +
                            self.comboBox_unit_1.currentText() + " = " )
        self.label_2.setText(self.input_lable_2.text() + " " +
                            self.comboBox_unit_2.currentText())
        # 绑定下拉框事件
        self.comboBox_unit_type.currentTextChanged.connect(self.changeUnitType)



    def calculate(self):
        # 获取输入值
        value = self.input_lable_1.text()
        # 获取单位类型
        unit_type = self.comboBox_unit_type.currentText()
        # 获取输入单位
        unit_1 = self.comboBox_unit_1.currentText()
        # 获取输出单位
        unit_2 = self.comboBox_unit_2.currentText()
        # 获取单位字典
        unit_dict = self.typeDict[unit_type]
        # 进行单位转换
        try:
            value = float(value)
        except ValueError:
            print("Invalid input value")
            return
        if unit_1 not in unit_dict or unit_2 not in unit_dict:
            print("Invalid unit type")
            return
        # 进行单位转换
        # 计算转换后的值
        converted_value = value * unit_dict[unit_1] / unit_dict[unit_2]
        # 显示转换后的值
        self.input_lable_2.setText(str(converted_value))

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
