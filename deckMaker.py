#
# DECK MAKER MAGIC THE GATHERING 1.5
# python (c) REL, 2013
#
#####

import random
import virtualMTG

'''
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



def madeDeck():
    cards = "abcdefghijklmno"
    card_list = list(cards)
    virtualMTG.deck
    for i in range(15):
        for x in range(4):
            deck += card_list[i]
        
    #print deck


madeDeck()











