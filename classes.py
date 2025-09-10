class Yarisma:
    def __init__(self,name):
        self.name = name
        self.yarismacilar = []

    def add_yarismaci(self,yarismaci):
        self.yarismacilar.append(yarismaci)

yarisma = Yarisma("Cevap Ne?")

class Yarismaci:
    def __init__(self,isim,puan = 0):
        self.isim = isim
        self.puan = puan


