# -*- coding: utf-8 -*-


class BankaHesabi:
    
    def __init__(self, kisi, bakiye=0):
        self.kisi = kisi
        self.bakiye = bakiye        
        
    def depozit(self, miktar):
        self.bakiye += miktar
        print(miktar,"TL Yatırıldı. Yeni Bakiye:", self.bakiye)
        
    def paraCekme (self, miktar):
        if miktar <= self.bakiye:
            self.bakiye -= miktar
            print(miktar,"TL Çekildi. Yeni Bakiye:",self.bakiye)
        else:
            print("Yetersiz bakiye")
            
hesap =BankaHesabi("Ahmet",1000)

hesap.depozit(800)
hesap.paraCekme(500)
hesap.paraCekme(1500)
