# kütüphaneler
import math
import time
import sys

# sürüm (alpha)
def alphastrt():
    try:
        print("Matematikçi - Alpha Hazır!")
        time.sleep(0.5)
        print("Bugün ne çözelim matematik ustası ;)\n")
        while True:
            b = input("İşlem Seç: (+,-,*,/) > ")
            sayi1 = float(input("İlk Sayıyı Gir: "))
            sayi2 = float(input("İkinci Sayıyı Gir: "))
            if b == "+":
                print("Cevap Üretiliyor..")
                time.sleep(0.6)
                print("Çok basit! Cevap: ", sayi1 + sayi2)
            elif b == "-":
                print("Cevap Üretiliyor..")
                time.sleep(1.2)
                print("Çıkarma benim adım. Cevap: ", sayi1 - sayi2)
            elif b == "*":
                print("Cevap Üretiliyor..")
                time.sleep(1.8)
                print("Biraz zor gelebilir, dermişim ;) Cevap: ", sayi1 * sayi2)
            elif b == "/" and sayi2 == 0:
                print("Sen, 0'a birşey bölmek? Cidden mi? -_-")
            elif b == "/":
                print("Cevap Üretiliyor..")
                time.sleep(2.4)
                print("Hadi Çözelim! Cevap: ", sayi1 / sayi2)
            else:
                print("Lütfen adamakıllı birşeyler gir.")
    except:
        print("Lütfen geçerli şeyler gir.")
        return alphastrt()
# sürüm (mini.beta)
def betastrt():
    try:
        print("Matematikçi - Mini.Beta Hazır!")
        time.sleep(0.5)
        print("Ne çözmek istersin Matematik kralı ;)\n")
        while True:
            b = input("İşlem Seç: (+,-,*,/,karekök,^, !, çık) > ").lower()
            if b == "karekök":
                sayiilk = float(input("Bir Sayı Gir: "))
                print("Cevap Hazırlanıyor..")
                time.sleep(1.2)
                print("Valla zor sordun bu sefer kralll ", math.sqrt(sayiilk))
            if b == "!":
                    ilksayi1 = int(input("Bir sayı gir: "))
                    print("Çözülüyor..")
                    time.sleep(1.2)
                    print("Faktoriyellerle aram iyi değildir ama.. Sonuç: ", math.factorial(ilksayi1))
            elif b == "çık":
                    print("Sürüm seçmeye geri dönülüyor..")
                    time.sleep(1)
                    break
            else:
                sayi1 = float(input("İlk Sayıyı Gir: ")) # !!!
                sayi2 = float(input("İkinci Sayıyı Gir: ")) # !!!
                if b == "+":
                    print("Cevap Üretiliyor..")
                    time.sleep(0.2)
                    print("Valla kolay! Cevap: ", sayi1 + sayi2)
                elif b == "-":
                    print("Cevap Üretiliyor..")
                    time.sleep(0.4)
                    print("Kolay o çıkarma! Cevap: ", sayi1 - sayi2)
                elif b == "*":
                    print("Cevap Üretiliyor..")
                    time.sleep(0.6)
                    print("Çarpma eğlencelidir. Cevap: ", sayi1 * sayi2)
                elif b == "/" and sayi2 == 0:
                    print("Sen, 0'a birşey bölmek? Cidden mi? •_•")
                elif b == "/":
                    print("Cevap Üretiliyor..")
                    time.sleep(0.8)
                    print("Hadi Çözelim! Cevap: ", sayi1 / sayi2)
                elif b == "^":
                    print("Cevap Üretiliyor..")
                    time.sleep(1.0)
                    print("En sevdiğim konu ;) ", sayi1 ** sayi2)
                else:
                    print("Lütfen adamakıllı birşeyler gir.")
    except:
         print("Lütfen geçerli şeyler gir.")
         return betastrt()
            
# giriş
time.sleep(1)
print("Matematikçi by The Yiğit Mehmet presents.. \n")
time.sleep(1)
print("Hangi sürümü kullanmayı tercih edersiniz?")
print("1- Alpha")
print("2- Mini.Beta")
print("Çık")
while True:
    a = input("Seçimin: ").lower()
    if a == "1" or a == "alpha":
        print("Alpha Sürüm Başlıyor..")
        time.sleep(1)
        alphastrt()
    elif a == "2" or a == "mini.beta":
        print("Minimal Beta Sürüm Başlıyor..")
        time.sleep(2)
        betastrt()
    elif a == "çık":
        print("Çıkılıyor..")
        sys.exit()
    else:
        print("Deli misin? Lütfen geçerli bir sürüm seç")
