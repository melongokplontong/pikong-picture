#create the Easy Editor photo editor here!
workdir = None
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton,QListWidget,QHBoxLayout,QVBoxLayout
from PyQt5.QtWidgets import QFileDialog
import os
from PIL import Image
from PyQt5.QtGui import QPixmap
from PIL import ImageFilter,ImageEnhance

#Set up awal
app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle( 'cutcut' ) #mengubah judul aplikasi
my_win.resize(700, 500) #mengubah ukuran jendela

#Di bagian ini kamu akan menambahkan kode widget-widget
tombol_left = QPushButton("left")
tombol_right = QPushButton("right")
mirror = QPushButton("mirror")
sharpness = QPushButton("sharpness")
B_w = QPushButton("B&W")
folder = QPushButton("folder")

image = QLabel("Image")

list_file = QListWidget()

garis_utama = QHBoxLayout()
garis_tombol = QHBoxLayout()
kolom1 = QVBoxLayout()
kolom2 = QVBoxLayout()

#Di bagian ini kamu menambahkan kode untuk tambah layout
kolom1.addWidget(folder)
kolom1.addWidget(list_file)
kolom2.addWidget(image)
garis_tombol.addWidget(tombol_right)
garis_tombol.addWidget(tombol_left)
garis_tombol.addWidget(mirror)
garis_tombol.addWidget(sharpness)
garis_tombol.addWidget(B_w)
kolom2.addLayout(garis_tombol)
garis_utama.addLayout(kolom1)
garis_utama.addLayout(kolom2)


#Di bagian ini kamu menambahkan function khusus
def ambil_folder():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
def tampilkan_folder():
    ambil_folder()
    daftar_file = os.listdir(workdir)
    file_ditampilkan = filter(daftar_file,['.png','.jpg','.jpeg','.svg','.bmp','.gif'])
    
    list_file.clear()
    for file in file_ditampilkan:
        list_file.addItem(file)
def filter(files, format_file):
    hasil: list =[]
    for file in files:
        for format in format_file:
            if file.endswith(format):
                hasil.append(file)
    return hasil
class image_prosessor ():
    def saveimage(self):
        lokasi_simpan = os.path.join(self.lokasi_folder, 'editen/')
        if not(os.path.exists(lokasi_simpan)or os.path.isdir(lokasi_simpan)):
          os.mkdir(lokasi_simpan)
        lokasi_file = os.path.join(lokasi_simpan,self.nama_file)
        self.gambar.save(lokasi_file)
    def bw(self):
        self.gambar = self.gambar.convert('L')
        self.saveimage()
        lokasi_file = os.path.join(self.lokasi_folder,'editen/',self.nama_file)
        self.showimage(lokasi_file)
    def mirror(self):
        self.gambar = self.gambar.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveimage()
        lokasi_file = os.path.join(self.lokasi_folder,'editen/',self.nama_file)
        self.showimage(lokasi_file)
    
    def left(self):
        self.gambar = self.gambar.transpose(Image.ROTATE_90)
        self.saveimage()
        lokasi_file = os.path.join(self.lokasi_folder,'editen/',self.nama_file)
        self.showimage(lokasi_file)
    def right(self):
        self.gambar = self.gambar.transpose(Image.ROTATE_270)
        self.saveimage()
        lokasi_file = os.path.join(self.lokasi_folder,'editen/',self.nama_file)
        self.showimage(lokasi_file)
    def sharpness(self):
        self.gambar = ImageEnhance.Contrast(self.gambar)
        self.gambar = self.gambar.enhance(1.5)
        self.saveimage()
        lokasi_file = os.path.join(self.lokasi_folder,'editen/',self.nama_file)
        self.showimage(lokasi_file)
    def __init__(self):
        self.nama_file = None
        self.lokasi_folder = None
        self.gambar = None
    def loadimage(self, lokasi_folder, nama_file):
        self.lokasi_folder = lokasi_folder
        self.nama_file = nama_file
        lokasi_file = os.path.join(self.lokasi_folder, self.nama_file)
        self.gambar = Image.open(lokasi_file)
    def showimage(self, lokasi_file):
        image.hide()
        pixmap = QPixmap(lokasi_file)
        lebar = image.width()
        tinggi = image.height()
        pixmap = pixmap.scaled(lebar, tinggi, Qt.KeepAspectRatio)
        image.setPixmap(pixmap)
        image.show()
gambar_dibuka = image_prosessor()
def tampilkan_gambar():
    if list_file.currentRow() >= 0 :
        nama_file = list_file.currentItem().text()
        gambar_dibuka.loadimage(workdir, nama_file) 
        lokasi_file = os.path.join(gambar_dibuka.lokasi_folder, gambar_dibuka.nama_file)
        gambar_dibuka.showimage(lokasi_file)

#Di bagian ini kamu menambahkan event
folder.clicked.connect(tampilkan_folder)
list_file.currentRowChanged.connect(tampilkan_gambar)
B_w.clicked.connect(gambar_dibuka.bw)
mirror.clicked.connect(gambar_dibuka.mirror)
sharpness.clicked.connect(gambar_dibuka.sharpness)
tombol_left.clicked.connect(gambar_dibuka.left)
tombol_right.clicked.connect(gambar_dibuka.right)

#Set up akhir
my_win.setLayout(garis_utama)
my_win.show()
app.exec_()
