import primek

def main():
    for i in range(1, 100):
        if primek.is_prime(i):
            print(i)

if __name__ == "__main__":
    main()