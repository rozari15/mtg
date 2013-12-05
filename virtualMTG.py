#
# VIRTUAL MAGIC THE GATHERING 1.0
# python (c) REL, 2013
#
#####

import deckMaker
import random
import mulligan



x = 7
i = 0

def openingHand(str, x):
    shuffled = random.shuffle(deckMaker.deck)
    print str
    for i in range(x):
        print deckMaker.deck[i]
        i += 1

def mulligan():
    mulligan = str(raw_input('Keep or Mulligan? (k/m) '))
    if (mulligan == 'k'):
        pass

    elif (mulligan == 'm'):
        a = 'Redraw:'
        openingHand(a, 6)
    
    else:
        print 'k/m only'
      

openingHand('Opening Hand:', 7)
mulligan()
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





'''
mulligan = str(raw_input('Keep or Mulligan? (k/m) '))
if (mulligan == 'k'):
    print 1

elif (mulligan == 'm'):
    print 2

else:
    print 'k/m only'

'''
