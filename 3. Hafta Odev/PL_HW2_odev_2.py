# 1-) (0,1,2,3,4,...1358) Sayi dizisinin toplamini bulunuz.

toplam = 0
degisken = 0
sayi_adedi = (((1358 - 0) / 1) + 1)

while degisken < sayi_adedi:
    toplam += degisken
    degisken += 1

print " "
print "---------------------------------------------------"
print " "
print "1 nolu proplem icin cevabim asagida yer almaktadir."
print "0' dan 1358' e kadar olan sayilarin toplami : " + str(toplam) + " 'dir."

# 2-) (0.2,0.4,0.6,0.8,...,9,8) Sayi dizisinin toplamini bulunuz.

toplam = 0
toplam_1 = 0
degisken = 0
sayi_adedi = (((9.8 - 0.2) / 0.2) + 1)

while degisken < sayi_adedi:
    toplam = 0.2 * degisken
    toplam_1 += toplam
    degisken += 1

print " "
print "---------------------------------------------------"
print " "
print "2 nolu proplem icin cevabim asagida yer almaktadir."
print "0.2' dae 9.8' e kadar olan sayilarin toplami : " + str(int(toplam_1)) + " 'dir."

# 3-) (0,1,2,3,4,...,248) Sayi dizisindeki sayilarin karelerinin toplamini bulunuz.

toplam = 0
degisken = 0
karesi = 0
sayi_adedi = (((248 - 0) / 1) + 1)

while degisken < sayi_adedi:
    karesi = degisken * degisken
    toplam += karesi
    degisken += 1

print " "
print "---------------------------------------------------"
print " "
print "3 nolu proplem icin cevabim asagida yer almaktadir."
print "0' dan 248' e kadar olan sayilarin karelerinin toplami : " + str(toplam) + " 'dir."

# 4-) (0,1,2,3,4,...,248) Sayi dizisindeki 6'ya bolunebilen sayilari ve toplam adedini bulunuz.

toplam = 0
degisken = 0
kalan = 0
sayi_adedi = 0
sayi_adedi_1 = (((248 - 0) / 1) + 1)
altiya_bolunen_toplam_sayi = 0

print " "
print "---------------------------------------------------"
print " "
print "4 nolu proplem icin cevabim asagida yer almaktadir."
print "Altiya Bolunebilen Sayilar :"
print " "
while degisken < sayi_adedi_1:
    kalan = degisken % 6
    if kalan == 0:
        sayi_adedi += 1
        print str(sayi_adedi) + ".Sayi :" + str(degisken)
        print " "
        altiya_bolunen_toplam_sayi += degisken
    degisken += 1
print "Altiya bolunebilen " + str(sayi_adedi) + " adet sayinin toplami : " + str(altiya_bolunen_toplam_sayi) + " 'dir."
print " "
print "---------------------------------------------------"

a = 12534
b = 255688
c = a*b
print type(a)
print type(b)
print type(c)


