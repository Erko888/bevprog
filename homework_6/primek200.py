import primek

def main():
    osszeg = 0;
    for i in range(1,200):
        if primek.is_prime(i):
            osszeg += i
    print(osszeg)



if __name__ == "__main__":
    main()