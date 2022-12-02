from PyQt5.QtWidgets import *
from view import *


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton_area.clicked.connect(lambda: self.area())
        self.pushButton_perim.clicked.connect(lambda: self.perim())
        self.comboBox_shapes.currentIndexChanged.connect(lambda: self.combobox_update())

    def area(self):
        return

    def perim(self):
        return

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
            case 5:
                self.reset_input()
                self.lineEdit_dimension_1.setEnabled(True)
                self.label_dimension_1.setText("Height")
                self.lineEdit_dimension_2.setEnabled(True)
                self.label_dimension_2.setText("Width")
            case _:
                self.reset_input()

    def reset_input(self):
        self.lineEdit_dimension_1.setEnabled(False)
        self.lineEdit_dimension_2.setEnabled(False)
        self.lineEdit_dimension_3.setEnabled(False)
        self.label_dimension_1.setText("")
        self.label_dimension_2.setText("")
        self.label_dimension_3.setText("")

