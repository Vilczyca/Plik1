# input pobiera ciąg znaków od urzytkownika
koteł = "=^-w-^="
imie = input("Cześć, podaj swoje imie: ")
iloscKotełów = input ("Ile chcesz kotów?  ")

try:
    iloscKotełów = int(iloscKotełów)
except ValueError as owcaError:
    print("Podałeś błędny numer karty")
    iloscKotełów = 7

    #Zadanie domowe
    """
    Napisać program który generuje dowolną piramidę z kotełów.

    Założenia:
    Jeżeli użytkownik wpisze liczbe ujemną będzie krzyczeć i wpisze do konsoli =^!^=

Liczba = 3
"=^-w-^="
"=^-w-^=""=^-w-^="
"=^-w-^=""=^-w-^=""=^-w-^="
Hint: Pętle for i if
"""



