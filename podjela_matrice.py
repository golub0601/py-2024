a = [
    [1,1,1,2,2,2],
    [3,3,3,4,4,4],
    [5,5,5,6,6,6],
    [7,7,7,8,8,8]
]
m = len(a)
n = len(a[0])
h = 2
w = 3

cells = [
    [[a[i+i1][j+j1] for j1 in range(w)] for i1 in range(h)]
    for i in range(0, m, h) for j in range(0, n, w)
]

for cell in cells:
    print(*cell, sep='\n')
    print()