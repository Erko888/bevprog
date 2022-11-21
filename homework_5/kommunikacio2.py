def main():
    f = open("D:/bevprog/homework_5/comm.txt", "a")
    favNum = int(input("Add meg a kedvenc szamod: "))
    for i in range(0, favNum):
        f.write(str(favNum))

if __name__ == "__main__":
    main()