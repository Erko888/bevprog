def main():
    f = open("D:/bevprog/homework_5/pivers.txt", "r")
    lines = f.readlines()
    f.close()
    f = open("D:/bevprog/homework_5/pivers_Elsoszamjegy", "w")
    for i in lines:
        i = i.split(' ')
        print(len(i[0]), file=f)
    f.close()


if __name__ == "__main__":
    main()