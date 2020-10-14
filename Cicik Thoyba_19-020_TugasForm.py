#mengimport semua system
import sys
from PyQt5.QtWidgets import *

def window():#membuat fungsi dengan nama fungsi window
    app = QApplication(sys.argv)#deklarasi app dengan parameter sys.argv
    form = QWidget()#membuat variabel 
    form.setGeometry(100,100,700,200)#mengatur ukuran window(koordinat x,koordinat y,lebar,tinggi) 

#Menampilkan teks 
    label = QLabel(form)#membuat variabel label dengan nama Qlabel dengan parameter form
    label.setText("Input Biodata")#menambahkan teks Input Biodata
    label.setStyleSheet("background-color: grey; color: red; font: bold 25px; ")#memberikan warna background abu-abu,warna tulisan merah,jenis font bold dengan ukuran 25pixsel

#membuat kotak inputan
    lineEdit1 = QLineEdit()
    lineEdit2 = QLineEdit()
    lineEdit3 = QLineEdit()

    layout = QFormLayout()#membuat layout
    layout.addRow(label)#menambahkan baris pada layout
    layout.addRow("Name", lineEdit1)#menambahkan teks Name diteruskan lineEdit1(kotak inputan)
    layout.addRow("Adress", lineEdit2)#menambahkan teks Name diteruskan lineEdit2(kotak inputan)
    layout.addRow("", lineEdit3)#tidak ada teks diteruskan lineEdit3(kotak inputan)

#Menampilkan pilihan yang bisa dipilih lebih dari 1
    checkbox1 = QCheckBox("Makan")#membuat variabel checkbox1
    checkbox2 = QCheckBox("Tidur")#membuat variabel checkbox2
    checkbox3 = QCheckBox("Main")#membuat variabel checkbox3
    layout.addRow("Hobby", checkbox1)#setelah kata hobby disampingnya ada teks makan(checkbox1)
    layout.addWidget(checkbox2)#menambahkan widget tidur(checkbox2)
    layout.addWidget(checkbox3)#menambahkan widget main(checkbox3)

#Menampilkan pilihan yang hanya bisa dipilih satu saja
    radio1 = QRadioButton("Pelajar")#membuat variabel radio1
    radio2 = QRadioButton("Pegawai")#membuat variabel radio2
    radio3 = QRadioButton("Wirasawasta")#membuat variabel radio3
    layout.addRow("Status", radio1)#setelah kata status disampingnya ada teks pelajar(radio1)
    layout.addWidget(radio2)#menambahkan widget Pegawai(radio2)
    layout.addWidget(radio3)#menambahkan widget Wiraswasta(radio3)

#perintah menjalankan
    form.setLayout(layout)
    form.show()
    app.exec_()

if __name__ == '__main__':#tugas utama
    window()
