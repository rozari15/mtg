#
# MULLIGAN MAGIC THE GATHERING 1.0
# python (c) REL, 2013
#
#####




x = 7

def mulligan():
    global x
    mulligan = str(raw_input('Keep or Mulligan? (k/m) '))
    if (mulligan == 'k'):
        pass

    elif (mulligan == 'm'):
        openingHand('Redraw', x - 1)
        
    else:
        print 'k/m only'
        mulligan()

