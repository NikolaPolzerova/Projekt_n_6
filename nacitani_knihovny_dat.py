import csv
from random import randint

""" Funkce pro načítání knihovny dat ve formátu .csv,
    :vystupní data: nazev_souboru = název souboru, který chceme načíst
    :výstup funkce: načtená knihovna ve formátu - 1. řádek obsahuje názvy proměnných, ostatní řádky obsahují hodnoty
    proměnných v poředí"""

def main():
    knihovna = nacitani_knihovny('movie_titles.csv')


def nacitani_knihovny(nazev_souboru):
    MovieID = []
    Titles = []

    with open (nazev_souboru, newline='') as csvFile:
        data = csv.DictReader(csvFile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)

        for line in data:
            MovieID.append(line['MovieID'])
            Titles.append(line[' Title'])
 #           print(line['MovieID'], line[' Title'])

if __name__ == "__main__":
    main()