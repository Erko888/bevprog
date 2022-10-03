def main():
    szam = int(input("Adj meg egy számot: "))
    original = szam
    reverse = 0

    while(szam > 0):
        digit = szam % 10 #utolso szamjegy
        reverse = reverse * 10 + digit
        szam = szam / 10

    if original == reverse:
        print("A szám tükör szám!")
    else:
        print("A szám nem tükör szám!")

if __name__ == "__main__":
    main()