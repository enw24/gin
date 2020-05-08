import random
deck = []
suits = ["S","C","D","H"]
p1 = []
AI = []
pile = []
K = []
A = []
ten = []
remove = []
count = 0


def decksetup():
    for x in suits:
        for i in range(2, 11):
            deck.append(x + str(i))
        deck.append(x + "A")
        deck.append(x + "J")
        deck.append(x + "Q")
        deck.append(x + "K")
    random.shuffle(deck)

def deal():
    for i in range(20):
        if i%2 == 0:
            p1.append(deck[i])
        else:
            AI.append(deck[i])
    while len(deck)>32:
        deck.pop(0)
    pile.append(deck[0])
    deck.pop(0)
    pile.append("X")

def update():
    index = 9
    p1.sort(key = lambda p1: p1[1])
    AI.sort(key = lambda AI: AI[1])
    for i in p1:
        if "A" in i:
            remove.append(i)
            A.append(i)
        elif "K" in i:
            remove.append(i)
            K.append(i)
        elif "10" in i:
            remove.append(i)
            ten.append(i)
    for x in remove:
        if x in p1:
            p1.remove(x)
    for l in p1:
        if "J" in l:
            index = p1.index(l)
            break
        elif "Q" in l:
            index = p1.index(l)
            break
        elif "K" in l:
            index = p1.index(l)
            break
    for i in ten:
        p1.insert(index, i)

    for i in A:
        p1.insert(0, i)

    for i in K:
        p1.insert(9, i)
    remove.clear()
    A.clear()
    K.clear()
    ten.clear()

    index=9
    for i in AI:
        if "A" in i:
            remove.append(i)
            A.append(i)
        elif "K" in i:
            remove.append(i)
            K.append(i)
        elif "10" in i:
            remove.append(i)
            ten.append(i)
    for x in remove:
        if x in AI:
            AI.remove(x)
    for l in AI:
        if "J" in l:
            index = AI.index(l)
            break
        elif "Q" in l:
            index = AI.index(l)
            break
        elif "K" in l:
            index = AI.index(l)
            break
    for i in ten:
        AI.insert(index, i)

    for i in A:
        AI.insert(0, i)

    for i in K:
        AI.insert(9, i)
    remove.clear()
    A.clear()
    K.clear()
    ten.clear()

    print(AI)
    print()
    print()
    print("                      ", "Deck", " ", pile[0])
    print()
    print()
    print(p1)
    print()
    print()

def player1():
    while True:
        try:
            move = input("Deck or pile? ").upper()
            if move == "PILE":
                break
            elif move == "DECK":
                break

        except:
            print("invalid entry")
            continue
    if move == "PILE":
        p1.append(pile[0])
        pile.pop(0)
    else:
        p1.append(deck[0])
        deck.pop(0)
    print(AI)
    print()
    print()
    print("                      ", "Deck", " ", pile[0])
    print()
    print()
    print(p1)
    print()
    print()
    x = True
    while x == True:
        try:
            discard = input("Discard? ").upper()
            print()
            print()
            for i in p1:
                if i == discard:
                    x = False
        except:
            print("invalid input")
            continue
    pile.insert(0, discard)
    p1.remove(discard)

def computer():
    AI.append(deck[0])
    deck.pop(0)
    pile.insert(0, AI[0])
    AI.remove(AI[0])

#help from dad
def won1():
    hand = []
    listof4 = []
    listof3 = []
    possible3s = []
    final = []
    count = 0

    for i in range(0, 52):
        hand.append(0)

    for x in suits:
        for c in p1:
            if x in c:
                if "A" in c:
                    hand[1 + count] = 1
                elif "K" in c:
                    hand[13 + count] = 1
                elif "Q" in c:
                    hand[12 + count] = 1
                elif"J" in c:
                    hand[11 + count] = 1
                else:
                    hand[int(c[1:])+count] = 1
        count += 13

    # creates list of all runs of three same numbers
    for i in range(1, 13):
        if (hand[i] + hand[i + 13] + hand[i + 26] + hand[i + 39] == 4):
            listof4.append([i, i + 13, i + 26, i + 39])
        if (hand[i] + hand[i + 13] + hand[i + 26] + hand[i + 39] == 3):
            if (hand[i] == 0):
                listof3.append([i + 13, i + 26, i + 39])
            elif (hand[i + 13] == 0):
                listof3.append([i, i + 26, i + 39])
            elif (hand[i + 26] == 0):
                listof3.append([i, i + 13, i + 39])
            else:
                listof3.append([i, i + 13, i + 26])

    # adds to list all runs of 3
    for i in range(1, 11):
        if (hand[i] + hand[i + 1] + hand[i + 2] == 3):
            listof3.append([i, i + 1, i + 2])
    for i in range(14, 24):
        if (hand[i] + hand[i + 1] + hand[i + 2] == 3):
            listof3.append([i, i + 1, i + 2])
    for i in range(27, 37):
        if (hand[i] + hand[i + 1] + hand[i + 2] == 3):
            listof3.append([i, i + 1, i + 2])
    for i in range(40, 50):
        if (hand[i] + hand[i + 1] + hand[i + 2] == 3):
            listof3.append([i, i + 1, i + 2])

    # adds to list all runs of 4
    for i in range(1, 10):
        if (hand[i] + hand[i + 1] + hand[i + 2] + hand[i + 3] == 4):
            listof4.append([i, i + 1, i + 2, i + 3])
    for i in range(14, 23):
        if (hand[i] + hand[i + 1] + hand[i + 2] + hand[i + 3] == 4):
            listof4.append([i, i + 1, i + 2, i + 3])
    for i in range(27, 36):
        if (hand[i] + hand[i + 1] + hand[i + 2] + hand[i + 3] == 4):
            listof4.append([i, i + 1, i + 2, i + 3])
    for i in range(40, 49):
        if (hand[i] + hand[i + 1] + hand[i + 2] + hand[i + 3] == 4):
            listof4.append([i, i + 1, i + 2, i + 3])

    if len(listof4) > 0 and len(listof3) > 1:  # if have at least 1 run of 4 and 2 runs of 3, then check for contention
        for x in listof4:
            final.clear()
            for y in listof3:
                overlap = 0
                for j in x:
                    for z in y:
                        # print(j, z)
                        if z == j:
                            overlap = 1
                if overlap == 0:
                    possible3s.append(y)  # appends a list of 3 that is independent
            possible3length = len(possible3s)
            if possible3length > 1:  # if there are 2 groups of 3, then check for contention within them
                for a in possible3s:  # scans one less than total length
                    good3s = 1
                    for b in possible3s:
                        for z in range(0, 2):
                            if not (a == b) and (a[z] == b[0] or a[z] == b[2] or a[z] == b[2]):
                                good3s = 0
                    if good3s == 1:
                        final.append(a)
            if len(final) > 1:
                final.append(x)

    if len(final) == 3:
        return True
    else:
        hand.clear()
        listof4.clear()
        listof3.clear()
        possible3s.clear()
        final.clear()
        return False

def won2():
    hand = []
    listof4 = []
    listof3 = []
    possible3s = []
    final = []
    count = 0

    for i in range(0, 52):
        hand.append(0)

    for x in suits:
        for c in AI:
            if x in c:
                if "A" in c:
                    hand[1 + count] = 1
                elif "K" in c:
                    hand[13 + count] = 1
                elif "Q" in c:
                    hand[12 + count] = 1
                elif"J" in c:
                    hand[11 + count] = 1
                else:
                    hand[int(c[1:])+count] = 1
        count += 13

    # creates list of all runs of three same numbers
    for i in range(1, 13):
        if (hand[i] + hand[i + 13] + hand[i + 26] + hand[i + 39] == 4):
            listof4.append([i, i + 13, i + 26, i + 39])
        if (hand[i] + hand[i + 13] + hand[i + 26] + hand[i + 39] == 3):
            if (hand[i] == 0):
                listof3.append([i + 13, i + 26, i + 39])
            elif (hand[i + 13] == 0):
                listof3.append([i, i + 26, i + 39])
            elif (hand[i + 26] == 0):
                listof3.append([i, i + 13, i + 39])
            else:
                listof3.append([i, i + 13, i + 26])

    # adds to list all runs of 3
    for i in range(1, 50):
        if (hand[i] + hand[i + 1] + hand[i + 2] == 3):
            listof3.append([i, i + 1, i + 2])

    # adds to list all runs of 4
    for i in range(1, 49):
        if (hand[i] + hand[i + 1] + hand[i + 2] + hand[i + 3] == 4):
            listof4.append([i, i + 1, i + 2, i + 3])


    if len(listof4) > 0 and len(listof3) > 1:  # if have at least 1 run of 4 and 2 runs of 3, then check for contention
        for x in listof4:
            final.clear()
            for y in listof3:
                overlap = 0
                for j in x:
                    for z in y:
                        # print(j, z)
                        if z == j:
                            overlap = 1
                if overlap == 0:
                    possible3s.append(y)  # appends a list of 3 that is independent
            possible3length = len(possible3s)
            if possible3length > 1:  # if there are 2 groups of 3, then check for contention within them
                for a in possible3s:  # scans one less than total length
                    good3s = 1
                    for b in possible3s:
                        for z in range(0, 2):
                            if not (a == b) and (a[z] == b[0] or a[z] == b[2] or a[z] == b[2]):
                                good3s = 0
                    if good3s == 1:
                        final.append(a)
            if len(final) > 1:
                final.append(x)


    if len(final) == 3:
        return True
    else:
        hand.clear()
        listof4.clear()
        listof3.clear()
        possible3s.clear()
        final.clear()
        return False

def game():
    win = False
    decksetup()
    deal()
    update()
    while win == False:
        player1()
        if won1() == True:
            win == True
            print("you win")
            break
        update()
        computer()
        if won2() == True:
            win == True
            print("you lose")
            break
        update()

game()