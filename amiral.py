#-*- coding: utf-8 -*-
import random
import time
gemilist = []
gemilist2 = []
oyunalani = [[0]*8 for i in range(8)]
print oyunalani[0],"\n",oyunalani[1],"\n",oyunalani[2],"\n",oyunalani[3],"\n",oyunalani[4],"\n",oyunalani[5],"\n",oyunalani[6],"\n",oyunalani[7],"\n",
print """Savaşacağımız Alan Yukarıda Stratejini İyi Belirlemelisin...

1 - Rastgele Strateji Oluştur
2- Kendi Stratejimi Uygulayacağım

"""
secim = raw_input("Seçiminizi Tuşlayınız : ")
if secim == 2:
	print "\n 0-7 Arası Değerler Giriniz \n"
	for i in range(1,10):
		x = int(raw_input("{}. Geminin 'x' Koordinatı : ".format(i)))
		y = int(raw_input("{}. Geminin 'y' Koordinatı : ".format(i)))
		oyunalani[x][y] = 1
		gemilist.append([x,y])
else:
	for i in range(1,10):
		x=random.randrange(0,7)
		y=random.randrange(0,7)
		oyunalani[x][y] = 1
		gemilist.append([x,y])
print "\nGemilerin Konumları...\n"
print oyunalani[0],"\n",oyunalani[1],"\n",oyunalani[2],"\n",oyunalani[3],"\n",oyunalani[4],"\n",oyunalani[5],"\n",oyunalani[6],"\n",oyunalani[7],"\n",
print "\nRakibin Gemilerini Konumlandırıyor...\nEtrafta Savaş Kokusu Var...\n"
for j in range(1,10):
	x = random.randrange(0,7)
	y = random.randrange(0,7)
	oyunalani[x][y] = 2
	gemilist2.append([x,y])
print "\n Rakip Savaşa Hazır...\nHaydi Kazamız Mübarek Olsun...\n"

oyuncu = 1 #1 = user -- 2 = pc
pcgemi = 9
usergemi = 9
while True:
	if oyuncu == 1:
		print "\nSıra Sende...\n"
		x = int(raw_input("Hedefin 'x' Koordinatı : "))
		y = int(raw_input("Hedefin 'y' Koordinatı : "))
		if oyunalani[x][y] == 2:
			oyunalani[x][y] = 0
			pcgemi -= 1
			time.sleep(2)
			print "BOOOOOOOMMMMMM !!!!!! Bir Düşman Gemisini Vurdun !!!!!!!!\n"
			print "Rakibin Kalan Gemi Sayısı : ",str(pcgemi)
			print "Oyuncunun Kalan Gemi Sayısı : ",str(usergemi)
		else:
			oyuncu = 2
			time.sleep(2)
			print "KARAVANA !! Hedef Koordinatlarda Düşman Gemisi Bulunmuyor..\n"
			
	elif oyuncu == 2:
		print "Rakibinin Saldırı Yapmasını Beklemelisin..."
		x = random.randrange(0,7)
		y = random.randrange(0,7)
		if oyunalani[x][y] == 1:
			oyunalani[x][y] = 0
			usergemi -= 1
			time.sleep(3)
			print "Naaayır Noooolamazz !! Bir Gemi Kaybettin !!"
			print "Rakibin Kalan Gemi Sayısı : ",str(pcgemi)
			print "Oyuncunun Kalan Gemi Sayısı : ",str(usergemi)
		else:
			time.sleep(3)
			print "Rakibin Iskaladı..."
			oyuncu = 1
	if usergemi == 0:
		print "\n\n\nKAYBETTİN !!! Geçmiş Olsun...\n\n"
	elif pcgemi == 0:
		print "\n\n\nKAZANDINNN !! Bu Iş Böyle Yapılır Tebrikler.."


