ilekotow = input("podaj ile kotów chcesz mieć : ")
#print('ilekotow jest : ', type(ilekotow) )

try:
    ilekotow = int(ilekotow)
except ValueError as owcaError:
    print(f'{owcaError}, program przyjmuje tylko liczby naturalne')




input (ilekotow * " (=^.^=) ")