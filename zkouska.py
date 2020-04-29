import csv
import numpy as np

def main():

    print('Prosíme o strpení. Vzhledem k množství dat, se kterými program pracuje, může načítání trvat i několik desítek minut.')
    ### Vždy budeme načítat jen jeden txt soubor.
    combined_data1 = nacitaniTxt1('movie_titles.csv', 'cvicny_text_1.txt')
    

def nacitaniTxt1(nazev_souboruCsv, nazev_souboruTxt1):
    pocet_filmu = input('Kolik filmů se nachází v knihovně, kterou chceta načíst? ')
    MovieID = []
    Titles = []
    uzivatele = []
    seznam_uzivatelu = []
    seznam_filmu = []
    x = list(range(0,int(pocet_filmu) + 1))

### Načítá csv a txt soubory, pro další zpracování
    with open (nazev_souboruCsv, newline='') as csvFile:
        data = csv.reader(csvFile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)

        for line in data:
            MovieID.append(line[0])
            Titles.append(line[2])
        print('Knihovna filmů byla načtena.')

    with open (nazev_souboruTxt1, newline='') as txtFile:
        txt = csv.reader(txtFile, delimiter=',', quotechar=':', quoting=csv.QUOTE_MINIMAL)

        for line in txt:
            uzivatele.append(line[0])
        print('Knihovna uživatelů byla načtena.')

### Vypíše pozice Movie ID v listu uzivatelu
    indexy = []
    for i in range(0, len(uzivatele) - 1, 1):
        for index in range(0, len(x), 1):
            seznam_filmu = '%s:' % (x[index])
            if seznam_filmu == uzivatele[i]:
                indexy.append(i)
##Jak odstranit ze seznamu uzivatele postupne hodnoty na pozicích v proměnné indexy?

### Vytvoří list uzivatelu pro každý film.
    for i in range(0, len(indexy) - 1, 1):
        Movie1 = uzivatele[indexy[i]:indexy[i+1]]
        print(Movie1)
    print('Seznamy filmů byly načteny.')
##Vypsání i posledního stringu filmů? Jak vytvořit proměnné s listem pro každý film?

### Odstraní z listu uživatelů MovieID a vytvoří list pouze s UserID


    
    
### Pomocí input vložíme UserID, následně projedeme list uzivatele abychom zjistli,
#### zda se uživatel v knihovně nachází.
    ### Pokud se uživatel v knihovně nachází, vyhledá všechny filmy, které viděl. Vypíše všechny listy s filmy ve kterých se nachází,
    #### do proměnné zhlednuto.
    zhlednuto = []
    u = input('Zadejte ID uživatele: ')
    for index in range(0, len(uzivatele), 1):
        if u == uzivatele[index]:
            print('Tento uživatel se v knihovně nachází.')
            for i in range(0, len(indexy) - 1, 1):
                Movie1 = uzivatele[indexy[i]:indexy[i + 1]]
                for j in range(0, len(Movie1), 1):
                    if u == Movie1[j]:
                        zhlednuto.append(Movie1)
                        ### Jak docílit toho, aby se proměnná se zhlédnutým filmem a uživateli načetla jen jednou?
    print(zhlednuto)
    ### Jak dál? :D

if __name__ == "__main__":
    main()