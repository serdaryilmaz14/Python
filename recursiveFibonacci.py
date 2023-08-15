# -*- coding: utf-8 -*-

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        fibo = fibonacci(n-1)
        fibo.append(fibo[-1] + fibo[-2])
        return fibo
    
adet = int(input("Lütfen bir sayı girin: "))
fibDizi = fibonacci(adet)
print(f"İlk {adet} Fibonacci sayısı: {fibDizi}")
        