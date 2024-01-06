from PyQt6 import QtCore, QtGui, QtWidgets
import requests
from decimal import Decimal, ROUND_HALF_UP


class ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 450)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 671, 61))
        font = QtGui.QFont()
        font.setFamily("Optima")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white")
        self.label.setGeometry(102, 15, 500, 55)
        # self.label.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 160, 581, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.base_comboBox = QtWidgets.QComboBox(parent=self.layoutWidget)
        double_validator = QtGui.QDoubleValidator(0.00, 1000000.00, 2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.base_comboBox.setFont(font)
        self.base_comboBox.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.base_comboBox.setObjectName("base_comboBox")
        self.base_comboBox.addItem("")
        self.base_comboBox.addItem("")
        self.base_comboBox.addItem("")
        self.base_comboBox.addItem("")
        self.base_comboBox.addItem("")

        self.verticalLayout.addWidget(self.base_comboBox)
        self.basevalue_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.basevalue_lineEdit.setFont(font)
        self.basevalue_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.basevalue_lineEdit.setPlaceholderText("")
        self.basevalue_lineEdit.setObjectName("basevalue_lineEdit")
        self.basevalue_lineEdit.setValidator(double_validator)
        self.verticalLayout.addWidget(self.basevalue_lineEdit)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white")
        self.label_2.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.currencyrate_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.currencyrate_lineEdit.setFont(font)
        self.currencyrate_lineEdit.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.currencyrate_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.currencyrate_lineEdit.setReadOnly(True)
        self.currencyrate_lineEdit.setPlaceholderText("")
        self.currencyrate_lineEdit.setObjectName("currencyrate_lineEdit")
        self.verticalLayout_2.addWidget(self.currencyrate_lineEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.target_comboBox = QtWidgets.QComboBox(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.target_comboBox.setFont(font)
        self.target_comboBox.setObjectName("target_comboBox")
        self.target_comboBox.addItem("")
        self.target_comboBox.addItem("")
        self.target_comboBox.addItem("")
        self.target_comboBox.addItem("")
        self.target_comboBox.addItem("")
        self.verticalLayout_3.addWidget(self.target_comboBox)
        self.targetvalue_lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.targetvalue_lineEdit.setFont(font)
        self.targetvalue_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.targetvalue_lineEdit.setReadOnly(True)
        self.targetvalue_lineEdit.setPlaceholderText("")
        self.targetvalue_lineEdit.setObjectName("targetvalue_lineEdit")
        self.verticalLayout_3.addWidget(self.targetvalue_lineEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        pixmap = QtGui.QPixmap("images/converter.png")
        self.background_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 631, 431))
        self.background_label.setText("")
        self.background_label.setObjectName("background_label")
        self.background_label.raise_()
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)
        self.layoutWidget.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # connecting elements to methods
        self.base_comboBox.currentIndexChanged.connect(self.update_conversion_rate)
        self.target_comboBox.currentIndexChanged.connect(self.update_conversion_rate)
        self.basevalue_lineEdit.editingFinished.connect(self.convert_currency)

        self.rate = None # initialising rate


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", " CURRENCY CONVERTER"))
        self.base_comboBox.setItemText(0, _translate("MainWindow", "EUR"))
        self.base_comboBox.setItemText(1, _translate("MainWindow", "USD"))
        self.base_comboBox.setItemText(2, _translate("MainWindow", "GBP"))
        self.base_comboBox.setItemText(3, _translate("MainWindow", "JPY"))
        self.base_comboBox.setItemText(4, _translate("MainWindow", "AED"))
        self.label_2.setText(_translate("MainWindow", "RATE"))
        self.target_comboBox.setItemText(0, _translate("MainWindow", "EUR"))
        self.target_comboBox.setItemText(1, _translate("MainWindow", "USD"))
        self.target_comboBox.setItemText(2, _translate("MainWindow", "GBP"))
        self.target_comboBox.setItemText(3, _translate("MainWindow", "JPY"))
        self.target_comboBox.setItemText(4, _translate("MainWindow", "AED"))


    def update_conversion_rate(self):
        api_key = ""  # add api here

        base_currency = self.base_comboBox.currentText()
        target_currency = self.target_comboBox.currentText()

        # check if both base and target currencies are selected
        if base_currency and target_currency:
            url = f"http://data.fixer.io/api/latest?access_key={api_key}&symbols={target_currency}&base={base_currency}"
            response = requests.get(url)
            data = response.json()

            if data.get("success", False):
                self.rate = float(data['rates'][target_currency])  # converting rate to float
                self.currencyrate_lineEdit.setText("{:.2f}".format(self.rate))

                # checking if there is a valid base amount before converting
                if self.basevalue_lineEdit.text():
                    self.convert_currency()
            else:
                QtWidgets.QMessageBox.critical(MainWindow, "API Error", "Failed to fetch currency data. Current API Plan only allows Euro as base currency.")
                self.rate = None
        else:
            self.rate = None


    def convert_currency(self):
        if self.rate is not None and self.basevalue_lineEdit.text():
            try:
                base_amount = Decimal(self.basevalue_lineEdit.text())
                rate = Decimal(str(self.rate))  # convert rate to decimal
                converted_amount = (base_amount * rate).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                self.targetvalue_lineEdit.setText(f"{converted_amount}")
            except (ValueError, InvalidOperation):
                QtWidgets.QMessageBox.warning(MainWindow, "Input Error", "Please enter a valid amount.")
        else:
            self.targetvalue_lineEdit.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
