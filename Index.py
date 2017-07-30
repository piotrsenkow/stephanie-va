from Stephanie.boot import Boot
from PyQt4 import QtGui
import sys

class Window (QtGui.QMainWindow):

    def __init__(self):
        super(Window,self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(50, 50, 300, 100)
        self.setWindowTitle("Stephanie")
        self.center()

        button=  QtGui.QPushButton('Start Program', self)
        button.resize(button.sizeHint())
        button.clicked.connect(self.StartProgram)
        button.move(30,50)

        button2 = QtGui.QPushButton('Exit Program', self)
        button2.clicked.connect(self.ExitApp)
        button2.move(160,50)

        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        button.setToolTip(('Press here to start <b>STEPHANIE</b>'))
        button2.setToolTip('Click here to <b>exit</b>')
        self.show()

    def center(self):
        WindowGeometry = self.frameGeometry()
        ScreenResolution = QtGui.QDesktopWidget().availableGeometry().center()
        WindowGeometry.moveCenter(ScreenResolution)
        self.move(WindowGeometry.topLeft())

    def StartProgram(self):
        b = Boot()
        b.initiate()

    def ExitApp(self):
        sys.exit()


def main():
        app= QtGui.QApplication(sys.argv)
        w=Window()
        app.exec_()
if __name__ == '__main__':
    main()



