import csv

def main():

    print('Prosíme o strpení. Vzhledem k množství dat, se kterými program pracuje, může načítání trvat i několik desítek minut.')

    combined_data1 = nacitaniTxt1('combined_data_1.txt')
    combined_data2 = nacitaniTxt2('combined_data_2.txt')
    combined_data3 = nacitaniTxt3('combined_data_3.txt')
    combined_data4 = nacitaniTxt4('combined_data_4.txt')

def nacitaniTxt1(nazev_souboruTxt):
    UserID1 = []
    Rating1 = []
    DateOfRating1 = []

    with open (nazev_souboruTxt, newline='') as txtFile:
        txt = csv.DictReader(txtFile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)


        for line in txt:
            UserID1.append(line['UserID'])
#            Rating1.append(line[' Rating'])
#            DateOfRating1.append(line[' DateOfRating'])
        print(UserID1[1])

def nacitaniTxt2(nazev_souboruTxt):
    UserID2 = []
    Rating2 = []
    DateOfRating2 = []

    with open (nazev_souboruTxt, newline='') as txtFile:
        txt = csv.DictReader(txtFile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)


        for line in txt:
            UserID2.append(line['UserID'])
#            Rating2.append(line[' Rating'])
#            DateOfRating2.append(line[' DateOfRating'])
        print(UserID2[1])

def nacitaniTxt3(nazev_souboruTxt):
    UserID3 = []
    Rating3 = []
    DateOfRating3 = []

    with open (nazev_souboruTxt, newline='') as txtFile:
        txt = csv.DictReader(txtFile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)


        for line in txt:
            UserID3.append(line['UserID'])
#            Rating3.append(line[' Rating'])
#            DateOfRating3.append(line[' DateOfRating'])
        print(UserID3[1])

def nacitaniTxt4(nazev_souboruTxt):
    UserID4 = []
    Rating4 = []
    DateOfRating4 = []

    with open (nazev_souboruTxt, newline='') as txtFile:
        txt = csv.DictReader(txtFile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)


        for line in txt:
            UserID4.append(line['UserID'])
#            Rating4.append(line[' Rating'])
#            DateOfRating4.append(line[' DateOfRating'])
        print(UserID4[1])


if __name__ == "__main__":
    main()