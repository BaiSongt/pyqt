from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QSlider
from PySide6.QtCore import Qt

class MyWindow(QWidget):
  def __init__(self):
    """
    Initializes the main window with a vertical layout containing a horizontal slider.

    The slider is configured with:
    - Tick marks displayed below the slider.
    - Tick interval set to 5.
    - Minimum value set to 50.
    - Maximum value set to 100.

    The slider's value change event is connected to the `showSlider` method.
    """
    super().__init__()

    mainlayout = QVBoxLayout()

    slider_1 = QSlider(Qt.Orientation.Horizontal)
    slider_1.setTickPosition(QSlider.TickPosition.TicksBelow)
    slider_1.setTickInterval(5)

    # slider_1.setMinimum(50)
    # slider_1.setMaximum(100)
    slider_1.setRange(10, 20)

    slider_1.valueChanged.connect(self.showSlider)

    mainlayout.addWidget(slider_1)
    self.setLayout(mainlayout)

  def hello(self):
    print("hello world!")

  def showSlider(self, value):
    """
    显示滑块的值。
    此方法用于获取触发该方法的滑块控件，并打印其当前的值。
    """
    print(f"current Slider: {value}")
    # current_widget = self.sender()
    # print(current_widget.value())


if __name__ == '__main__':
  # 创建应用程序实例
  app = QApplication([])
  # 创建主窗口实例
  window = MyWindow()
  # 显示主窗口
  window.show()
  # 运行应用程序事件循环
  app.exec()
