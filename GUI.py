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
        self.getPin = QMainWindow()
        self.getPin.resize(1000, 500)
        self.getPin.setWindowTitle("Insert Pin")
        self.label = QtWidgets.QLabel(self.getPin)
        self.label.setText(Main.run(pin))
        self.label.setStyleSheet("QLabel {font: 15pt Times New Roman}")
        self.label.adjustSize()
        self.getPin.show()

# -------------------------------------------------------------------------------------------------------------------- #
    def instructions(self):
        self.readMe = QMainWindow()
        self.readMe.resize(1000, 500)
        self.readMe.setWindowTitle("Instructions")
        self.label = QtWidgets.QLabel(self.readMe)
        self.label.setText("For first time use:\n" 
                           "1) Ensure desired website is most recent tab prior to clicking generate password.\n"
                           "2) Click 'Generate Password'.\n"
                           "3) Set unique pin when prompted.\n"
                           "4) Camera application will pop up. Look towards camera and press space to store picture of yourself, this will be used for generation and authentication.\n"
                           "5) Your unique password for desired website will be copied to clipboard. Set this as your new password for desired website.\n\n"
                           "For subsequent use:\n"
                           "1) Ensure desired website is most recent tab prior to clicking generate password.\n"
                           "2) Click 'Generate Password'\n"
                           "3) Enter same pin as inputted during setup\n"
                           "4) Look towards camera and password will be generated and pasted to your clipboard\n"
                           "5) Paste password into website.")
        self.label.setStyleSheet("QLabel {font: 15pt Times New Roman}")
        self.label.adjustSize()
        self.readMe.show()

# -------------------------------------------------------------------------------------------------------------------- #
    def setupUi(self, Application):

        Application.setObjectName("Application")
        Application.resize(1000, 500)  # Default size
        self.gridLayout = QtWidgets.QGridLayout(Application)
        self.gridLayout.setObjectName("gridLayout")

        # Top Label
        self.label = QtWidgets.QLabel(Application)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet("QLabel {font: 20pt Times New Roman}")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        # Line for visual separation
        self.line = QtWidgets.QFrame(Application)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)

        # Generate Button
        self.pushButton = QtWidgets.QPushButton(Application)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet('QPushButton {font: 20pt Times New Roman}')
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.pushButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Read Me
        self.pushButton_2 = QtWidgets.QPushButton(Application)
        self.pushButton_2.setObjectName("pushButton")
        self.pushButton_2.setStyleSheet('QPushButton {font: 20pt Times New Roman}')
        self.gridLayout.addWidget(self.pushButton_2, 3, 0, 1, 1)
        self.pushButton_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.retranslateUi(Application)

        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.getPin)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.instructions)
        QtCore.QMetaObject.connectSlotsByName(Application)

# -------------------------------------------------------------------------------------------------------------------- #
    def retranslateUi(self, Application):
        Application.setWindowTitle(
        QtWidgets.QApplication.translate("Application", "Unique Password Generator", None, -1))
        # Top Label
        self.label.setText(QtWidgets.QApplication.translate("Application", "Unique Password Generator", None, -1))
        # Generate Button
        self.pushButton.setText(QtWidgets.QApplication.translate("Application", "Generate Password", None, -1))
        # Instructions Button
        self.pushButton_2.setText(QtWidgets.QApplication.translate("Application", "Instructions", None, -1))


# -------------------------------------------------------------------------------------------------------------------- #
class inputDialog(QWidget):
    def __init__(self, parent=None):
        super(inputDialog, self).__init__(parent)

        infoList = ['', '', '']

        layout = QFormLayout()

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
