import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget
from 计算器_ui import Ui_Form

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
    self.bind()

  def bind(self):
    """
    bind() 方法用于绑定按钮的点击事件。
    """
    self.pushButton_0.clicked.connect(lambda: self.addNumber("0"))
    self.pushButton_1.clicked.connect(lambda: self.addNumber("1"))
    self.pushButton_2.clicked.connect(lambda: self.addNumber("2"))
    self.pushButton_3.clicked.connect(lambda: self.addNumber("3"))
    self.pushButton_4.clicked.connect(lambda: self.addNumber("4"))
    self.pushButton_5.clicked.connect(lambda: self.addNumber("5"))
    self.pushButton_6.clicked.connect(lambda: self.addNumber("6"))
    self.pushButton_7.clicked.connect(lambda: self.addNumber("7"))
    self.pushButton_8.clicked.connect(lambda: self.addNumber("8"))
    self.pushButton_9.clicked.connect(lambda: self.addNumber("9"))
    self.dot.clicked.connect(lambda: self.addNumber("."))
    self.add.clicked.connect(lambda: self.addNumber("+"))
    self.sub.clicked.connect(lambda: self.addNumber("-"))
    self.mul.clicked.connect(lambda: self.addNumber("*"))
    self.div.clicked.connect(lambda: self.addNumber("/"))

    self.clear.clicked.connect(self.clearAll)
    self.equal.clicked.connect(self.result)
    self.back.clicked.connect(self.backNum)


  def addNumber(self, number):
    """
    addNumber() 方法用于添加数字到文本框。
    """
    text = self.lineEdit.text()
    self.lineEdit.setText(text + number)

  def clearAll(self):
    self.lineEdit.clear()

  def backNum(self):
    text = self.lineEdit.text()
    self.lineEdit.setText(text[:-1])

  def result(self):
    text = self.lineEdit.text()
    try:
      result = eval(text)
      self.lineEdit.setText(str(result))
    except:
      self.lineEdit.setText("Error")



if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = MyWindow()
  window.show()
  sys.exit(app.exec_())
