import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

Form, Window = uic.loadUiType("./unlisted/GUI/tConvert.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
sys.exit(app.exec())