def main():
    codedText = "kwwsv=22|rxwx1eh2gTz7z<Zj[fT"
    decodedText = ""
    for i in codedText:
        decodedText += chr(ord(i) - 3)
    print(decodedText)

if __name__ == "__main__":
    main()