def insert(text, word, insertWord):
    textList = list(text)
    if word not in text:
        print("A szó nincs benne a szövegben!")
    else:
        textList.insert(text.find(word), "{0} ".format(insertWord))
        return "".join(textList)

def main():
    print(insert("Az egy bögre", "bögre", "piros"))

if __name__ == "__main__":
    main()