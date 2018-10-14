licznik = 0
liczba = 1
kot = '(=^.^=)'
wysokoscSchodow = int(input('Jak wysokie mają być schody : '))
print('\n')
while licznik < wysokoscSchodow:
    licznik += 1
    kot1 = ''
    for i in range(0, licznik):
        kot1 = kot1 + kot   
    print(kot1)
print('\n')
input('Naciśnij ENTER aby wyjść')

