import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QPalette, QColor, Qt
from PySide2.QtWidgets import QMainWindow, QApplication, QInputDialog, QWidget, QPushButton, QLabel, QFormLayout, \
    QLineEdit, QSizePolicy
import Main

# -------------------------------------------------------------------------------------------------------------------- #
class Ui_Application(object):
# -------------------------------------------------------------------------------------------------------------------- #
    def getPin(self):
        self.inputWindow = inputDialog()
        pin = self.inputWindow.getint("Enter your pin: ")
        Main.run(pin)

# -------------------------------------------------------------------------------------------------------------------- #
    def setupUi(self, Application):
        Application.setObjectName("Application")
        Application.resize(200, 100)  # Default size
        self.gridLayout = QtWidgets.QGridLayout(Application)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(Application)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.retranslateUi(Application)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.getPin)
        QtCore.QMetaObject.connectSlotsByName(Application)

# -------------------------------------------------------------------------------------------------------------------- #
    def retranslateUi(self, Application):
        Application.setWindowTitle(
        QtWidgets.QApplication.translate("Application", "Application", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Application", "Generate Password", None, -1))


# -------------------------------------------------------------------------------------------------------------------- #
class inputDialog(QWidget):
    def __init__(self, parent=None):
        super(inputDialog, self).__init__(parent)

        infoList = ['', '', '']

        layout = QFormLayout()
        self.btn = QPushButton("Choose from list")
        self.btn.clicked.connect(self.getItem)

        self.le = QLineEdit()
        layout.addRow(self.btn, self.le)
        self.btn1 = QPushButton("Get name")
        self.btn1.clicked.connect(self.gettext)

        self.le1 = QLineEdit()
        layout.addRow(self.btn1, self.le1)
        self.btn2 = QPushButton("Enter an integer")
        self.btn2.clicked.connect(self.getint)

        self.le2 = QLineEdit()
        layout.addRow(self.btn2, self.le2)
        self.setLayout(layout)
        self.setWindowTitle("Title")

# -------------------------------------------------------------------------------------------------------------------- #
    def getItem(self, prompt="Enter an option: "):
        items = ("P1", "P2", "P3", "P4")

        item, ok = QInputDialog.getItem(self, prompt,
                                        "List of Items", items, 0, False)

        if ok and item:
            self.le.setText(item)
            return str(item)

# -------------------------------------------------------------------------------------------------------------------- #
    def gettext(self, prompt="Enter text: "):
        text, ok = QInputDialog.getText(self, 'Text Input Dialog', prompt)

        if ok:
            self.le1.setText(str(text))
            return str(text)

# -------------------------------------------------------------------------------------------------------------------- #
    def getint(self, prompt="Enter a number: "):
        num, ok = QInputDialog.getInt(self, "Integer input dialog", prompt)

        if ok:
            self.le2.setText(str(num))
            return int(num)


# -------------------------------------------------------------------------------------------------------------------- #
def main():
    app = QtWidgets.QApplication(sys.argv)

    # Change palette to allow for for dark theme
    # Breeze, Oxygen, QtCurve. Windows, Fusion
    app.setStyle('Fusion')
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)

    Application = QtWidgets.QWidget()
    ui = Ui_Application()
    ui.setupUi(Application)
    Application.show()
    sys.exit(app.exec_())


# -------------------------------------------------------------------------------------------------------------------- #
main()
