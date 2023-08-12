
notlar =[]

dersSayisi = int(input("Ders Sayısını Girin: "))

for dersler in range(dersSayisi):
    
    dersAdi = input("Ders Adını Girin: ")
    print("" ,dersler+1,". Ders Adı: " , dersAdi)
    notu =float(input("1-100 Arasında Olacak Şekilde Notunuzu Girin: "))
    if notu <=100 and notu >=0:
        print("Notunuz: " , notu)
    else :
        print("Geçerli Bir Not Girin!!!")    
    notlar.append((dersAdi,notu))


toplamNot = 0

for dersAdi, notu in notlar:
    print(dersAdi, ": ", notu)
    toplamNot = toplamNot + notu

ortalama = toplamNot / dersSayisi
print("Ortalamanız: ", ortalama)


if ortalama <=100 and ortalama >=55:
    print("Tebrikler Geçtiniz")
elif ortalama < 55 and ortalama > 0:
    print("Kaldınız")
else:
    print("Geçersiz Not Aralığı")











