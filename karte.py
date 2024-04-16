# 5. Špil karata za poker sastoji se od 52 karte. One su podijeljene u 4 boje, a od svake boje postoji 13
# karata različitih jačina (2, 3, ..., 9, 10, J - žandar, Q - dama, K - kralj, A - as). 
# Korišćenjem modula random, napisati Python funkciju koja simulira izvlačenje slučajne ruke od 5 karata,
# a zatim napisati funkcije koje estimiraju vjerovatnoću izvlačenja sljedećih kombinacija karata:
# a) full house (0.1441%) - tri karte jedne jačine i dvije karte neke druge jačine (npr. tri kralja i
# dvije devetke)
# b) dva para (4.7539%) - dvije karte jedne jačine i dvije karte neke druge jačine, pri čemu peta
# karta može biti proizvoljna ali ne od jedne od prethodnih jačina (npr. dva žandara, dvije petice i
# jedan as)
# Vjerovatnoća određene kombinacije se estimira tako što se simulira izvlačenje N puta, a zatim se
# izračuna koliki procenat od tih N ruka predstavlja traženu kombinaciju. N uzeti proizvoljno (npr.
# 1000, 10000...).


import random

def hand(deck):
    r = random.sample(population=deck, k=5)
    return r
# hand1 = [(1,2),(1,1),(2,3),(2,1),(5,2)]

def isCouple(hand):
    cntD = {j1 :sum(1 for i,j in hand if i==j1) for j1 in range(1,14)}
    ind=0
    
    for el in cntD:
        if cntD[el] == 2:
            ind+=1 
            
    if ind == 2:
        return True
    else:
        return False
    
def isHouse(hand):
    cntD = {j1 :sum(1 for i,j in hand if i==j1) for j1 in range(1,14)}
    ind1=0
    ind2=0
    for el in cntD:
        if cntD[el] == 2:
            ind1+=1 
        elif cntD[el] == 3:
            ind2+=1
    if ind1 == 1 and ind2 == 1:
        return True
    else:
        return False
    
def calculate(noDraws):
    deck = [(x,y) for x in range(1,14) for y in range(1,5)]
    noCouples = 0
    noHouses = 0
    for i in range(noDraws):
        currHand = hand(deck)
        if isCouple(currHand):
            noCouples += 1
        elif isHouse(currHand):
            noHouses += 1
    percentCouples = noCouples / noDraws * 100
    percentHouses = noHouses / noDraws * 100
    return percentCouples, percentHouses
    

print(calculate(10000))