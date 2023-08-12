# -*- coding: utf-8 -*-
import random

rastgeleSayi = random.randint(1, 100)

tahminHakki = 7

while tahminHakki > 0:
    
    
    sayi = int(input("1-100 arasında bir sayi girin: "))
    
    if sayi <= 100 and sayi >=0:
        if rastgeleSayi == sayi:
            print("Tebrikler doğru bildiniz")
            break
        elif rastgeleSayi <= sayi:
            print("Küçük bir sayı giriniz")
        else :
            print("Büyük bir sayı giriniz")
    else:
        print("Lütfen 1 ile 100 arasında bir sayı giriniz")
        
    tahminHakki -=1
        
if tahminHakki == 0:
    print("Tahmin hakkınız bitti! Doğru cevap : ",rastgeleSayi)


