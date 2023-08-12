# -*- coding: utf-8 -*-

sozluk = {
    "apple" : "Elma",
    "banana" : "Muz",
    "pear" :"Armut",
    "orange" : "Portakal",
    "melon" : "Kavun",
    "grape" : "Üzüm",
    "watermelon" : "Karpuz",
    "strawberry" : "Çilek",
    "kiwi" : "Kivi",
    }


def kelimeAra(sozluk,kelime):
    if kelime in sozluk:
        return sozluk [kelime]
    else:
        return "kelime bulunamadı"
    
while True:
    kelime = input("Anlamını Öğrenmek İstediğiniz Meyvenin İngilizcesini Girin:")
    if kelime == "q" :
        break

    anlam = kelimeAra(sozluk, kelime)
    print(kelime,":",anlam)