import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QPalette, QColor, Qt
from PySide2.QtWidgets import QMainWindow, QApplication, QInputDialog, QWidget, QPushButton, QLabel, QFormLayout, \
    QLineEdit, QSizePolicy
import Main

# -------------------------------------------------------------------------------------------------------------------- #
class Ui_Application(object):
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
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), Main.run)
        QtCore.QMetaObject.connectSlotsByName(Application)

    # -------------------------------------------------------------------------------------------------------------------- #
    def retranslateUi(self, Application):
        Application.setWindowTitle(
            QtWidgets.QApplication.translate("Application", "Application", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Application", "Generate Password", None, -1))


# -------------------------------------------------------------------------------------------------------------------- #
def main():
    app = QtWidgets.QApplication(sys.argv)

    # Change palette to allow for for dark theme
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
