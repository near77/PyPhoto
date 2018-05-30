import sys
from PyQt5 import QtGui,QtWidgets,QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2

name = 0
File = 0

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,1000,600)
        self.setWindowTitle('QT5')
        self.setWindowIcon(QtGui.QIcon('pythonimg.png'))

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

        GreyScale = QtWidgets.QAction('&Grey Scale', self)
        GreyScale.setShortcut('Ctrl+G')
        GreyScale.setStatusTip('Grey scale image')
        GreyScale.triggered.connect(self.grey_scale)

        BackOrigin = QtWidgets.QAction('&Back to origin', self)
        BackOrigin.setShortcut('Ctrl+O')
        BackOrigin.setStatusTip('Back to original image')
        BackOrigin.triggered.connect(self.back_to_origin)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        fileMenu.addAction(openImage)
        fileMenu.addAction(GreyScale)
        fileMenu.addAction(BackOrigin)

        imageTMenu = mainMenu.addMenu('&ImageTable')
        imageTMenu.addAction(openImageT)

        self.home()

    def home(self):
        extractAction = QtWidgets.QAction(QtGui.QIcon('image/pythonimg.png'),'Flee the Scene', self)
        extractAction.triggered.connect(self.close_application)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)
        '''
        checkBox = QtWidgets.QCheckBox('Enlarge', self)
        checkBox.move(100,25)
        checkBox.stateChanged.connect(self.enlarge_window)
        '''
        self.show()

    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50,50,1000,600)
        else:
            self.setGeometry(50,50,500,300)
    
    
    def imageTable(self):
        self.imageT = QLabel(self)
        pixmap1 = QPixmap('image/doge')
        self.pixmap = pixmap1.scaled(self.width(),self.height())
        self.imageT.setPixmap(self.pixmap)
        self.imageT.setMinimumSize(400,300)
        self.setCentralWidget(self.imageT)
    
        
        
    def open_image(self):
        global name 
        name = QtWidgets.QFileDialog.getOpenFileName(self,'Open File')
        global File
        File = name[0]
        self.imageTable()
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
    
    def grey_scale(self):
        global File
        img_file = cv2.imread(File, 0)
        cv2.imwrite('image/template/template.jpg',img_file)
        self.imageTable()
        File2 = 'image/template/template.jpg'
        pixmap1 = QPixmap(File2)
        self.pixmap = pixmap1.scaled(self.width(),self.height())
        self.imageT.setPixmap(self.pixmap)
        self.imageT.setMinimumSize(400,300)
        self.setCentralWidget(self.imageT)

    def back_to_origin(self):
        global File
        self.imageTable()
        pixmap1 = QPixmap(File)
        self.pixmap = pixmap1.scaled(self.width(),self.height())
        self.imageT.setPixmap(self.pixmap)
        self.imageT.setMinimumSize(400,300)
        self.setCentralWidget(self.imageT)

def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()