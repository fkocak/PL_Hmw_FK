# -*- coding: utf-8 -*-
# HW-3 answers for Alfa Programming Language Course Lecture-5

# Program name: PL-HW3_odev_3.py
# Written by: Fatih Koçak (fkocak@aysuelektrik.com.tr)
# Date: 31-03-2016
# Version : 1.0

# Soru #1

print '''
Problem 1-)
Kullanıcıdan gelen karekter dizinini ortadan iki'ye bölün ilk yarısını
tersten olacak şekilde ikinci yarısının sağ tarafına yazdırınız ?
'''
# Algoritma #1

# 1-)Kullancından giriş al
# 2-)kelimenin baştan orta kısmına kadar olan kısmını tersten al
# 3-)kelimenin ortadan sonuna kadar olan kısmını değiştirmeden al
# 4-)3 adımdaki verinin sağ yanına 2 adımdaki veriyi alarak ekrana yazdır.

# Cevap #1

kelime = raw_input("Lütfen bir karekter dizisi (kelime) giriniz : ")
kelime_uzunlugu = len(kelime)
kalan = kelime_uzunlugu % 2

if kalan == 1:
    orta_karakter_sayisi = (((kelime_uzunlugu+1)/2)-1)
    print "Kelimenin orta kısmının sağı aynen alarak sol kısmını tersten sağ tarafa yazdırıyorum : ",kelime[orta_karakter_sayisi::1]+ kelime[orta_karakter_sayisi-1::-1]

else :
    orta_karakter_sayisi = (kelime_uzunlugu / 2)
    print "Kelimenin orta kısmının sağı aynen alarak sol kısmını tersten sağ tarafa yazdırıyorum : ",kelime[orta_karakter_sayisi::1]+ kelime[orta_karakter_sayisi-1::-1]

# Soru #2

print '''
Problem 2-)
Kullanıcıdan gelen karekter dizinini tersten yazılışı ile
karşılaştırarak aynı olup olmadığının doğruluk kontrolünü yapınız ?
'''
# Algoritma #2

# 1-)Kullancından giriş al
# 2-)kelimenin baştan sonuna kadar olan kısmını tersten al
# 3-)1 adımdaki veri ile 2 adımdaki veri için eşitlik kontrolü yap
# 4-)eşitlik bilgisinin sonucu ekrana yaz

# Cevap #2

kelime = raw_input("Lütfen bir karekter dizisi (kelime) giriniz : ")
tersten_kelime = kelime[::-1]
dogru = True
yanlis = False

if kelime == tersten_kelime :
    print ("Girdiğiniz kelime ile kelimenin tersten yazılışı ile yanıdır :"), dogru
else :
    print ("Gürdiğiniz kelime ile kelimenin tersten yazılışı aynı değildir : "), yanlis

# Soru #3

print '''
Problem 3-)
Kullanıcıdan gelen iki adet karekter dizisi için birinci inputtaki
alfabatik karakterlerin ikinci inputta kaç defa olduğunu bulunuz ?
'''
# Algoritma #3

# 1-)Kullancından girişleri al
# 2-)Kelimelerin alfabetik olduğunu kontrol et; alfabetikse 3. adıma geç, değilse 5. adıma geç
# 3-)Birinci kelimenin karekterlerini ikinci kelimenin içinde ara
# 4-)Eşleşen kelimeleri ekrana miktari ile birlikte yaz
# 5-)Ekrana hatalı bilgi mesajı yaz

# Cevap #3

kelime1 = raw_input("Lütfen birinci karekter dizisi (kelime) giriniz : ")
kelime2 = raw_input("Lütfen ikinci karekter dizisi (kelime) giriniz : ")

kelime_uzunlugu = len(kelime1)
i = 0
if kelime2.isalpha():
    if kelime1.isalpha():
        while i < kelime_uzunlugu :
            if kelime1[i] in kelime2 :
                a = kelime2.count(kelime1[i])
                print kelime1[i],"harfinden", a, "adet vardır."
            i += 1
    else :
        print "Girdiğiniz karakter dizisi alfabetik değildir. ( Sayı, Sembol yada Türkçe karakter içeriyor )!"
else :
        print "Girdiğiniz karakter dizisi alfabetik değildir. ( Sayı, Sembol yada Türkçe karakter içeriyor )!"


a = input ("a köşesi x ve y eksen değerini giriniz!")
b = input ("b köşesi x ve y eksen değerini giriniz!")
c = input ("c köşesi x ve y eksen değerini giriniz!")
d = input ("d köşesi x ve y eksen değerini giriniz!")

Kisa_kenar_1 = float(b[1]) - float(a[1])
Kisa_kenar_2 = float(c[1]) - float(d[1])
Uzun_kenar_1 = float(c[0]) - float(b[0])
Uzun_kenar_2 = float(d[0]) - float(a[0])


print Kisa_kenar_1,Kisa_kenar_2, Uzun_kenar_1, Uzun_kenar_2

if Kisa_kenar_1 == Kisa_kenar_2 :
    if Uzun_kenar_1 == Uzun_kenar_2 :
        sonuc = Kisa_kenar_1 * Uzun_kenar_1
        print sonuc
    else :
        print "uzun kenerlar birbirine eşit değildir."
else :
    print "kısa keneralar birbirine eşit değildir."

sonuc = float(((Uzun_kenar_1 + Uzun_kenar_2) / 2 )) * Kisa_kenar_2

print "Koordinatlarinizin alan sonucu:", sonuc, "metrekaredir."

