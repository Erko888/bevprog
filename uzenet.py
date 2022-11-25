def main():
    codedText = """Cbcq Dgyk!
    
    Dmeybh kce cew yrwyg hmrylyaqmr:
    rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!
    
    Aqmimjjyi:
    
    Ynyb"""
    decodedText = ""
    for i in codedText:
        if i == 'y':
            decodedText += 'a'
        elif i == 'z':
            decodedText += 'a'
        elif i == 'Y':
            decodedText += 'A'
        elif i == 'Z':
            decodedText += 'A'
        elif i.isspace():
            decodedText += i
        elif i == '!':
            decodedText += i
        elif i == ':':
            decodedText += i
        else:
            decodedText += chr(ord(i) + 2)
    print(decodedText)


if __name__ == "__main__":
    main()