def showFilenamesList():
    try:
        extensions = ['.jpg','.jpeg', '.png']
        chooseWorkdir()
        filenames = filter(os.listdir(workdir), extensions)
        file_list.clear()
        for filename in filenames:
            file_list.addItem(filename)
        self.filename = None
        self.image = None
        self.edit_image = None
    except:
        pass

def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result

def showChosenImage():
    if file_list.currentRow() >= 0:
        filename = file_list.currentItem().text()
        workimage.loadImage(filename)
        image_path = os.path.join(workdir,
        workimage.filename)
        workimage.showImage(image_path)

class ImageProcessor():
    def __init__(self):
        self.filename = None
        self.image = None
        self.edit_image = None
        self.dir = 'mod/'
    def loadImage(self, filename):
        self.filename = filename
        image_path = os.path.join(workdir, filename)
        self.image = Image.open(image_path)
    def showImage(self, path):
        pixmapimage = QPixmap(path)
        label_width = img.width()
        label_height = img.height()
        scaled_pixmap = pixmapimage.scaled(
        label_width,
        label_height,
        Qt.KeepAspectRatio)
        img.setPixmap(scaled_pixmap)
        img.setVisible(True)
    
    def do_bw(self):
        try:
            self.edit_image = self.image.convert('L')
            self.saveImage()
            image_path = os.path.join(
                workdir,
                self.dir,
                self.filename)
            self.showImage(image_path)
        except:
            img.setText('Вы не выбрали картинку.')

    def saveImage(self):
        try:
            path = os.path.join(workdir, self.dir)
            if not(os.path.exists(path) or os.path.isdir(path)):
                os.mkdir(path)
            image_path = os.path.join(path, self.filename)
            self.edit_image.sve(image_path)
        except:
            img.setText('Вы не выбрали картинку')
    def do_left(self):
        try:
            self.edit_image = self.image.transpose(Image.ROTATE_90)
            self.saveImage()
            image_path = os.path.join(
                workdir,
                self.dir,
                self.filename)
            self.showImage(image_path)
        except:
            img.setText('Вы не выбрали картинку')
    def do_right(self):
        try:
            self.edit_image = self.image.transpose(Image.ROTATE_270)
            self.saveImage()
            image_path = os.path.join(
                workdir,
                self.dir,
                self.filename)
            self.showImage(image_path)
        except:
            img.setText('Вы не выбрали картинку')
    def do_sharp(self):
        try:
            self.edit_image = self.image.filter(ImageFilter.SHARPEN)
            self.saveImage()
            image_path = os.path.join(
                workdir,
                self.dir,
                self.filename)
            self.showImage(image_path)
        except:
            img.setText('Вы не выбрали картинку')
    def do_save(self):
        try:
            self.saveImage()
        except:
            img.setText('Вы не выбрали картинку')
    def do_reset(self):
        try:
            image_path = os.path.join()
            self.showImage(image_path)
        except:
            img.setText('Вы не выбрали картинку')
    def do_mirror(self):
        try:
            image_path = os.path.join(workdir, self.filename)
            self.saveImage()
            image_path = os.path.join(
                workdir,
                self.dir,
                self.filename)
            self.showImage(image_path)
        except:
            img.setText('Вы не выбрали картинку')
import os
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageFilter, ImageOps
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(
    QApplication, QWidget, QPushButton,
    QLabel, QVBoxLayout, QHBoxLayout, 
    QListWidget, QFileDialog)

workdir = ''
workimage = ImageProcessor

app = QApplication([])

win = QWidget()
win.resize(800, 600)
win.setWindowTitle('ИзиЭдит')

btn_folder = QPushButton('папка')
btn_left = QPushButton('лево')
btn_right = QPushButton('право')
btn_mirror = QPushButton('зеркало')
btn_sharp = QPushButton('резкость')
btn_bw = QPushButton('ч/б')
btn_save = QPushButton('сохранить')
btn_reset = QPushButton('сбросить')

img = QLabel('Картинка не загружена')
file_list = QListWidget()

main_layout = QHBoxLayout()
left_layout = QVBoxLayout()
right_layout = QVBoxLayout()
btn_layout = QHBoxLayout()

left_layout.addWidget(btn_folder)
left_layout.addWidget(file_list)
right_layout.addWidget(img)

btn_layout.addWidget(btn_left)
btn_layout.addWidget(btn_right)
btn_layout.addWidget(btn_mirror)
btn_layout.addWidget(btn_sharp)
btn_layout.addWidget(btn_bw)
btn_layout.addWidget(btn_save)
btn_layout.addWidget(btn_reset)
right_layout.addLayout(btn_layout)

right_line.addWidget(img, 70)
right_line.addLayout(btn_line, 30)

main_layout.addLayout(left_layout, 20)
main_layout.addLayout(right_layout, 80)
win.setLayout(main_layout)

btn_folder.clicked.connect(showFilenamesList)
file_list.currentRowChanged.connect(showChosenImage)
btn_bw.clicked.connect(workimage.do_bw)
btn_left.clicked.connect(workimage.do_left)
btn_right.clicked.connect(workimage.do_right)
btn_save.clicked.connect(workimage.do_save)
btn_sharp.clicked.connect(workimage.do_sharp)
btn_reset.clicked.connect(workimage.do_reset)
btn_mirror.clicked.connect(workimage.do_mirror)



win.show()
app.exec()