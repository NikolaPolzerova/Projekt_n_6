def main():
    """Hlavní funkce byla spuštěna."""
    print("Hlavní funkce byla spuštěna.")
    vysledek = get_center_distance(2, 5, 3, 4, 3, 2)
    prunik = find_intersection(2, 5, 3, 4, 3, 2)
    print(vysledek, prunik)

def get_center_distance(x_a, y_a, r_a, x_b, y_b, r_b):
    vypocet = ((x_a - x_b)**2 + (y_a - y_b)**2) ** (1/2)
    return vypocet

def find_intersection(x_a, y_a, r_a, x_b, y_b, r_b):
    vzdalenost = get_center_distance(x_a, y_a, r_a, x_b, y_b, r_b)
    if vzdalenost < (r_a + r_b):
        return True, 'Dané kružnice se protínají.'
    else:
        print('Dané kružice se neprotínají.')

if __name__ == "__main__":
    main()





### ošetřit případ že je jedna kružnice v druhé!!!
