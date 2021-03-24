import random


# zdefiniowanie pogrubienia jako klasa
class bcolors:
    BOLD = '\033[1m'
    BOLD0 = '\033[0m'


# stworzenie dictionary, kluczy i przypisanie im wartości. Stąd gracz i pc czerpią values
wybor = {"p": "Papier", "k": "Kamień", "n": "Nożyce"}
print("Zagrajmy w grę: ")


def pkn():  # stworzenie funkcji wypisująca wartości ze słownika
    for key, value in wybor.items():
        print(value, '-', key)
    print(end='\n')


pkn()  # odpalenie funkcji wypisującej słownik


# pętla przeszukująca itemy w słowniku i jeśli klucz słownika równa się inputowi gracza to wypisuje wartość tego klucza
def gracz():
    for key, value in wybor.items():
        if x == key:
            print(f'Ty: {bcolors.BOLD}{value}{bcolors.BOLD}{bcolors.BOLD0}')


def PC():
    pc = random.choice(list(wybor.values()))  # losowy wybór komputera, konwersja dict na liste
    print(f'PC: {bcolors.BOLD}{pc}{bcolors.BOLD}{bcolors.BOLD0}\n')
    for key, value in wybor.items():
        if pc == value:
            val = key
            if val == x:
                print("Remis")
            elif val == "p" and x == "n":
                print("Nożyce przecinają papier - Wygrywasz")
            elif val == "n" and x == "p":
                print("Nożyce przecinają papier - Przegrywasz")
            elif val == "p" and x == "k":
                print("Papier przykrywa kamień - Przegrywasz")
            elif val == "k" and x == "p":
                print("Papier przykrywa kamień - Wygrywasz")
            elif val == "k" and x == "n":
                "Kamień tępi nożyczki - Przegrywasz"
            elif val == "n" and x == "k":
                print("Kamień tępi nożyczki - Wygrywasz")
            else:
                print("Błąd, zagraj jeszcze raz.")


i = 1
while i > 0:
    x = input("Co wybierasz? ")
    gracz()
    PC()
    print("\n")
else:
    print("Gra skończona")


