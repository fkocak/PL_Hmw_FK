# -*- coding: utf-8 -*-
# HW-3 answers for Alfa Programming Language Course Lecture-6

# Program name: PL-HW3_odev_4.py
# Written by: Fatih Koçak (fkocak@aysuelektrik.com.tr)
# Date: 09-04-2016
# Version : 1.0
# ---------------------------------------------------------------------------

# Soru #1
print "Problem 1-)"
print "Kullanıcıdan iki adet input alın.Birinci input max 200 karakter olsun."
print "İkinci input ise 4 adet integer olsun. 2. inputtaki 1. ve 2. değerler arası ile "
print "3. ve 4. değerler arası kadar 1.inputtan string kesip sonuçları birleştirerek yazınız."
print " "

# Algoritma #1

# 1-)Kullancından giriş al
# 2-)Birinci inputun alfanümerik ve max 200 karakter olduğunu kontrol et
# 3-)ikinci inputtaki girişleri boşluk karakterine göre böl
# 4-)Yeni bir listeye bölünen indexleri ata
# 5-)Listenin birinci indexinden ikinci indexine kadar olan aralığı birinci inputtaki stringten alıp s1 değişkenine ata
# 6-)Listenin üçüncü indexinden dördüncü indexine kadar olan aralığı birinci inputtaki stringten alıp s2 değişkenine ata
# 7-)s1 ve s2 değerlerini yanyana olcak şekilde ekrana yazdır.


# Cevap #1

giris_1 = raw_input("Lütfen 200 karakterden fazla olmayacak şekilde string' inizi giriniz :")
giris_2 = raw_input("Lütfen 4 adet index değerini giriniz")

if giris_1.isalpha():
    uzunluk_1 = len(giris_1)
    if uzunluk_1 <= 200:
        listem = giris_2.split()
        print type(listem)
        a = int(listem[0])
        b = int(listem[1])
        c = int(listem[2])
        d = int(listem[3])
        if a < b:
            s1 = giris_1[a:b:1]
        elif a > b:
            s1 = giris_1[b:a:1]
        if c < d:
            s2 = giris_1[c:d:1]
        elif c > d:
            s2 = giris_1[d:c:1]
        print s1 + s2
    else:
        print "Girmiş olduğunuz giriş 200 adet karekterden fazladır."
else:
    print "Birinci string alfanümerik değildir."

# ----------------------------------------------------------------------------
# Soru #2

print "Problem 2-)"
print "Kullnacıdan 4 adet kordinat değeri alınız, Bu değerlere göre oluşan dörtgenin çevre ve alanını hesaplayınız"
print " "

# Algoritma #2
# 1-)Kullanıdan 4 adet kordinat giris al
# 2-)Kordinatların arası mesafeleri kenar olarak hesapla
# 3-)Karşılıklı kenarlar birbirine eşitse dörtgenin çevre ve alanını hesapla değilse 5. adıma geç
# 4-)Sonuçları ekrana yazdır.
# 5-)Hatalı kenar bilgilerini ekrana yazdır.

# Cevap #2

a = input("a köşesi x ve y eksen değerini giriniz!")
b = input("b köşesi x ve y eksen değerini giriniz!")
c = input("c köşesi x ve y eksen değerini giriniz!")
d = input("d köşesi x ve y eksen değerini giriniz!")

Kisa_kenar_1 = float(d[1]) - float(a[1])
Kisa_kenar_2 = float(c[1]) - float(b[1])
Uzun_kenar_1 = float(c[0]) - float(d[0])
Uzun_kenar_2 = float(b[0]) - float(a[0])

if Kisa_kenar_1 == Kisa_kenar_2:
    if Uzun_kenar_1 == Uzun_kenar_2:
        alan = Kisa_kenar_1 * Uzun_kenar_1
        cevre = Kisa_kenar_1 + Kisa_kenar_2 + Uzun_kenar_1 + Uzun_kenar_2
        print "Dörtgenin alanı :", alan
        print "Dörtegenin çevresi :", cevre
    else:
        print "uzun kenerlar birbirine eşit değildir."
else:
    print "kısa keneralar birbirine eşit değildir."

# ----------------------------------------------------------------------------
# Soru #3

print "Problem 3-)"
print "Kullnacıdan 1 adet input alınız. Aldığınız input ile sıfır arasındaki asal sayıları bulunuz"
print " "

# Algoritma #3
# 1-)Kullanıdan 1 adet giris al
# 2-)3 ten başlayarak girişe kadar 2 artımlı liste yap
# 3-)Matematiksel formüllerle asal sayı kontrolü yap
# 4-)Sonuçları ekrana yazdır.

# Cevap #3

giris = input("Lütfen bir sayı giriniz :")
if 2 <= giris :
    liste=range(3,giris+1,2)
    karakok = giris ** 0.5
    yarisi=(giris+1)/2-1
    i=0
    m=3
    while m <= karakok:
        if liste[i]:
            j=(m*m-3)/2
            liste[j]=0
            while j<yarisi:
                liste[j]=0
                j+=m
        i=i+1
        m=2*i+3
    liste.insert(0,2)
    uzunluk = len(liste)

    a = 0
    while a <= uzunluk :
        liste = sorted(liste)
        if liste[0] == 0:
            del liste[0]
        a += 1
    print "Sıfır ile girdiğiniz sayı arasındaki asal sayılar :\n", liste
else:
    print "Sıfır ile girdiğiniz sayı arasında asal sayı yokutr!."

# ----------------------------------------------------------------------------
# Soru #4

print "Problem 4-)"
print "Kullanıcı tarafından verilen integer listenin 0. indeksinden başlayarak"
print "2'li gruplar halinde toplamlarını yeni listeye ekleyiniz"

# Algoritma #4
# 1-)Kullanıdan integer listeyi al
# 2-)liste uzunluğunu bul 2' ye tam bölünüyorsa 3. adıma, değilse 6. adıma geç
# 3-)0.idexten başlayarak 2'li gruplar halinde verilen integer listenin itemlerini topla
# 4-)Topladığın her itemi yeni bir listeye sırası ile ekle
# 5-)Oluşturduğun yeni listeyi ekrana yazdır.
# 6-)0.idexten başlayarak 2'li gruplar halinde verilen integer listenin itemlerini topla
# 7-)Topladığın her itemi yeni bir listeye sırası ile ekle
# 8-)Verilen listenin son itemini yeni listeye ekle
# 9-)Oluşturduğun yeni listeyi ekrana yazdır.

# Cevap #4

listem = input("lütfen sayı listesinizi giriniz :")
uzunluk = len(listem)
if uzunluk %2 == 0 :
    i = 0
    j = 0
    w = 1
    yeni_listem = list()
    while i <= uzunluk:
        if w == uzunluk:
            break
        if j == uzunluk:
            break
        a = listem[j]
        b = listem[w]
        yeni_item = a+b
        yeni_listem.append(yeni_item)
        j += 2
        w = j + 1
        i += 1
else :
    i = 0
    j = 0
    w = 1
    yeni_listem = list()
    while i <= uzunluk:
        if w == uzunluk:
            yeni_listem.append(listem[(uzunluk-1)])
            break
        if j == uzunluk:
            yeni_listem.append(listem[(uzunluk-1)])
            break
        a = listem[j]
        b = listem[w]
        yeni_item = a+b
        yeni_listem.append(yeni_item)
        j += 2
        w = j + 1
        i += 1

print "Oluşturduğum yeni liste :\n",yeni_listem

