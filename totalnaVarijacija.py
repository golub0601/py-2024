# Data je matrica (lista listi) proizvoljnog formata m×n. Korišćenjem generatorskih izraza i sum()
# funkcije, izračunati totalnu varijaciju date matrice - zbir apsolutnih razlika između svih parova
# susjednih elemenata. Dva elementa su susjedi ako se nalaze u istoj vrsti i susjednim kolonama, ili u
# istoj koloni i susjednim vrstama. Test primjeri:
# Ulaz Izlaz
# [[100, 120],
#  [110, 150]]
# 100
# [[2, 1, 9],
#  [0, 5, 3],
#  [7, 8, 6]]
# 44
# Pojašenjenje test primjera: |100 - 120| + |110 - 150| + |100 - 110| + |120 - 150| = 20 + 40 + 10 + 30 =
# 100.


a = [[2, 1, 9],
 [0, 5, 3],
 [7, 8, 6]]


def totalnaVarijacija (a):
    sumkol = sum(abs(x[i]-x[i+1]) for x in a for i in range(len(x)-1))
    sumrow = sum(abs(a[i][j]-a[i+1][j]) for i in range(len(a)-1) for j in range(len(a[0]))) 
    return sumkol+sumrow


print(totalnaVarijacija(a))