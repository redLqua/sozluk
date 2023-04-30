import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

sifre_uzunlugu = int(input("Şifre uzunluğunu giriniz: "))#5
sifre = ""


for i in range(sifre_uzunlugu):
    sifre += random.choice(karakterler)

print(sifre)