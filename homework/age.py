def main():
    yourAge = int(input("How old are you: "))
    americanLegalDrinkingAge = 21
    abletoBuyCigarettesHungary = 18
    abletoGetDriversLicenseHungary = 16
    shrek2AgeLimit = 12

    if yourAge>=americanLegalDrinkingAge:
        print("You can legally drink in the USA")
    else:
        print("You are not allowed to legally drink in the USA")
    
    if yourAge>=abletoBuyCigarettesHungary:
        print("You can legally buy cigarettes in Hungary")
    else:
        print("You can't legally buy cigarettes in Hungary")
    
    if yourAge>=abletoGetDriversLicenseHungary:
        print("You can go and get your drivers license in Hungary")
    else:
        print("You can't get your drivers license in Hungary yet")
    
    if yourAge>=shrek2AgeLimit:
        print("You can watch Shrek 2")
    else:
        print("You can't watch Shrek 2 yet")
    
if __name__ == "__main__":
    main()