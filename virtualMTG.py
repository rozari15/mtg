#
# VIRTUAL MAGIC THE GATHERING 1.0
# python (c) REL, 2013
#
#####

from deckMaker import deck1
import random

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

deck = [a, a, a, a, b, b, b, b, c, c, c, c, d, d, d, d, e, e, e, e,
        f, f, f, f, g, g, g, g, h, h, h, h, i, i, i, i, j, j, j, j,
        k, k, k, k, l, l, l, l, m, m, m, m, n, n, n, n, o, o, o, o]

deck = random.shuffle(deck)
'''


x = 0

print "Opening hand:"
for x in range(7):
    print deck1
    x += 1
'''


while (x < len(deck) - 1):
    n = random.randint(0, len(deck) - 1)
    print deck[n]
    del(deck[n])
    x += 1
'''
'''
print "Next draws:" 
while(len(deck) > 0):
    n = random.randint(0, len(deck) - 1)
    print deck[n]
    del(deck[n])
'''


mulligan = str(raw_input('Keep or Mulligan? (k/m) '))
if (mulligan == 'k'):
    print 1

elif (mulligan == 'm'):
    print 2

else:
    print 'k/m only'
 
