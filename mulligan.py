#
# MULLIGAN MAGIC THE GATHERING 1.0
# python (c) REL, 2013
#
#####

import virtualMTG


def mulligan():
    mulligan = str(raw_input('Keep or Mulligan? (k/m) '))
    if (mulligan == 'k'):
        pass

    elif (mulligan == 'm'):
        virtualMTG.openingHand('Redraw', 6)
    
    else:
        print 'k/m only'

