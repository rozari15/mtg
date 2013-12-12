#
# VIRTUAL MAGIC THE GATHERING 1.5
# python (c) REL, 2013
#
#####

import deckMaker
import random
import mulligan



x = 0
i = 0
deck = []

def openingHand(str, int):
    deckMaker.madeDeck()
    print str
    for i in range(int):
        print deckMaker.deck[i]
        i += 1

def mulligan():
    mulligan = str(raw_input('Keep or Mulligan? (k/m) '))
    if (mulligan == 'k'):
        pass

    elif (mulligan == 'm'):
        openingHand('Redraw', 6)
        
    else:
        print 'k/m only'
        mulligan()
      

openingHand('Opening Hand:', 7)
mulligan()
    


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


