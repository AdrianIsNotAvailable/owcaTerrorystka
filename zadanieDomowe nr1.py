#Zadanie nr.1

ilekotow = input("podaj ile kotów chcesz mieć : ")

try:
    ilekotow = int(ilekotow)
except ValueError as OwcaError:
    print(f'{OwcaError}, program przyjmuje tylko liczby naturalne')

input (ilekotow * " (=^.^=) ")