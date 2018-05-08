import sys
from PyQt5 import QtGui,QtWidgets,QtCore
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QFileDialog, QLabel
import cv2
class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle('QT5')
        self.setWindowIcon(QtGui.QIcon('Icon.PNG'))
        extractAction = QtWidgets.QAction('&Quit',self)
        extractAction.setShortcut('Ctrl+Q')
        extractAction.setStatusTip('Quit the App')
        extractAction.triggered.connect(self.close_application)

        openImageT = QtWidgets.QAction('&ImageTable',self)
        openImageT.setShortcut('Ctrl+W')
        openImageT.setStatusTip('Open Image Table')
        openImageT.triggered.connect(self.imageTable)

        openImage = QtWidgets.QAction('&Open Image',self)
        openImage.setShortcut('Ctrl+I')
        openImage.setStatusTip('Open Image')
        openImage.triggered.connect(self.open_image)

        self.statusBar()
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        fileMenu.addAction(openImage)

        imageTMenu = mainMenu.addMenu('&ImageTable')
        imageTMenu.addAction(openImageT)

        self.home()

    def home(self):
        extractAction = QtWidgets.QAction(QtGui.QIcon('Icon.PNG'),'Flee the Scene', self)
        extractAction.triggered.connect(self.close_application)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)
        checkBox = QtWidgets.QCheckBox('Enlarge Window', self)
        checkBox.move(100,25)
        checkBox.stateChanged.connect(self.enlarge_window)

        self.show()

    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50,50,1000,600)
        else:
            self.setGeometry(50,50,500,300)
    

    def imageTable(self):
        self.imageT = QLabel(self)
        pixmap1 = QPixmap('doge')
        self.pixmap = pixmap1.scaled(self.width(),self.height())
        self.imageT.setPixmap(self.pixmap)
        self.imageT.setMinimumSize(400,300)
        self.setCentralWidget(self.imageT)
        #self.imageT.setPixmap(QPixmap('doge'))
        #self.setCentralWidget(self.imageT)
        
        
    def open_image(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self,'Open File')
        File = name[0]
        self.imageTable()
        #self.imageT.setPixmap(QPixmap(File))
        pixmap1 = QPixmap(File)
        self.pixmap = pixmap1.scaled(self.width(),self.height())
        self.imageT.setPixmap(self.pixmap)
        self.imageT.setMinimumSize(400,300)
        self.setCentralWidget(self.imageT)

    def close_application(self):
        choice = QtWidgets.QMessageBox.question(self, 'Extract!',
                                                "Quit ?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            sys.exit()
        else:
            pass

def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()



