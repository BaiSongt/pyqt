## PySide6 基础控件的综合运用

from PySide6.QtWidgets import QApplication, QWidget, \
                              QVBoxLayout, QPushButton, QLabel, QLineEdit, \
                              QComboBox, QCheckBox, \
                              QRadioButton, QButtonGroup,\
                              QTextEdit, QPlainTextEdit, QSlider


from PySide6.QtCore import Qt

markdown = """
# PySide6 Basic Widgets Example

This example demonstrates the use of various PySide6 widgets, including:

- **QLabel**: Displays a label.
- **QPushButton**: A clickable button.
- **QLineEdit**: A single-line text box with password masking.
- **QComboBox**: A dropdown selection box.
- **QCheckBox**: Checkable boxes with different states.
- **QRadioButton**: Radio buttons grouped for gender and favorite subjects.
- **QTextEdit**: A multi-line text editor with placeholder text.

## Features

- Button click counter.
- Dynamic label updates based on input.
- Dropdown selection handling.
- Checkbox and radio button state changes.
"""

html = """
<h1>PySide6 Basic Widgets Example</h1>
<p>This example demonstrates the use of various PySide6 widgets, including:</p>
<ul>
  <li><b>QLabel</b>: Displays a label.</li>
  <li><b>QPushButton</b>: A clickable button.</li>
  <li><b>QLineEdit</b>: A single-line text box with password masking.</li>
  <li><b>QComboBox</b>: A dropdown selection box.</li>
  <li><b>QCheckBox</b>: Checkable boxes with different states.</li>
  <li><b>QRadioButton</b>: Radio buttons grouped for gender and favorite subjects.</li>
  <li><b>QTextEdit</b>: A multi-line text editor with placeholder text.</li>
</ul>
<h2>Features</h2>
<ul>
  <li>Button click counter.</li>
  <li>Dynamic label updates based on input.</li>
  <li>Dropdown selection handling.</li>
  <li>Checkbox and radio button state changes.</li>
</ul>
"""


class MyWindow(QWidget) :
  def __init__(self):
    super().__init__()

    self.count = 0

    self.mainlayout = QVBoxLayout()

    # lable
    self.Title = QLabel("PySide6 Basic Widgets Example")
    self.Title.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.lb1 = QLabel()
    self.lb1.setText("标签")
    self.lb1.setAlignment(Qt.AlignmentFlag.AlignCenter)

    # pushButton
    self.btn1 = QPushButton("QPushButton")

    # lineEdit
    self.lineEdit1 = QLineEdit()
    self.lineEdit1.setPlaceholderText("Password:")
    self.lineEdit1.setEchoMode(QLineEdit.EchoMode.Password)

    # combox
    self.combox = QComboBox()
    self.combox.addItems(["mode 1", "mode 2", "mode 3"])
    self.combox.removeItem(2)

    # check box
    self.cbox1 = QCheckBox("Check Box 1")
    self.cbox2 = QCheckBox("Check Box 2")
    self.cbox1.setCheckable(True)
    self.cbox1.setChecked(True)
    self.cbox2.setCheckable(False)

    # 创建单选按钮
    self.genderMan = QRadioButton("男")
    self.genderWomen = QRadioButton("女")
    self.faMath = QRadioButton("数学")
    self.faChinese = QRadioButton("语文")

    # 创建按钮组
    self.genderGroup = QButtonGroup()
    self.genderGroup.addButton(self.genderMan)
    self.genderGroup.addButton(self.genderWomen)

    self.favoriteGroup = QButtonGroup()
    self.favoriteGroup.addButton(self.faMath)
    self.favoriteGroup.addButton(self.faChinese)

    # TextEdit
    self.richText = QTextEdit()
    self.richText.setPlaceholderText("请输入内容")

    self.markdownSelect = QRadioButton("Markdown")
    self.HtmlSelect = QRadioButton("HTML")
    self.TextSelect = QRadioButton("plainText")
    self.formatGroup = QButtonGroup()
    self.formatGroup.addButton(self.HtmlSelect)
    self.formatGroup.addButton(self.TextSelect)
    self.formatGroup.addButton(self.markdownSelect)

    # 纯文本框
    self.plainText = QPlainTextEdit()
    self.plainText.setPlaceholderText("这是一个纯文本框")

    # 滚动条
    self.slider = QSlider()
    self.slider.setOrientation(Qt.Orientation.Horizontal)
    self.slider.setRange(0, 10)
    self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)

    # layout add
    self.mainlayout.addWidget(self.Title)
    self.mainlayout.addWidget(self.lb1)
    self.mainlayout.addWidget(self.btn1)
    self.mainlayout.addWidget(self.lineEdit1)
    self.mainlayout.addWidget(self.combox)
    self.mainlayout.addWidget(self.cbox1)
    self.mainlayout.addWidget(self.cbox2)
    self.mainlayout.addWidget(self.genderMan)
    self.mainlayout.addWidget(self.genderWomen)
    self.mainlayout.addWidget(self.faMath)
    self.mainlayout.addWidget(self.faChinese)
    self.mainlayout.addWidget(self.richText)
    self.mainlayout.addWidget(self.HtmlSelect)
    self.mainlayout.addWidget(self.TextSelect)
    self.mainlayout.addWidget(self.markdownSelect)
    self.mainlayout.addWidget(self.plainText)
    self.mainlayout.addWidget(self.slider)
    self.setLayout(self.mainlayout)
    self.bind()

  def bind(self):
    self.btn1.clicked.connect(self.update_label)
    self.lineEdit1.textChanged.connect(self.lineEdit_textChanged)
    self.lineEdit1.returnPressed.connect(self.lineEdit_returnPressed)
    self.combox.currentTextChanged.connect(self.comboxChanged)
    self.cbox1.stateChanged.connect(self.check1Changed)
    self.cbox2.stateChanged.connect(self.check2Changed)
    self.genderMan.clicked.connect(lambda: print("男"))
    self.genderWomen.clicked.connect(lambda: print("女"))
    self.faMath.clicked.connect(lambda: print("数学"))
    self.faChinese.clicked.connect(lambda: print("语文"))
    self.richText.textChanged.connect(lambda : print("rich 文本框内容改变了"))
    self.plainText.textChanged.connect(lambda : print("plain 文本框内容改变了"))
    self.markdownSelect.clicked.connect(self.textFormatSelect)
    self.HtmlSelect.clicked.connect(self.textFormatSelect)
    self.TextSelect.clicked.connect(self.textFormatSelect)
    self.btn1.clicked.connect(self.richText.clear)
    self.btn1.clicked.connect(self.plainText.clear)
    self.slider.valueChanged.connect(self.sliderChangedPlainText)

  def update_label(self):
      self.count += 1
      self.lb1.setText(f"clicked {self.count}")

  def lineEdit_textChanged(self, text):
      print(f"LineEdit textChanged {text}")

  def lineEdit_returnPressed(self):
      print("Line Edit Enter!")
      print("Line Edit : " + self.lineEdit1.text())
      self.lb1.setText(self.lineEdit1.text())

  def comboxChanged(self, text):
      print("Combox Changed:", text)

  def check1Changed(self, state):
      print("Check box 1 state changed", state)

  def check2Changed(self):
      print("Check box 2 state is :", self.cbox2.isChecked())

  def textFormatSelect(self):
      if self.markdownSelect.isChecked() :
         self.richText.setMarkdown(markdown)
      elif self.HtmlSelect.isChecked() :
         self.richText.setHtml(html)
      elif self.TextSelect.isChecked():
         self.richText.setPlainText(markdown)
      else : pass

  def sliderChangedPlainText(self, value):
     print(value)
     self.plainText.setPlainText(f"{value}")

if __name__ == "__main__":
  app = QApplication()
  window = MyWindow()
  window.show()
  app.exec()

