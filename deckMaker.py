#
# DECK MAKER MAGIC THE GATHERING 1.0
# python (c) REL, 2013
#
#####

import random


a = "card1"
b = "card2"
c = "card3"
d = "card4"
e = "card5"
f = "card6"
g = "card7"
h = "card8"
i = "card9"
j = "card10"
k = "card11"
l = "card12"
m = "card13"
n = "card14"
o = "card15"

deck = [a, a, a, a, b, b, b, b, c, c, c, c, d, d, d, d, e, e, e, e, f, f, f, f,
        g, g, g, g, h, h, h, h, i, i, i, i, j, j, j, j, k, k, k, k, l, l, l, l,
        m, m, m, m, n, n, n, n, o, o, o, o]


shuffled = random.shuffle(deck)

'''

class Deck(object):
    def __init__(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o):

        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.i = i
        self.j = j
        self.k = k
        self.l = l
        self.m = m
        self.n = n
        self.o = o

        self.deck = [a, a, a, a, b, b, b, b, c, c, c, c, d, d, d, d, e, e, e, e, f, f, f, f,
        g, g, g, g, h, h, h, h, i, i, i, i, j, j, j, j, k, k, k, k, l, l, l, l,
        m, m, m, m, n, n, n, n, o, o, o, o]

    def Shuffle(self):
        while (x < len(self.deck) - 1):
            n = random.randint(0, len(self.deck) - 1)
            print self.deck[n]
            del(self.deck[n])
            x += 1


deck1 = Deck(a = "card1",
    b = "card2",
    c = "card3",
    d = "card4",
    e = "card5",
    f = "card6",
    g = "card7",
    h = "card8",
    i = "card9",
    j = "card10",
    k = "card11",
    l = "card12",
    m = "card13",
    n = "card14",
    o = "card15")


x = 0

print "Opening hand:"
for x in range(7):
    print Deck.Shuffle(deck1[x])
    x += 1
'''

    











