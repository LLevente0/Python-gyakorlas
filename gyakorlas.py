def szambekeres():
    szam = int(input("Kérlek adj meg egy számot: "))

    osszeg = 0
    for i in range(1, szam + 1):
        print(i)
        osszeg += i
    print(osszeg)



def jelszobekeres():

    jelszo = "titkos"

    while True:
        bekeres = input("Kérlek add meg a jelszót: ")
        if bekeres == jelszo:
            print("Sikeres bejelentkezés.")
            break

        else:
            print("Sikertelen bejelentkezés. Próbáld újra!")


def eurofizetes():

    euro = int(input("Add meg mennyi euró van nálad! "))
    arfolyam = float(input("Add meg az euró árfolyamát! "))
    ar = int(input("Add meg a termék árát forintban! "))

    forint = euro * arfolyam
    print(f"{forint} forint van nálad.")

    if forint < ar:
        print("A terméket nem tudod megvásárolni.")
    else:
        print("A terméket meg tudod vásárolni.")

eurofizetes()