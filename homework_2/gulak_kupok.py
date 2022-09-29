import math
from cmath import pi

def kor():
    r = int(input("Add meg a kör sugarát: "))
    korT = r*r*pi
    return korT

def teglalap():
    a = int(input("Add meg a téglalap a oldalát: "))
    b = int(input("Add meg a téglalap b oldalát: "))
    teglalapT = a *b
    return teglalapT

def main():
    m = int(input("Add meg a magasságot: "))
    gulaTerfogat = teglalap()*m/3
    kupTerfogat = kor()*m/3

    print("A gúla térfogata: {0}" .format(gulaTerfogat))
    print("A kúp térfogata: {0}".format(kupTerfogat))

if __name__ == "__main__":
    main()