from PyQt5.QtWidgets import *
from view import *
from functions import *


def remove_zeros(number):
    string = str(number)
    return string.rstrip(
        '0').rstrip('.') if '.' in string else string


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton_area.clicked.connect(lambda: self.area())
        self.pushButton_perim.clicked.connect(lambda: self.perim())
        self.comboBox_shapes.currentIndexChanged.connect(lambda: self.combobox_update())

    def area(self):
        try:
            value_1 = float(self.lineEdit_dimension_1.text())
            if self.lineEdit_dimension_2.isEnabled():
                value_2 = float(self.lineEdit_dimension_2.text())
            else:
                value_2 = 0
        except ValueError:
            self.label_output.setText('Please enter a number for all text boxes')
        else:
            output = area_func(self.comboBox_shapes.currentIndex(), value_1, value_2)
            self.label_output.setText(f"Area:\n"
                                      f"{remove_zeros(output)}")

    def perim(self):
        try:
            value_1 = float(self.lineEdit_dimension_1.text())
            if self.lineEdit_dimension_2.isEnabled():
                value_2 = float(self.lineEdit_dimension_2.text())
            else:
                value_2 = 0
            if self.lineEdit_dimension_3.isEnabled():
                value_3 = float(self.lineEdit_dimension_3.text())
            else:
                value_3 = 0
        except ValueError:
            self.label_output.setText('Please enter a number for all text boxes')
        else:
            output = str(perimeter_func(self.comboBox_shapes.currentIndex(), value_1, value_2, value_3))
            self.label_output.setText(f"Perimeter:\n"
                                      f"{remove_zeros(output)}")

    def combobox_update(self):
        match self.comboBox_shapes.currentIndex():
            case 1:
                self.reset_input()
                self.lineEdit_dimension_1.setEnabled(True)
                self.label_dimension_1.setText("Side Length")
            case 2:
                self.reset_input()
                self.lineEdit_dimension_1.setEnabled(True)
                self.label_dimension_1.setText("Length")
                self.lineEdit_dimension_2.setEnabled(True)
                self.label_dimension_2.setText("Width")
            case 3:
                self.reset_input()
                self.lineEdit_dimension_1.setEnabled(True)
                self.label_dimension_1.setText("Radius")
            case 4:
                self.reset_input()
                self.lineEdit_dimension_1.setEnabled(True)
                self.label_dimension_1.setText("Side 1 Length")
                self.lineEdit_dimension_2.setEnabled(True)
                self.label_dimension_2.setText("Side 2 Length")
                self.lineEdit_dimension_3.setEnabled(True)
                self.label_dimension_3.setText("Side 3 Length")
                self.pushButton_area.setEnabled(False)
            case 5:
                self.reset_input()
                self.lineEdit_dimension_1.setEnabled(True)
                self.label_dimension_1.setText("Height")
                self.lineEdit_dimension_2.setEnabled(True)
                self.label_dimension_2.setText("Width")
                self.pushButton_perim.setEnabled(False)
            case _:
                self.reset_input()
                self.pushButton_perim.setEnabled(False)
                self.pushButton_area.setEnabled(False)

    def reset_input(self):
        self.pushButton_perim.setEnabled(True)
        self.pushButton_area.setEnabled(True)
        self.lineEdit_dimension_1.setEnabled(False)
        self.lineEdit_dimension_2.setEnabled(False)
        self.lineEdit_dimension_3.setEnabled(False)
        self.label_dimension_1.setText("")
        self.label_dimension_2.setText("")
        self.label_dimension_3.setText("")
