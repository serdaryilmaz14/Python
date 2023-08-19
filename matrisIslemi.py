# -*- coding: utf-8 -*-

def matrisToplama(matris1,matris2):
    if len(matris1) != len(matris2) or len(matris1[0]) != len(matris2[0]):
        raise ValueError("Matris boyutları eşleşmiyor")
        
    sonuc = [[matris1[i][j] + matris2[i][j] for j in range(len(matris1[0]))] for i in range(len(matris1))]
    return sonuc

def matrisCarpimi(matris1, matris2):
    if len(matris1[0]) != len(matris2):
        raise ValueError("Matris boyutları çarpılamaz")
        
        
    sonuc = [[0 for _ in range(len(matris2[0]))] for _ in range(len(matris1))]
    for i in range(len(matris1)):
        for j in range(len(matris2[0])):
           for k in range(len(matris2)): 
               sonuc[i][j] += matris1[i][k] * matris2[k][j]
               
    return sonuc


matris1 = [[4, 4], [2, 3]]
matris2 = [[1, 2], [4, 2]]

print("Matris Toplamı:")
print(matrisToplama(matris1, matris2))
print("Matris Çarpımı:")
print(matrisCarpimi(matris1, matris2))