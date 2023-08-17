# -*- coding: utf-8 -*-

import random

oyuncuPuani = 0
bilgisayarPuani = 0

while True:
    
    print("\nSeçiminizi yapın:")
    print("1. Taş")
    print("2. Kağıt")
    print("3. Makas")
    print("4. Çıkış")
    
    
    secim = int(input("Seçiminizi yapın:"))
    
    if secim == 4:
        break
    secenekler = ["Taş", "Kağıt", "Makas"]
    bilgisayarSecimi = random.choice(secenekler)
    
    oyuncuSecimi = secenekler[int(secim) - 1]
    
    print("Siz:", oyuncuSecimi)
    print("Bilgisayar:", bilgisayarSecimi)
    
    if oyuncuSecimi == bilgisayarSecimi:
        print("BERABERE!")
    elif oyuncuSecimi == "Kağıt" and bilgisayarSecimi == "Taş":
        print("SİZ KAZANDINIZ!")
        oyuncuPuani += 1
    elif oyuncuSecimi == "Taş" and bilgisayarSecimi == "Makas":
        print("SİZ KAZANDINIZ!")
        oyuncuPuani += 1
    elif oyuncuSecimi == "Makas" and bilgisayarSecimi == "Kağıt":
        print("SİZ KAZANDINIZ!")
        oyuncuPuani += 1
    else:
        print("BİLGİSAYAR KAZANDI!")
        bilgisayarPuani += 1
    
    print("SİZ:", oyuncuPuani, "-", "BİLGİSAYAR:", bilgisayarPuani)
    
    