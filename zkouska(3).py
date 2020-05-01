import csv


def main():
    print(
        'Prosíme o strpení. Vzhledem k množství dat, se kterými program pracuje, může načítání trvat i několik desítek minut.'
            )
    ### Vždy budeme načítat jen jeden txt soubor.
    vystup_funkce = nacitaniTxt1('movie_titles.csv', 'cvicny_text_2.txt')


Movies = "movie_titles.csv"
Seen = "cvicny_text_1.txt"


def nacitaniTxt1(Movies, Seen):
    pocatecni_index = input('Zadejte počáteční index filmu: ') # txt soubor s uživateli nezačíná vždy číslem 1
    pocet_filmu = input('Kolik filmů se nachází v knihovně, kterou chcete načíst? ') # v každém txt souboru je jiný počet filmů
    konecny_index = int(pocatecni_index) + int(pocet_filmu)
    MovieID = []
    Titles = []
    uzivatele = []
    seznam_uzivatelu = []
    seznam_filmu = []
    x = list(range(int(pocatecni_index), int(konecny_index)))

    ### Načítá csv a txt soubory, pro další zpracování
    with open(Movies, newline='') as csvFile:
        data = csv.reader(csvFile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)

        for line in data:
            MovieID.append(line[0])
            Titles.append(line[2])
        print('Knihovna filmů byla načtena.')

    with open(Seen, newline='') as txtFile:
        txt = csv.reader(txtFile, delimiter=',', quotechar=':', quoting=csv.QUOTE_MINIMAL)

        for line in txt:
            uzivatele.append(line[0])
        print('Knihovna uživatelů byla načtena.')

    ### Vypíše pozice Movie ID v listu uzivatelu, uživatele jednoho filmu (produktu) jsou ohraničeni čísly filmu (produktu).
    indexy = []
    for i in range(0, len(uzivatele) - 1, 1):
        for index in range(0, len(x), 1):
            seznam_filmu = '%s:' % (x[index])
            if seznam_filmu == uzivatele[i]:
                indexy.append(i)


    posledni_index = len(uzivatele) - 1
    indexy.append(posledni_index)

    ### Vytvoří list uzivatelu pro každý film.
    #### Vytváříme list se všemi filmy a uživateli.
    seznam = []
    for i in range(0, len(indexy) - 1, 1):
        Movie1 = uzivatele[indexy[i]:indexy[i + 1]]
        seznam.append(Movie1)
        print(Movie1)
    print('Seznamy filmů byly načteny.')

    ### Odstraní z listu uživatelů MovieID a vytvoří list pouze s UserID, vytvoří knihovnu pouze s uživateli
    for i in range(0, len(indexy) - 1, 1):
        Movie1 = uzivatele[indexy[i]:indexy[i + 1]]
        del Movie1[0]
        seznam_uzivatelu.append(Movie1)
    print("Seznamy uživetelů byly načteny.")

    ### Pomocí input vložíme UserID, následně projedeme list uzivatele abychom zjistli,
    #### zda se uživatel v knihovně nachází.
    ### Pokud se uživatel v knihovně nachází, vyhledá všechny filmy, které viděl. Vypíše všechny listy s filmy ve kterých se nachází,
    #### do proměnné zhlednuto.
    zhlednuto = []
    a = []
    u = input('Zadejte ID uživatele: ')
    for index in range(0, len(uzivatele), 1):
        if u == uzivatele[index]:
            a = 'Tento uživatel se v knihovně nachází.'
            print(a)
            for i in range(0, len(indexy) - 1, 1):
                Movie1 = uzivatele[indexy[i]:indexy[i + 1]]
                for j in range(0, len(Movie1), 1):
                    if u == Movie1[j]:
                        zhlednuto.append(Movie1)
                        for i in range(0, len(zhlednuto) - 1, 1):
                            if zhlednuto[i] == zhlednuto[i+1]:
                                del zhlednuto[i+1]
            break
    else:
        a = 'Tento uživatel se v knihovně nenachází'
        print(a)

    ### Vrátí názvy filmů, které užiavatel už viděl.
    if a == 'Tento uživatel se v knihovně nachází.':
        zhlednuto.append(zhlednuto[0])
        Names = []
        Title = []
        for i in range(0, len(zhlednuto) - 1, 1):
            Names.append(zhlednuto[i][0])
            Title.append(Names[i].split(':'))

    if a == 'Tento uživatel se v knihovně nachází.':
        Title.append(Title[0])
        for i in range(0, len(Title) - 1, 1):
            print('Tento film jste už viděli: ',Titles[int(Title[i][0]) - 1])
    ### Jak dál? :D



if __name__ == "__main__":
    main()