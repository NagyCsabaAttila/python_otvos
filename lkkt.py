#Ez a paraméter beolvasás része amit múltkor néztünk
import sys

#Deklarációk
print(sys.argv[1])
szamok = []
szorzok = []

#A beolvasott paraméterből alkotunk egy tömböt 'inNum' néven.
inNum = sys.argv[1].split(',')

#Mivel ilyenkor string (str) formában vannnak a számok
#így át kell őket alakítani int-é ahhoz, hogy dolgozhassunk
#velük.
for n in inNum:
    szamok.append(int(n))

print(szamok)

############################################################

#Ez itt egy prímtényezős felbontás.
#Ez nem szükséges, de gondoltam benne hagyom
#lehet még vmikor kelleni fog.
n = 2

for i in range(len(szamok)):
    szam = szamok[i]
    print(szam)
    while (n <= szam):
        if szam % n == 0:
            szam = szam / n
            szorzok.append(n)
            print(n)
        else:
            n = n + 1
    n = 2
    print()

print(szorzok)
print()

############################################################

#Euklideszi algoritmus: LKKT(a, b) = a * b / LNKO(a, b)
#Vagyis elsőnek kiszámoljuk a legnagyob közös osztójukat,
#majd a két szám szorzatát elosztjuk vele.

# LEGNAGYOBB KÖZÖS OSZTÓ

#A számok sorbarendezése.
#Így a legkönnyebb megállapítani, h melyik a legkisebb szám.
szamok.sort()
kisebb = szamok[0]
print(kisebb)

#1-től a legkisebb számíg végigosztjuk mindkét számot,
#és ahol az 'i' A-számmal és B-számmal is osztható
#ott egyenlővé tesszük az 'lnko'-val, hiszen
#akkor megtaláltuk a keresendő számot (vagyis
#a Legnagyobb Közös Osztót.
for i in range(1, kisebb):
    #Ha A-számot maradéktalanul tudjuk osztani az i-számmal,
    #ÉS a B-számot is maradéktalanul tudjuk osztani az i-számmal,
    #akkor...
    if szamok[0]%i == 0 and szamok[1]%i == 0:
        #.. Írja ki az 'i'-t (csak visszajelzésként),
        print('az i =',i)
        #.. az 'i' a keresett Legnagyobb Közös Osztó (LNKO).
        lnko = i
        #----#
        #Esetleg lehetne ide egy 'break'-et tenni,
        #hogy ne számoljon akkor is, ha már megvan az LNKO.
        #----#
    else:
        #Máskülönben nincsen közös osztója a két számunknak.
        print('az', i, 'nem közös osztó')

#Maga az Euklideszi algoritmus:
lkkt = int(szamok[0] * szamok[1] / lnko)
print(lkkt)

#Rem érthető. Ha nem, vagy vmi kérdésed lenne még, akkor írj nyugodtan.
