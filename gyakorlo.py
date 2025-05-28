"""1. Egyszerű számbekérő
Kérj be egy számot a felhasználótól, és döntsd el, hogy páros vagy páratlan. Írd ki az eredményt!
Pl. 5
print:
Az 5-ös szám páratlan szám.
"""

def szambekero():
    szam = int(input("Kérlek adj meg egy számot: "))

    if szam % 2 == 0:
        print(f"Ez a szám {szam} és páros.")
    else:
        print(f"Ez a szám {szam} és páratlan.")



"""
2. Összegszámítás
Kérj be egy egész számot, és számítsd ki az 1-től a megadott számig terjedő egész számok összegét.
pl. 7
print:
1
2
3
4
5
6
7
"""

def osszegszamitas():
    szam = int(input("Adj meg egy egész számot: "))

    osszeg = 0

    for i in range(1, szam + 1):
        print(i)
        osszeg += i

    print("Összeg:", osszeg)






"""
3. Számok listázása és összegzése
a) Írj egy programot, amely bekér n számot a felhasználótól, majd egy while ciklussal megkérdezi a felhasználót, 
hogy szeretne-e újabb számot megadni. Addig folytassa a program a számok bekérését, amíg a felhasználó igennel válaszol.
A program végén jelenítse meg a bekért számok összegét.
Pl. 5
    igen
    6
    nem

print: A számok összege: 11
"""

def listazas():
    szamok = []
    szam = int(input("Kérlek adj meg egy számot: "))
    szamok.append(szam)

    while True:
        valasz = input("Szeretnél új számot megadni? ").strip().lower()
        if valasz == "igen":
            szam = int(input("Kérlek adj meg egy számot: "))
            szamok.append(szam)
        elif valasz == "nem":
            break


    print(szamok)
listazas()




"""
b) jelenítsd meg a bekért számokat (lista használata)
Pl. 5
    igen
    6
    nem

print: A számok: [5, 6]
"""
