# -*- coding: cp1254 -*-

#�deal kilo hesaplama program� =>

"""
print "
1)Erkek
2)Kad�n
"

cinsiyet = input("Cinsiyetinizi belirleyiniz! > ")
if cinsiyet == 1:
    e_boy = input("Boyunuzu giriniz > ")
    e_yas = input ("Ya��n�z� giriniz > ")
    e_top = (e_boy-100+e_yas/10)*0.9    #Erkek i�in form�l.
    print "�deal kilonuz >> ", e_top
    
if cinsiyet == 2:
    k_boy = input("Boyunuzu giriniz > ")
    k_yas = input ("Ya��n�z� giriniz > ")
    k_top = (k_boy-100+k_yas/10)*0.8    #Kad�n i�in form�l.
    print "�deal kilonuz >> ", k_top


"""

#hocan�n yapt��� 
print "1) erkek"
print "2) kad�n"
b = float(raw_input("Boyunuz (cm) : "))
y = int(raw_input("Ya��n�z : "))
c = int(raw_input("Cinsiyetiniz "))

if c == 1:
    top = (b-100+y/10)*0.9    #Erkek i�in form�l.
else:
    top = (b-100+y/10)*0.8    #Kad�n i�in form�l.

print "�deal kilonuz >> ", top
