import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QMessageBox, QLabel, QLineEdit
from PyQt5.QtCore import pyqtSlot
 
 
class App(QMainWindow, QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = "Celsius-Fahrenheit Converter"
 
        # Initialized programs place and size
        self.left = 20
        self.top = 20
        self.width = 360
        self.height = 100
 
        self.init_ui()
 
    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        # button is created for converting from celsius to fahrenheit
        self.celsius_button = QPushButton("Convert", self)
        self.celsius_button.setToolTip("Convert button from celsius to fahrenheit")
        self.celsius_button.setGeometry(20, 50, 90, 30)
 
        # button is created for converting from fahrenheit to celsius
        self.fahreinheit_button = QPushButton("Convert", self)
        self.fahreinheit_button.setToolTip("Convert Button from fahrenheit to celsius")
        self.fahreinheit_button.setGeometry(160, 50, 90, 30)
 
        # celsius textbox is created for writing degree
        self.celsius_textbox = QLineEdit(self)
        self.celsius_textbox.move(80, 20)
        self.celsius_textbox.resize(70, 20)
 
        # fahrenheit textbox is created for writing fahrenheit degree
        self.fahrenheit_text_box = QLineEdit(self)
        self.fahrenheit_text_box.move(250, 20)
        self.fahrenheit_text_box.resize(70, 20)
 
 
        # celsius label is created
        self.celsius_label = QLabel("Celsius : ", self)
        self.celsius_label.setGeometry(20, 20, 70, 20)
 
        # fahrenheit label is created
        self.fahrenheit_label = QLabel("Fahrenheit : ", self)
        self.fahrenheit_label.setGeometry(160, 20, 100, 20)
 
        self.celsius_button.clicked.connect(self.first_on_click)
        self.fahreinheit_button.clicked.connect(self.second_on_click)
        self.show()
 
    # Converts the degree from celsius to fahrenheit
    def cels_to_fahr(self, degree):
        return ((degree * 9) / 5) + 32
 
    # Converts the degree from fahrenheit to celsius
    def fahr_to_cels(self, degree):
        return (degree - 32) * (5 / 9)
 
    @pyqtSlot()
    def first_on_click(self):
 
        # ValueError situations are handled
        try:
            print("First button is clicked")
            degree = self.celsius_textbox.text()
            answer = self.cels_to_fahr(float(degree))
            QMessageBox.question(self, "Answer", "Fahrenheit : " + str(answer), QMessageBox.Ok, QMessageBox.Ok)
        except ValueError:
            print("Error in first button")
            QMessageBox.question(self, "Error", "Only integer and floating numbers with '.' is being accepted", QMessageBox.Ok, QMessageBox.Ok)
 
    @pyqtSlot()
    def second_on_click(self):
 
        # ValueError situations are handled
        try:
            print("Second button is clicked")
            degree = self.fahrenheit_text_box.text()
            answer = self.fahr_to_cels(float(degree))
            QMessageBox.question(self, "Answer", "Celsius : " + str(answer), QMessageBox.Ok, QMessageBox.Ok)
        except ValueError:
            print("Error in second button")
            QMessageBox.question(self, "Error", "Only integer and floating numbers with '.' is being accepted", QMessageBox.Ok, QMessageBox.Ok)
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())