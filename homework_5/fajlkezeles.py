def main():
    f = open("D:/bevprog/homework_5/string1.py", "r")
    lines = f.readlines()
    f.close()
    f = open("D:/bevprog/homework_5/string1_clean.py", "w")
    for line in lines:
        if "#" not in line:
            f.write(line)

        
if __name__ == "__main__":
    main()