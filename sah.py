# 2. Tokom pripreme za šahovski turnir, potrebno je vježbati završnice partija. U tu svrhu treba
# napisati Python skriptu koja za dati skup figura generiše njihov slučajni raspored na tabli dimenzija
# 8×8, korišćenjem funkcionalnosti modula random. Preciznije, zadaje se rječnik u kojem ključevi
# označavaju različite figure, a vrijednosti govore koliko puta se koja figura pojavljuje. Bijele figure
# se označavaju velikim slovima, a crne malim, pri čemu se koristi sljedeća konvencija u oznakama:
# K/k - kralj, Q/q - dama, R/r - top, B/b - lovac, N/n - skakač, P/p - pion. Prazna polja se označavaju
# tačkama. Generisani raspored mora biti validan, tj. moraju biti zadovoljeni sljedeći uslovi:
# - nijedan pion se ne može nalaziti u prvoj ili posljednjoj vrsti
# - kraljevi se ne smiju međusobno napadati, tj. biti u susjednim poljima horizontalno, vertikalno ili
# dijagonalno
# Na primjer, za ulazni rječnik {'K':1, 'R':2, 'P':1, 'k':1, 'r':1, 'n':1, 'p':2}, jedan
# validan izlaz bi mogao da bude:
# . . . . . . . .
# . . . r . . . .
# . . . . . . p k
# . . n . . . . p
# . . P . . . . .
# . . . . . R . .
# . . K . . . . .
# R . . . . . . .
import random
u = {'K':1, 'R':2, 'P': 1, 'k':1, 'r':1, 'n':1, 'p':2}

def printS(r):
    for x in r:
        print(x)
   
def rasporediFiguru(f,counter,result):
    kritFigure = ['K','k', 'P', 'p']
    
    if f not in kritFigure:
       while counter > 0: 
            coordi = random.randint(0,7)
            coordy = random.randint(0,7)
            if result[coordi][coordy] == '.':
                result[coordi][coordy] = f
                counter -=1
    
    elif f == 'P':
        while counter > 0: 
            coordi = random.randint(1,6)
            coordy = random.randint(0,7)
            if result[coordi][coordy] == '.':
                result[coordi][coordy] = 'P'
                counter -=1
                
    elif f == 'p':
        while counter >0: 
            coordi = random.randint(1,6)
            coordy = random.randint(0,7)
            if result[coordi][coordy] == '.':
                result[coordi][coordy] = 'pb'
                counter -=1      
                 
    elif f == 'K':
        while counter > 0:
            coordi = random.randint(0,7)
            coordy = random.randint(0,7)
            if result[coordi][coordy] == '.':
                # result[coordi][coordy]='K'
                if coordi != 0 and result[coordi-1][coordy] != 'k' :
                    if coordy!= 7 and result[coordi-1][coordy+1] != 'k' and result[coordi][coordy+1] != 'k':
                        if coordy!= 0 and result[coordi-1][coordy-1] != 'k' and result[coordi][coordy-1] != 'k':
                            if coordi != 7 and result[coordi+1][coordy] != 'k' :
                                if coordy!= 7 and result[coordi+1][coordy+1] != 'k':
                                    if coordy!= 0 and result[coordi-1][coordy-1] != 'k':
                                        result[coordi][coordy]='K' 
                                        counter -=1          
    elif f == 'k':
        while counter > 0:
            coordi = random.randint(0,7)
            coordy = random.randint(0,7)
            if result[coordi][coordy] == '.':
                if coordi != 0 and result[coordi-1][coordy] != 'K' :
                    if coordy!= 7 and result[coordi-1][coordy+1] != 'K' and result[coordi][coordy+1] != 'K':
                        if coordy!= 0 and result[coordi-1][coordy-1] != 'K' and result[coordi][coordy-1] != 'K':
                            if coordi != 7 and result[coordi+1][coordy] != 'K' :
                                if coordy!= 7 and result[coordi+1][coordy+1] != 'K':
                                    if coordy!= 0 and result[coordi-1][coordy-1] != 'K':
                                        result[coordi][coordy]='k'
                                        counter-=1
    return result
             

def sah(u):
    result = [[('.') for x in range(8)] for y in range(8)]
    
    for f in u:
        result = rasporediFiguru(f, u[f], result)
        
    printS(result)
    

sah(u) 