# -*- coding: utf-8 -*-

import random

aktiviteler = [
    "Doğa yürüyüşüne çıkın ve temiz havanın tadını çıkarın.",
    "Bir kitapçıya gidin ve yeni bir kitap keşfedin.",
    "Gönüllü bir organizasyona katılın ve topluluğunuza yardım edin.",
    "Farklı bir spor dalına başlayın ve yeni bir spor deneyimi yaşayın.",
    "Piknik yapın ve doğanın içinde rahatlayın.",
    "Yemek pişirmeyi öğrenmek için bir yemek kursuna kaydolun.",
    "Puzzle çözerek zihinsel becerilerinizi geliştirin.",
    "Fotoğrafçılığı daha da ileri taşıyarak fotoğraf düzenleme becerileri öğrenin.",
    "Şehrinizdeki tarihi binaları veya anıtları ziyaret edin ve yerel kültürü keşfedin.,"
    "Koleksiyon yapmaya başlayarak ilgi alanınıza uygun nesneler biriktirin.",
    "Kamp yaparak doğada kendinizi deneyimleyin.",
    "Gitar, piyano gibi bir enstrüman çalmayı öğrenmeye başlayın.",
    "Yoga veya meditasyon pratiği yaparak içsel huzur bulun.",
    "Fotoğraf albümü veya hatıra defteri oluşturarak anılarınızı saklayın.",
    "Gelişen teknolojiyi takip ederek yeni dijital araçlar deneyimleyin.",
    "Bir programlama dilini öğrenmeye başlayarak temel kodlama becerileri kazanın.",
    "Kişisel bir web sitesi veya blog oluşturarak web geliştirme deneyimi yaşayın.",
    "Mobil uygulama geliştirerek akıllı telefon platformlarında deneyim kazanın.",
    "Açık kaynaklı projelere katkıda bulunarak toplulukla işbirliği yapın.",
    "Veri analizi yaparak istatistiksel ve analitik becerilerinizi geliştirin.",
    "Makine öğrenimi veya yapay zeka projeleriyle veri tahmini yapın.",
    ]

def rastgeleAktiviteSec():
    return random.choice(aktiviteler)

while True:
    print("\nRastgele Aktivite Uygulaması")
    print("1. Rasgele Aktivite Öner")
    print("2. Çıkış")
    
    secim = input("Bir Seçenek Seçin: ")
    
    if secim == "1":
        rastgeleAktivite = rastgeleAktiviteSec()
        print("\nÖnerilen Aktivite:")
        print(rastgeleAktivite)
    elif secim == "2":
        break
    else:
        print("Geçersiz Seçenek")
    
    
    
    
    




