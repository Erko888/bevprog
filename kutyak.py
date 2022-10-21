class Kutya:
    def __init__(self, kutyaNev, kutyaFaj, kutyaKor):
        self.kutyaNev = kutyaNev
        self.kutyaFaj = kutyaFaj
        if kutyaKor <= 0:
            self.kutyaKor = 0
        else:
            self.kutyaKor = kutyaKor
    def Kor(self):
        print("A kutya {0} éves!" .format(self.kutyaKor))

        
    def ugat(self):
        print("{0}: VAÚ" .format(self.kutyaNev))

def main():
    kutyak = []
    for i in range(3):
        kutyaNev = input("Név: ")
        kutyaFaj = input("Fajta: ")
        kutyaKor = int(input("Kor: "))
        ujkutya = Kutya(kutyaNev, kutyaFaj, kutyaKor)
        kutyak.append(ujkutya)

    for i in range(len(kutyak)):
        print("Név: {0}\nFaj: {1}\nKor: {2}" .format(kutyak[i].kutyaNev, kutyak[i].kutyaFaj, kutyak[i].kutyaKor))
        kutyak[i].ugat()

if __name__ == "__main__":
    main()