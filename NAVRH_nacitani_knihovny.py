"""Návrh na grafickou tabulku, u mě kód funguje (nahází mi error :D), ale tabulku nechce otevřít v prohlížeči

pip install plotly==4.6.0 - instalační balíček pro grafické prvky, nutno napsat do terminálu

import plotly.graph_objects as go

knihovna = go.Figure(data=[go.Table(header=dict(values=['ID filmu', 'ID uživatele', 'Hodnocení filmu', 'Datum hodnocení']),
                                    cells=dict(values=[[1547], [1586], '5/10', '11.07.2016']))])

knihovna.show()"""

import csv

""" Funkce pro načítání knihovny dat ve formátu .csv,
    :nazev_souboru = název souboru, který chceme načíst
    :výstup funkce: načtená knihovna ve formátu - 1. řádek obsahuje názvy proměnných, ostatní řádky obsahují hodnoty
    proměnných v poředí"""

def main():
    knihovna = nacteni_knihovny_dat('cvicna_knihovna.csv')

def nacteni_knihovny_dat(nazev_souboru):

    with open(nazev_souboru, 'r') as myFile:
        lines = csv.reader(myFile, delimiter=',')
        for line in lines:
            print(line)


if __name__ == "__main__":
    main()

""" Vytahování dat z načtené knihovny - netuším jak dál! Vždy mi to napíše KeyError když se snažím vytáhnout ty konkrétní
hodnoty.
:https://docs.python.org/3/library/csv.html
:https://towardsdatascience.com/an-overview-of-importing-data-in-python-ac6aa46e0889 ,
tady jsou odkazy odkud jsem čerpala při načítání knihovny a když jsem se snažila vytáhnout data, třeba uvidíte něco,
co já ne :D. Podle mě ta tabulka vytvořená pomocí toho DictReader není správně, ale nevím jak to spravit. Byly 2 návrhy
jak vytáhnout data z knihovny a to
:print(line[nazev proměnné])
:pole1.append(line[nazev proměnné])
nefungovalo mi ani jedno, pokaždé jen KeyError"""


with open('cvicna_knihovna.csv', newline='') as myFile:
    lines = csv.DictReader(myFile)
    for line in lines:
        print(line)


