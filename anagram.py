def check(s1, s2):
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")

def main():
    s1 = "listen"
    s2 = "silent"
    check(s1, s2)

    s3 = "random"
    s4 = "tired"
    check(s3, s4)


if __name__ == "__main__":
    main()