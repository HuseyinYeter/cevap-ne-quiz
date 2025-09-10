import random

import pygame


#Class Import
from classes import *
from sorular import *

#PyQt5 Imports
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon


pygame.mixer.init()
pygame.mixer.music.load("In The Morning - The Grey Room _ Clark Sims.mp3")



class GirisEkrani(QDialog):
    def __init__(self):
        super(GirisEkrani,self).__init__()
        loadUi("girisekran_tr.ui",self)
        self.yarismayabasla.clicked.connect(self.yarismabaslat)

        self.muziksecenek.stateChanged.connect(self.toggle_music)


    def yarismabaslat(self):
        isim = self.yarismaciadi.text()
        puan = 0


        if isim:
            yarismaci = Yarismaci(isim,puan)
            yarisma.add_yarismaci(yarismaci)

            yarismaekrani.set_yarismaci(yarismaci)



        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(1000)
        widget.setFixedHeight(800)

    def toggle_music(self,state):
        if state == 2:
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.stop()

class YarismaEkrani(QDialog):
    def __init__(self):
        super(YarismaEkrani,self).__init__()
        loadUi("yarismaekrani_tr.ui",self)
        self.AA.clicked.connect(lambda: self.cevap_kontrol(self.cevapa.text()))
        self.BB.clicked.connect(lambda: self.cevap_kontrol(self.cevapb.text()))
        self.CC.clicked.connect(lambda: self.cevap_kontrol(self.cevapc.text()))
        self.DD.clicked.connect(lambda: self.cevap_kontrol(self.cevapd.text()))

        self.muziksecenek.stateChanged.connect(self.toggle_music)

    def toggle_music(self, state):
        if state == 2:
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.stop()



    def set_yarismaci(self,yarismaci):
        self.yarismaci = yarismaci
        self.yarismaciekranisim.setText(self.yarismaci.isim)
        self.puangosterim.setText(f"{str(self.yarismaci.puan)}")

        soru_no = int(self.sorusayisi.text())

        if 1 <= soru_no <=3:
            soru_secimi = random.choice(kolay_sorular)
            kolay_sorular.remove(soru_secimi)

        elif 4 <= soru_no <= 7:
            soru_secimi = random.choice(ortaduzey_sorular)
            ortaduzey_sorular.remove(soru_secimi)

        elif 8 <= soru_no <= 10:
            soru_secimi = random.choice(zor_sorular)
            zor_sorular.remove(soru_secimi)


        else:
            widget.setCurrentIndex(2)
            widget.setFixedWidth(800)
            widget.setFixedHeight(600)
            return




        self.soru.setText(soru_secimi["soru"])
        self.dogru_cevap = soru_secimi["cevap"]


        secenekler = soru_secimi["seçenekler"].copy()
        random.shuffle(secenekler)

        self.cevapa.setText(secenekler[0])
        self.cevapb.setText(secenekler[1])
        self.cevapc.setText(secenekler[2])
        self.cevapd.setText(secenekler[3])



    def cevap_kontrol(self, secilen_cevap):


        if secilen_cevap == self.dogru_cevap:
            self.yarismaci.puan += 10
            QMessageBox.information(self, "Tebrikler", "Doğru cevap! ✅")
        else:
            QMessageBox.information(self, "Yanlış", f"Yanlış! Doğru cevap: {self.dogru_cevap}")
            widget.setCurrentIndex(widget.currentIndex() - 1)
            self.sorusayisi.setText(str(0))
            widget.setFixedWidth(800)
            widget.setFixedHeight(600)
        self.puangosterim.setText(str(self.yarismaci.puan))
        self.sorusayisi.setText(str(int(self.sorusayisi.text()) + 1))
        self.set_yarismaci(self.yarismaci)


    def sonraki_soru(self):
        self.sorusayisi.setText(str(int(self.sorusayisi.text()) + 1))
        self.set_yarismaci(self.yarismaci)




kolay_sorular_orj = kolay_sorular.copy()
ortaduzey_sorular_orj = ortaduzey_sorular.copy()
zor_sorular_orj = zor_sorular.copy()


class BitisEkrani(QDialog):
    def __init__(self):
        super(BitisEkrani,self).__init__()
        loadUi("bitisekrani.ui",self)
        self.tekraroyna.clicked.connect(self.tekrar_oyna)
        self.muziksecenek.stateChanged.connect(self.toggle_music)

    def toggle_music(self, state):
        if state == 2:
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.stop()

    def tekrar_oyna(self):

        yarisma.yarismacilar.clear()

        global kolay_sorular, ortaduzey_sorular, zor_sorular
        kolay_sorular = kolay_sorular_orj.copy()
        ortaduzey_sorular = ortaduzey_sorular_orj.copy()
        zor_sorular = zor_sorular_orj.copy()

        yarismaekrani.sorusayisi.setText("1")

        widget.setCurrentIndex(0)




app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()



girisekrani = GirisEkrani()
yarismaekrani = YarismaEkrani()
bitisekrani = BitisEkrani()

widget.addWidget(girisekrani)
widget.addWidget(yarismaekrani)
widget.addWidget(bitisekrani)

widget.setWindowTitle("Cevap Ne?")
widget.setWindowIcon(QIcon("logo.png"))

widget.setFixedWidth(800)
widget.setFixedHeight(600)

widget.show()
sys.exit(app.exec())

