import sys
from PySide import QtGui

class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example,self).__init__()

        self.initUI()

    def initUI(self):
        self.statusBar().showMessage("Ready")
        self.setGeometry(300,300,200,150)
        self.seWindowTitle("Status_Bar")
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex= Example()
    sys.exit(app_exec())


if __name__ == "__main__":
    main()
    
