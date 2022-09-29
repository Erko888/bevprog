def fibonacci(n):
    if n<= 0:
        print("Nagyobbnak kell lennie mint 0!")
    elif n<=2:
        return n-1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    


def main():
    n = int(input("Adj meg egy 0-nál nagyobb számot: "))
    print(fibonacci(n))


if __name__ == "__main__":
    main()