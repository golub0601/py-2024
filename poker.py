import random

deck = [(i, j) for i in range(4) for j in range(13)]

# random.shuffle(deck)
# hand = deck[:5]
# print(hand)

# hand = random.sample(deck, 5)
# print(hand)

n = 100000

cnt_full = 0
cnt_2pairs = 0

for _ in range(n):

    hand = random.sample(deck, 5)

    cnts = {j:sum(1 for _, j1 in hand if j1 == j) for j in range(13)}

    # full
    ind3 = False
    ind2 = False
    for cnt in cnts.values():
        if cnt == 3:
            ind3 = True
        if cnt == 2:
            ind2 = True
    if ind2 and ind3:
        cnt_full += 1
    
    # 2 para
    ind21 = False
    ind22 = False
    for cnt in cnts.values():
        if cnt == 2:
            if not ind21:
                ind21 = True
            else:
                ind22 = True
    if ind21 and ind22:
        cnt_2pairs += 1

print(100 * cnt_full / n)
print(100 * cnt_2pairs / n)