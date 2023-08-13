# -*- coding: utf-8 -*-

class Kitap ():
    def __init__(self,ad,yazar):
        self.ad = ad
        self.yazar = yazar
        

kutuphane = []


while True:
    print("\nKütüphane Yönetimi")
    print("1. Kitap Ekle")
    print("2. Kitapları Listele")
    print("3. Kitap Ara")
    print("4. Çıkış")
    
    secim = int(input("Bir Seçim Yapın: "))
    
    if secim == 1:
        ad = input("Kitap Adı Girin: ")
        yazar = input("Yazar Adı Girin: ")
        kitap = Kitap(ad, yazar)
        kutuphane.append(kitap)
        
        print("Kitap Kütüphaneye Eklendi.")
    
    elif secim == 2:
        for kitap in kutuphane:
            print("Kitap Adı:",kitap.ad,"-","Yazar Adı:",kitap.yazar)
            
    elif secim == 3:
        aramaTerimi = input("Aranacak kitap Adını veya Yazar Adını Girin: ").lower()
        bulunanKitaplar = []

        for kitap in kutuphane:
            if aramaTerimi in kitap.ad.lower() or aramaTerimi in kitap.yazar.lower():
                bulunanKitaplar.append(kitap)

        if bulunanKitaplar:
            print("Bulunan Kitaplar:")
            for kitap in bulunanKitaplar:
                print("Kitap Adı:",kitap.ad,"-","Yazar Adı:",kitap.yazar)
        else:
            print("Kitap Bulunamadı.")
            
    elif secim == 4:
        break
    
    else:
        print("Geçersiz Seçenek, Tekrar Deneyin!")
        
        
        