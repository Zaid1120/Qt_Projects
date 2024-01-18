import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog, QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6 import uic


class Viewer(QMainWindow):
    def __init__(self):
        super(Viewer, self).__init__()
        uic.loadUi("image_viewer.ui", self)
        self.show()
        self.current_file = "waiting.jpg"
        pixmap = QPixmap(self.current_file)
        pixmap = pixmap.scaled(self.width(), self.height())
        self.label.setPixmap(pixmap)
        self.label.setMinimumSize(1, 1)
        self.file_list = None
        self.file_counter = None
        self.actionOpen_Image.triggered.connect(self.open_image)
        self.actionOpen_Directory.triggered.connect(self.open_directory)
        self.pushButton_next.clicked.connect(self.next_image)
        self.pushButton_prev.clicked.connect(self.prev_image)

    def open_image(self):
        # options = QFileDialog.Options()  # change from pyqt5 to pyqt6
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "Image Files (*.png *.jpg)")

        if filename != "":
            self.current_file = filename
            pixmap = QPixmap(self.current_file)
            pixmap = pixmap.scaled(self.width(), self.height())
            self.label.setPixmap(pixmap)

    def open_directory(self):
        directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.file_list = [directory + "/" + f for f in os.listdir(directory) if f.endswith(".png") or
                          f.endswith(".jpg")]
        self.file_counter = 0
        self.current_file = self.file_list[self.file_counter]
        pixmap = QPixmap(self.current_file)
        pixmap.scaled(self.width(), self.height())
        self.label.setPixmap(pixmap)

    def resizeEvent(self, a0, QResizeEvent=None):  # this is a registered method
        try:
            pixmap = QPixmap(self.current_file)
        except:
            pixmap = QPixmap("waiting.jpg")
        pixmap = pixmap.scaled(self.width(), self.height())
        self.label.setPixmap(pixmap)
        self.label.resize(self.width(), self.height())

    def next_image(self):
        if self.file_list:  # Check if the file list is not empty
            self.file_counter = (self.file_counter + 1) % len(self.file_list)  # Increment and wrap around
            self.current_file = self.file_list[self.file_counter]
            pixmap = QPixmap(self.current_file)
            pixmap = pixmap.scaled(self.width(), self.height())
            self.label.setPixmap(pixmap)

    def prev_image(self):
        if self.file_list:  # Check if the file list is not empty
            self.file_counter = (self.file_counter - 1) % len(self.file_list)  # Decrement and wrap around
            self.current_file = self.file_list[self.file_counter]
            pixmap = QPixmap(self.current_file)
            pixmap = pixmap.scaled(self.width(), self.height())
            self.label.setPixmap(pixmap)


# trying out new way to execute app
def main():
    app = QApplication(sys.argv)
    window = Viewer()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
