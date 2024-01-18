import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QToolBar, QSpinBox, QComboBox, QFileDialog
from PyQt6.QtGui import QIcon, QFont, QAction
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog
from PyQt6.QtCore import Qt


class TextEditor(QMainWindow):
    def __init__(self):
        super(TextEditor, self).__init__()
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)
        self.showMaximized()
        self.setWindowTitle("Text Editor")
        self.fontSizeBox = QSpinBox()
        self.font_box = QComboBox(self)
        self.create_toolbar()
        self.editor.setFontPointSize(18)
        font = QFont('Arial', 18)
        self.editor.setFont(font)
        self.path = ""

    def create_toolbar(self):
        toolbar = QToolBar()

        # undo functionality
        undo_btn = QAction(QIcon("images/undo.png"), "undo", self)
        undo_btn.setShortcut("Ctrl+Z")
        undo_btn.triggered.connect(self.editor.undo)

        # redo functionality
        redo_btn = QAction(QIcon("images/redo.png"), "redo", self)
        redo_btn.setShortcut("Ctrl+Y")
        redo_btn.triggered.connect(self.editor.redo)

        # copy functionality
        copy_btn = QAction(QIcon("images/copy.png"), "copy", self)
        copy_btn.setShortcut("Ctrl+C")
        copy_btn.triggered.connect(self.editor.copy)

        # cut functionality
        cut_btn = QAction(QIcon("images/cut.png"), "cut", self)
        cut_btn.setShortcut("Ctrl+X")
        cut_btn.triggered.connect(self.editor.cut)

        # paste functionality
        paste_btn = QAction(QIcon("images/paste.png"), "paste", self)
        paste_btn.setShortcut("Ctrl+V")
        paste_btn.triggered.connect(self.editor.paste)

        # bold functionality
        bold_btn = QAction(QIcon("images/bold.png"), "bold", self)
        bold_btn.setShortcut("Ctrl+B")
        bold_btn.triggered.connect(self.toggle_bold)

        # underline functionality
        underline_btn = QAction(QIcon("images/underline.png"), "Underline", self)
        underline_btn.setShortcut("Ctrl+U")
        underline_btn.triggered.connect(self.toggle_underline)

        # italic functionality
        italic_btn = QAction(QIcon("images/italic.png"), "italic", self)
        italic_btn.setShortcut("Ctrl+I")
        italic_btn.triggered.connect(self.toggle_italic)

        # changing font size functionality
        self.fontSizeBox.setValue(18)
        self.fontSizeBox.valueChanged.connect(self.set_font_size)

        # changing font functionality
        fonts = ['Arial', 'Courier Std', 'Hellentic Typewriter Regular', 'Helvetica', 'Helvetica',
                 'Monospace', 'SansSerif', 'Times New Roman']
        self.font_box.addItems(fonts)
        self.font_box.activated.connect(self.set_font)

        # right align functionality
        right_align = QAction(QIcon("images/right-align.png"), "right align", self)
        right_align.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignmentFlag.AlignRight))

        # left align functionality
        left_align = QAction(QIcon("images/left-align.png"), "left align", self)
        left_align.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignmentFlag.AlignLeft))

        # centre align functionality
        centre_align = QAction(QIcon("images/centre-align.png"), "left centre", self)
        centre_align.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignmentFlag.AlignCenter))

        # save functionality
        save_btn = QAction(QIcon("images/save.png"), "save", self)
        save_btn.setShortcut("Ctrl+S")
        save_btn.triggered.connect(self.save_file)

        # # zoom in functionality
        # zoom_in_btn = QAction(QIcon("images/zoom-in.png"), "zoom-in", self)
        # zoom_in_btn.triggered.connect(lambda: self.editor.zoomIn(2))
        #
        # # zoom out functionality
        # zoom_out_btn = QAction(QIcon("images/zoom-out.png"), "zoom-out", self)
        # zoom_out_btn.triggered.connect(lambda: self.editor.zoomOut(2))

        # print functionality
        print_btn = QAction(QIcon("images/print.png"), "print", self)
        print_btn.setShortcut("Ctrl+P")
        print_btn.triggered.connect(self.print_document)

        # adding functionalities to toolbar
        toolbar.addAction(save_btn)
        toolbar.addSeparator()
        toolbar.addWidget(self.fontSizeBox)
        toolbar.addWidget(self.font_box)
        toolbar.addAction(bold_btn)
        toolbar.addAction(underline_btn)
        toolbar.addAction(italic_btn)
        toolbar.addSeparator()
        toolbar.addAction(undo_btn)
        toolbar.addAction(redo_btn)
        toolbar.addSeparator()
        toolbar.addAction(copy_btn)
        toolbar.addAction(cut_btn)
        toolbar.addAction(paste_btn)
        toolbar.addSeparator()
        toolbar.addAction(left_align)
        toolbar.addAction(centre_align)
        toolbar.addAction(right_align)
        toolbar.addSeparator()
        toolbar.addAction(print_btn)
        # toolbar.addSeparator()
        # toolbar.addAction(zoom_in_btn)
        # toolbar.addAction(zoom_out_btn)

        # adding toolbar itself
        self.addToolBar(toolbar)

    def set_font_size(self):
        value = self.fontSizeBox.value()
        current_font = self.editor.font()
        current_font.setPointSize(value)
        self.editor.setFont(current_font)
        self.editor.setFontPointSize(value)

    def set_font(self):
        font = self.font_box.currentText()
        size = self.fontSizeBox.value()  # Get the current value of the font size box
        new_font = QFont(font, size)  # Create a new QFont with the selected font and size
        self.editor.setFont(new_font)  # Set the new font for the editor
        self.editor.setFontPointSize(size)  # Ensure the font size is applied

    def toggle_bold(self):
        if self.editor.fontWeight() == QFont.Weight.Normal:
            self.editor.setFontWeight(QFont.Weight.Bold)
        else:
            self.editor.setFontWeight(QFont.Weight.Normal)

    def toggle_italic(self):
        self.editor.setFontItalic(not self.editor.fontItalic())

    def toggle_underline(self):
        self.editor.setFontUnderline(not self.editor.fontUnderline())

    def save_file(self):
        print(self.path)
        if self.path == '':
            self.file_save_as()
        text = self.editor.toPlainText()
        try:
            with open(self.path, 'w') as f:
                f.write(text)
                self.update_title()
        except Exception as e:
            print(e)

    def file_save_as(self):
        self.path, _ = QFileDialog.getSaveFileName(self, "Save file", "",
                                                   "text documents (*.text);Text documents (*.txt);All files (*.*)")
        if self.path == '':
            return
        text = self.editor.toPlainText()
        try:
            with open(path, 'w') as f:
                f.write(text)
                self.update_title()
        except Exception as e:
            print(e)

    def print_document(self):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec() == QPrintDialog.DialogCode.Accepted:
            self.editor.print_(printer)


app = QApplication(sys.argv)
window = TextEditor()
window.show()
sys.exit(app.exec())
