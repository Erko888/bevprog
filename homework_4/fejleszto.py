class Fejlesztok:
    def __init__(self, nev, fizetes, rang="junior", ev = 0):
        self.nev = nev
        self.rang = rang
        self.fizetes = fizetes
        self.ev = ev

    def fizetesEmeles(self, emeles = 10000):
        self.fizetes += emeles

    def evek(self):
        self.ev+=1

    def rangok(self):
        if self.ev < 1:
            self.rang = "Intern"
        elif self.ev < 3:
            self.rang = "Junior"
        elif self.ev < 5:
            self.rang = "Medior"
        elif self.ev >= 5:
            self.rang = "Senior"
    
    def kiir(self):
        print(self.nev, self.ev, self.fizetes, self.rang) 

def main():
    fejleszto = Fejlesztok("Erik", 1000000)
    fejleszto.fizetesEmeles(20000)
    fejleszto.rangok()
    fejleszto.kiir()
    fejleszto.evek()
    fejleszto.evek()
    fejleszto.evek()
    fejleszto.fizetesEmeles()
    fejleszto.rangok()
    fejleszto.kiir()
    

if __name__ == "__main__":
    main()