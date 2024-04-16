# 6. Za datu matricu (listu listi) i cijele brojeve h i w, napisati list comprehension izraz koji vrši
# podjelu date matrice na disjunktne podmatrice dimenzija h×w. Ako su dimenzije ulazne matrice
# m×n, pretpostaviti da će m uvijek biti djeljivo sa h, i n će uvijek biti djeljivo sa w.
# Test primjer za h = 2 i w = 3:
# Ulaz Izlaz Pojašnjenje
# [[1,1,1,2,2,2],
#  [3,3,3,4,4,4],
#  [5,5,5,6,6,6],
#  [7,7,7,8,8,8]]
# [
#  [[1,1,1],
#  [3,3,3]],
#  [[2,2,2],
#  [4,4,4]],
#  [[5,5,5],
#  [7,7,7]],
#  [[6,6,6],
#  [8,8,8]]
# ]
# 1,1,1 | 2,2,2
# 3,3,3 | 4,4,4
# -------------
# 5,5,5 | 6,6,6
# 7,7,7 | 8,8,8

u = [
    [1,1,1,2,2,2],
    [3,3,3,4,4,4],
    [5,5,5,6,6,6],
    [7,7,7,8,8,8]
    ]

def podijeli(u, h, w):
    x = ([[u[j][i] for i in range(w)] for j in range(h)])
    return x
print(podijeli(u, 2,3))
