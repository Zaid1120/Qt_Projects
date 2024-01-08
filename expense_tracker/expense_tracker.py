import sys
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QAction, QPainter
from PySide6.QtWidgets import QApplication, QHeaderView, QHBoxLayout, QLabel, QLineEdit, \
    QMainWindow, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QMessageBox
from PySide6.QtCharts import QChartView, QPieSeries, QChart


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Expense Tracker")

        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl + Q")
        exit_action.triggered.connect(self.exit_app)
        self.file_menu.addAction(exit_action)

        self.main_widget = Widget()
        self.setCentralWidget(self.main_widget)

    @Slot()
    def exit_app(self):
        QApplication.quit()


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.items = 0
        # dummy data
        self.dummy_data = {"Food": 20,
                           "Computer": 1000,
                           "Rent": 1000,
                           "Internet": 50,
                           "Energy": 100}
        # left side
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Item", "Cost"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # right side
        self.description = QLineEdit()
        self.price = QLineEdit()
        self.add = QPushButton("Add")
        self.clear = QPushButton("Clear")
        self.quit = QPushButton("Quit")
        self.plot = QPushButton("Plot")

        # chat window
        self.chart_view = QChartView()
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        # layouts
        self.right = QVBoxLayout()
        self.layout = QHBoxLayout()

        # adding table and right side to overall layout
        self.layout.addWidget(self.table)
        self.layout.addLayout(self.right)

        self.right.addWidget(QLabel("Item"))
        self.right.addWidget(self.description)
        self.right.addWidget(QLabel("Cost"))
        self.right.addWidget(self.price)
        self.right.addWidget(self.add)
        self.right.addWidget(self.plot)
        self.right.addWidget(self.chart_view)
        self.right.addWidget(self.clear)
        self.right.addWidget(self.quit)

        # Set QWidget layout
        self.setLayout(self.layout)

        # connecting signals and slots
        self.add.clicked.connect(self.add_element)
        self.quit.clicked.connect(self.quit_application)
        self.plot.clicked.connect(self.plot_data)
        self.clear.clicked.connect(self.clear_table_and_plot)
        self.description.textChanged[str].connect(self.check_disable)
        self.price.textChanged[str].connect(self.check_disable)

        # the add button should be disabled at first
        self.add.setEnabled(False)

        # put dummy data in table
        self.fill_table()

    @Slot()
    def check_disable(self):
        if not self.description.text() or not self.price.text():
            self.add.setEnabled(False)
        else:
            self.add.setEnabled(True)

    @Slot()
    def add_element(self):
        desc = self.description.text()
        price = self.price.text()
        try:
            price_item = QTableWidgetItem(f"{float(price):.2f}")
            price_item.setTextAlignment(Qt.AlignRight)

            self.table.insertRow(self.items)
            description_item = QTableWidgetItem(desc)

            self.table.setItem(self.items, 0, description_item)
            self.table.setItem(self.items, 1, price_item)

            self.description.setText("")
            self.price.setText("")

            self.items += 1
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Invalid input! Please enter a price!")

    @Slot()
    def plot_data(self):
        # getting table info
        pi_series = QPieSeries()
        for i in range(self.table.rowCount()):
            text = self.table.item(i, 0).text()
            number = float(self.table.item(i, 1).text())
            pi_series.append(text, number)

        chart = QChart()
        chart.addSeries(pi_series)
        chart.legend().setAlignment(Qt.AlignLeft)
        self.chart_view.setChart(chart)

    def fill_table(self, data=None):
        if not data:
            data = self.dummy_data

        for item_object, price in data.items():
            item = QTableWidgetItem(item_object)
            item_cost = QTableWidgetItem(f"{price:.2f}")
            item_cost.setTextAlignment(Qt.AlignmentFlag.AlignRight)
            self.table.insertRow(self.items)
            self.table.setItem(self.items, 0, item)
            self.table.setItem(self.items, 1, item_cost)
            self.items += 1  # making sure new object is added to end of table, not top

    @Slot()
    def quit_application(self):
        QApplication.quit()

    @Slot()
    def clear_table_and_plot(self):
        # reset table
        self.table.setRowCount(0)
        self.items = 0
        # reset chart
        empty_chart = QChart()
        self.chart_view.setChart(empty_chart)


app = QApplication(sys.argv)
window = MainWindow()
window.resize(1000, 700)
window.show()
sys.exit(app.exec())
