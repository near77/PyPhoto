import sys
from PyQt5 import QtGui,QtWidgets,QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2
import os

name = 0
File = 0

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,850,650)
        self.setWindowTitle('QT5')
        self.setWindowIcon(QtGui.QIcon('icon/pythonimg.png'))

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

        GreyScale = QtWidgets.QAction('&Grayscale', self)
        GreyScale.setShortcut('Ctrl+G')
        GreyScale.setStatusTip('Grayscale image')
        GreyScale.triggered.connect(self.grayscale)

        BackOrigin = QtWidgets.QAction('&Back to origin', self)
        BackOrigin.setShortcut('Ctrl+O')
        BackOrigin.setStatusTip('Back to original image')
        BackOrigin.triggered.connect(self.back_to_origin)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        imageMenu = mainMenu.addMenu('&Image')
        imageMenu.addAction(openImage)
        imageMenu.addAction(GreyScale)
        imageMenu.addAction(BackOrigin)

        self.home()

    def home(self):
        extractAction = QtWidgets.QAction(QtGui.QIcon('image/icon/logout.png'),'Flee the Scene', self)
        extractAction.triggered.connect(self.close_application)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)

        Grayscale = QtWidgets.QAction(QtGui.QIcon('image/icon/pythonimg.png'),'Grayscale', self)
        Grayscale.triggered.connect(self.grayscale)
        self.toolBar = self.addToolBar("Grayscale")
        self.toolBar.addAction(Grayscale)

        BackToOrigin = QtWidgets.QAction(QtGui.QIcon('image/icon/bto.png'),'BackToOrigin', self)
        BackToOrigin.triggered.connect(self.back_to_origin)
        self.toolBar = self.addToolBar("BackToOrigin")
        self.toolBar.addAction(BackToOrigin)

        Save = QtWidgets.QAction(QtGui.QIcon('image/icon/save.png'),'Save to album', self)
        Save.triggered.connect(self.save_to_album)
        self.toolBar = self.addToolBar("Save to album")
        self.toolBar.addAction(Save)

        
        self.show()
    
    
    def imageTable(self):
        self.imageT = QLabel(self)
        pixmap1 = QPixmap('image/imageT')
        self.pixmap = pixmap1.scaled(self.width(),self.height())
        self.imageT.setPixmap(self.pixmap)
        self.setCentralWidget(self.imageT)
    
        
        
    def open_image(self):
        global name 
        name = QtWidgets.QFileDialog.getOpenFileName(self,'Open File')
        global File
        File = name[0]
        img_file = cv2.imread(File)
        cv2.imwrite('image/template/template.jpg',img_file)
        self.imageTable()
        pixmap1 = QPixmap(File)
        self.pixmap = pixmap1.scaled(self.width(),self.height(),QtCore.Qt.KeepAspectRatio)
        self.imageT.setPixmap(self.pixmap)
        self.setCentralWidget(self.imageT)

    def close_application(self):
        choice = QtWidgets.QMessageBox.question(self, 'Extract!',
                                                "Quit ?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            sys.exit()
        else:
            pass
    
    def grayscale(self):
        global File
        img_file = cv2.imread(File, 0)
        cv2.imwrite('image/template/template.jpg',img_file)
        self.imageTable()
        File2 = 'image/template/template.jpg'
        pixmap1 = QPixmap(File2)
        self.pixmap = pixmap1.scaled(self.width(),self.height(),QtCore.Qt.KeepAspectRatio)
        self.imageT.setPixmap(self.pixmap)
        self.imageT.setMinimumSize(400,300)
        self.setCentralWidget(self.imageT)

    def sharp(self):
        global File
        img_file = cv2.imread(File)
        #sharp function
        cv2.imwrite('image/template/template.jpg',img_file)
        self.imageTable()
        File2 = 'image/template/template.jpg'
        pixmap1 = QPixmap(File2)
        self.pixmap = pixmap1.scaled(self.width(),self.height(),QtCore.Qt.KeepAspectRatio)
        self.imageT.setPixmap(self.pixmap)
        self.imageT.setMinimumSize(400,300)
        self.setCentralWidget(self.imageT)

    def back_to_origin(self):
        global File
        self.imageTable()
        pixmap1 = QPixmap(File)
        self.pixmap = pixmap1.scaled(self.width(),self.height(),QtCore.Qt.KeepAspectRatio)
        self.imageT.setPixmap(self.pixmap)
        self.imageT.setMinimumSize(400,300)
        self.setCentralWidget(self.imageT)

    def save_to_album(self):
        path = os.path.abspath('')+'/image/album/'
        fileNum = 0
        for item in os.listdir(path):
            fileNum = fileNum+1
        File = 'image/template/template.jpg'
        self.imageTable()
        pixmap1 = QPixmap(File)
        img_file = cv2.imread(File)
        cv2.imwrite(path+str(fileNum)+'.jpg',img_file)
        self.pixmap = pixmap1.scaled(self.width(),self.height(),QtCore.Qt.KeepAspectRatio)
        self.imageT.setPixmap(self.pixmap)
        self.imageT.setMinimumSize(400,300)
        self.setCentralWidget(self.imageT)

def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()