from PyQt5 import QtGui,QtWidgets,QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from package.classes import Stack, Queue, BubbleSortImg
import numpy as np
import cv2
import os
import time
import sys

name = 0
File = 0
Prev = 0
Next = Queue()
ImageStatus = Stack()
GreyScaleOri = None

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

        BackOrigin = QtWidgets.QAction('&Back to origin', self)
        BackOrigin.setShortcut('Ctrl+O')
        BackOrigin.setStatusTip('Back to original image')
        BackOrigin.triggered.connect(self.back_to_origin)

        GreyScale = QtWidgets.QAction('&Grayscale', self)
        GreyScale.setStatusTip('Grayscale image')
        GreyScale.triggered.connect(self.grayscale)

        Sharpen = QtWidgets.QAction('&Sharpen', self)
        Sharpen.setStatusTip('Sharpen image')
        Sharpen.triggered.connect(self.sharpen)

        Previous = QtWidgets.QAction('&Previous', self)
        Previous.setStatusTip('Previous image')
        Previous.triggered.connect(self.previousstate)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        fileMenu.addAction(openImage)

        imageMenu = mainMenu.addMenu('&Image')
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
    
        Sharp = QtWidgets.QAction(QtGui.QIcon('image/icon/sharpen.png'),'Sharpen', self)
        Sharp.triggered.connect(self.sharpen)
        self.toolBar = self.addToolBar("Sharpen")
        self.toolBar.addAction(Sharp)

        Blur = QtWidgets.QAction(QtGui.QIcon('image/icon/blur.png'),'Blur', self)
        Blur.triggered.connect(self.blur)
        self.toolBar = self.addToolBar("Blur")
        self.toolBar.addAction(Blur)

        DeNoising = QtWidgets.QAction(QtGui.QIcon('image/icon/denoising.png'),'DeNoising', self)
        DeNoising.triggered.connect(self.denoising)
        self.toolBar = self.addToolBar("DeNoising")
        self.toolBar.addAction(DeNoising)

        PreviousState = QtWidgets.QAction(QtGui.QIcon('image/icon/previousstate.png'),'PreviousState', self)
        PreviousState.triggered.connect(self.previousstate)
        self.toolBar = self.addToolBar("PreviousState")
        self.toolBar.addAction(PreviousState)

        NextState = QtWidgets.QAction(QtGui.QIcon('image/icon/nextstate.png'),'NextState', self)
        NextState.triggered.connect(self.nextstate)
        self.toolBar = self.addToolBar("NextState")
        self.toolBar.addAction(NextState)

        BackToOrigin = QtWidgets.QAction(QtGui.QIcon('image/icon/bto.png'),'BackToOrigin', self)
        BackToOrigin.triggered.connect(self.back_to_origin)
        self.toolBar = self.addToolBar("BackToOrigin")
        self.toolBar.addAction(BackToOrigin)

        Save = QtWidgets.QAction(QtGui.QIcon('image/icon/save.png'),'Save to album', self)
        Save.triggered.connect(self.save_to_album)
        self.toolBar = self.addToolBar("Save to album")
        self.toolBar.addAction(Save)

        PlayAlbum = QtWidgets.QAction(QtGui.QIcon('image/icon/playalbum.png'),'Play Album', self)
        PlayAlbum.triggered.connect(self.playalbum)
        self.toolBar = self.addToolBar("Play Album")
        self.toolBar.addAction(PlayAlbum)

        PlayAlbumSorted = QtWidgets.QAction(QtGui.QIcon('image/icon/playalbumsorted.png'),'Play Sorted Album', self)
        PlayAlbumSorted.triggered.connect(self.play_album_sorted)
        self.toolBar = self.addToolBar("Play Sorted Album")
        self.toolBar.addAction(PlayAlbumSorted)

        self.show()
    
    def imageTable(self):
        self.imageT = QLabel(self)
        pixmap1 = QPixmap('image/imageT')
        self.pixmap = pixmap1.scaled(self.width(),self.height())
        self.imageT.setPixmap(self.pixmap)
        self.setCentralWidget(self.imageT)
        
    def open_image(self):
        global name
        global File
        global ImageStatus
        global Next
        name = QtWidgets.QFileDialog.getOpenFileName(self,'Open File')
        File = name[0]
        img_file = cv2.imread(File)
        Next.content = []
        ImageStatus.content = []
        ImageStatus.push(img_file)
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
        global Prev
        global Next
        global File
        global ImageStatus
        global GreyScaleOri
        if Prev == 1:
            Prev = 0
            Next.content = []
        if File != 0:
            img_file = ImageStatus.pop_status()
            if img_file.ndim == 3:
                GreyScaleOri = img_file
                img_file = cv2.cvtColor(img_file,cv2.COLOR_BGR2GRAY)
            elif img_file.ndim == 2:
                img_file = GreyScaleOri
            ImageStatus.push(img_file)
            cv2.imwrite('image/template/template.jpg',img_file)
            self.imageTable()
            File2 = 'image/template/template.jpg'
            pixmap1 = QPixmap(File2)
            self.pixmap = pixmap1.scaled(self.width(),self.height(),QtCore.Qt.KeepAspectRatio)
            self.imageT.setPixmap(self.pixmap)
            self.imageT.setMinimumSize(400,300)
            self.setCentralWidget(self.imageT)
        else:
            choice = QtWidgets.QMessageBox.question(self, 'Error!',
                                                "Open an image?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if choice == QtWidgets.QMessageBox.Yes:
                self.open_image()
            else:
                pass

    def sharpen(self):
        global Next
        global Prev
        global File
        global ImageStatus
        if Prev == 1:
            Prev = 0
            Next.content = []
        if File != 0:
            img_file = ImageStatus.pop_status()
            kernel_sharpening = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
            img_file = cv2.filter2D(img_file, -1, kernel_sharpening)
            ImageStatus.push(img_file)
            cv2.imwrite('image/template/template.jpg',img_file)
            self.imageTable()
            File2 = 'image/template/template.jpg'
            pixmap1 = QPixmap(File2)
            self.pixmap = pixmap1.scaled(self.width(),self.height(),QtCore.Qt.KeepAspectRatio)
            self.imageT.setPixmap(self.pixmap)
            self.imageT.setMinimumSize(400,300)
            self.setCentralWidget(self.imageT)
        else:
            choice = QtWidgets.QMessageBox.question(self, 'Error!',
                                                "Open an image?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if choice == QtWidgets.QMessageBox.Yes:
                self.open_image()
            else:
                pass

    def blur(self):
        global Next
        global Prev
        global File
        global ImageStatus
        if Prev == 1:
            Prev = 0
            Next.content = []
        if File != 0:
            img_file = ImageStatus.pop_status()
            kernel_3x3 = np.ones((3,3),np.float32)/9
            img_file = cv2.filter2D(img_file, -1, kernel_3x3)
            ImageStatus.push(img_file)
            cv2.imwrite('image/template/template.jpg',img_file)
            self.imageTable()
            File2 = 'image/template/template.jpg'
            pixmap1 = QPixmap(File2)
            self.pixmap = pixmap1.scaled(self.width(),self.height(),QtCore.Qt.KeepAspectRatio)
            self.imageT.setPixmap(self.pixmap)
            self.imageT.setMinimumSize(400,300)
            self.setCentralWidget(self.imageT)
        else:
            choice = QtWidgets.QMessageBox.question(self, 'Error!',
                                                "Open an image?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if choice == QtWidgets.QMessageBox.Yes:
                self.open_image()
            else:
                pass
    
    def denoising(self):
        global Next
        global Prev
        global File
        global ImageStatus
        if Prev == 1:
            Prev = 0
            Next.content = []
        if File != 0:
            img_file = ImageStatus.pop_status()
            if img_file.ndim == 3:
                img_file = cv2.fastNlMeansDenoisingColored(img_file, None, 6, 6, 7, 21)
            elif img_file.ndim == 2:
                img_file = cv2.fastNlMeansDenoising(img_file, None, 9,13)
            ImageStatus.push(img_file)
            cv2.imwrite('image/template/template.jpg',img_file)
            self.imageTable()
            File2 = 'image/template/template.jpg'
            pixmap1 = QPixmap(File2)
            self.pixmap = pixmap1.scaled(self.width(),self.height(),QtCore.Qt.KeepAspectRatio)
            self.imageT.setPixmap(self.pixmap)
            self.imageT.setMinimumSize(400,300)
            self.setCentralWidget(self.imageT)
        else:
            choice = QtWidgets.QMessageBox.question(self, 'Error!',
                                                "Open an image?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if choice == QtWidgets.QMessageBox.Yes:
                self.open_image()
            else:
                pass

    def previousstate(self):
        global Prev
        global File
        global Next
        global ImageStatus
        if Prev == 0:
            Prev = 1
        if File != 0:
            try:
                if len(ImageStatus.content) == 1:
                    img_file = ImageStatus.pop_status()
                else:
                    img_file = ImageStatus.pop()
                    Next.inqueue(img_file)
                    img_file = ImageStatus.pop_status()
            except:
                pass
            cv2.imwrite('image/template/template.jpg',img_file)
            self.imageTable()
            File2 = 'image/template/template.jpg'
            pixmap1 = QPixmap(File2)
            self.pixmap = pixmap1.scaled(self.width(),self.height(),QtCore.Qt.KeepAspectRatio)
            self.imageT.setPixmap(self.pixmap)
            self.imageT.setMinimumSize(400,300)
            self.setCentralWidget(self.imageT)
        else:
            choice = QtWidgets.QMessageBox.question(self, 'Error!',
                                                "Open an image?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if choice == QtWidgets.QMessageBox.Yes:
                self.open_image()
            else:
                pass

    def nextstate(self):
        global Prev
        global File
        global Next
        global ImageStatus
        if Prev == 1:
            if File != 0:
                try:
                    if len(Next.content) == 0:
                        img_file = ImageStatus.pop_status()
                    else:
                        img_file = Next.dequeue()
                        ImageStatus.push(img_file)
                except:
                    pass
                cv2.imwrite('image/template/template.jpg',img_file)
                self.imageTable()
                File2 = 'image/template/template.jpg'
                pixmap1 = QPixmap(File2)
                self.pixmap = pixmap1.scaled(self.width(),self.height(),QtCore.Qt.KeepAspectRatio)
                self.imageT.setPixmap(self.pixmap)
                self.imageT.setMinimumSize(400,300)
                self.setCentralWidget(self.imageT)
            else:
                choice = QtWidgets.QMessageBox.question(self, 'Error!',
                                                    "Open an image?",
                                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                if choice == QtWidgets.QMessageBox.Yes:
                    self.open_image()
                else:
                    pass
        else:
            pass

    def back_to_origin(self):
        global Prev
        global File
        global ImageStatus
        if Prev == 1:
            Prev = 0
        if File != 0:
            img_file = cv2.imread(File)
            ImageStatus.push(img_file)
            self.imageTable()
            pixmap1 = QPixmap(File)
            self.pixmap = pixmap1.scaled(self.width(),self.height(),QtCore.Qt.KeepAspectRatio)
            self.imageT.setPixmap(self.pixmap)
            self.imageT.setMinimumSize(400,300)
            self.setCentralWidget(self.imageT)
        else:
            choice = QtWidgets.QMessageBox.question(self, 'Error!',
                                                "Open an image?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if choice == QtWidgets.QMessageBox.Yes:
                self.open_image()
            else:
                pass

    def save_to_album(self):
        global File
        if File != 0:
            path = os.path.abspath('')+'/image/album/'
            fileNum = 0
            for item in os.listdir(path):
                fileNum = fileNum+1
            File = 'image/template/template.jpg'
            self.imageTable()
            pixmap1 = QPixmap(File)
            img_file = cv2.imread(File)
            fileNum = int(os.listdir(path)[fileNum-1][-5::-1])+1
            cv2.imwrite(path+str(fileNum)+'.jpg',img_file)
            self.pixmap = pixmap1.scaled(self.width(),self.height(),QtCore.Qt.KeepAspectRatio)
            self.imageT.setPixmap(self.pixmap)
            self.imageT.setMinimumSize(400,300)
            self.setCentralWidget(self.imageT)
        else:
            choice = QtWidgets.QMessageBox.question(self, 'Error!',
                                                "Open an image?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if choice == QtWidgets.QMessageBox.Yes:
                self.open_image()
            else:
                pass
    
    def playalbum(self):
        path = os.path.abspath('')+'/image/album/'
        self.imageTable()
        QApplication.processEvents()
        for item in os.listdir(path):
            img_file = cv2.imread(path+item)
            cv2.imwrite('image/template/template.jpg',img_file)
            File2 = 'image/template/template.jpg'
            pixmap1 = QPixmap(File2)
            self.pixmap = pixmap1.scaled(self.width(),self.height(),QtCore.Qt.KeepAspectRatio)
            self.imageT.setPixmap(self.pixmap)
            self.imageT.setMinimumSize(400,300)
            self.setCentralWidget(self.imageT)
            QApplication.processEvents()
            time.sleep(1)

    def play_album_sorted(self):
        path = os.path.abspath('')+'/image/album/'
        inputlist = os.listdir(path)
        imglist = BubbleSortImg(inputlist)
        self.imageTable()
        QApplication.processEvents()
        for item in imglist:
            img_file = item
            cv2.imwrite('image/template/template.jpg',img_file)
            File2 = 'image/template/template.jpg'
            pixmap1 = QPixmap(File2)
            self.pixmap = pixmap1.scaled(self.width(),self.height(),QtCore.Qt.KeepAspectRatio)
            self.imageT.setPixmap(self.pixmap)
            self.imageT.setMinimumSize(400,300)
            self.setCentralWidget(self.imageT)
            QApplication.processEvents()
            time.sleep(1)

def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()