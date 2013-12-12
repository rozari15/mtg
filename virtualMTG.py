#
# VIRTUAL MAGIC THE GATHERING 1.5
# python (c) REL, 2013
#
#####

import deckMaker
import random
import mulligan



i = 0

def openingHand(str, int):
    shuffled = random.shuffle(deckMaker.deck)
    print str
    for i in range(int):
        print deckMaker.deck[i]
        i += 1


      

openingHand('Opening Hand:', mulligan.x)
mulligan.mulligan()
    


