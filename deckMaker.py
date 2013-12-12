#
# DECK MAKER MAGIC THE GATHERING 1.5
# python (c) REL, 2013
#
#####




deck = []

def madeDeck():
    global deck
    cards = "abcdefghijklmno"
    card_list = list(cards)
    
    for i in range(15):
        for x in range(4):
            deck += card_list[i]
        


#madeDeck()











