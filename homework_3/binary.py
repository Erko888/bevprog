def toBinary(szam):
    if szam >=1:
        toBinary(szam // 2)
    print(szam % 2, end="")

def main():
    toBinary(156)


if __name__ == "__main__":
    main()