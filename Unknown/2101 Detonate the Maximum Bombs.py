def maximumDetonation(bombs):
    maximumDetonationAux(bombs, bombs[0], {})
    
def maximumDetonationAux(bombs, bomb, prevDetonations):
    for i in range(len(bombs)):
        if bombs[i] != bomb:
            x1 = bombs[i][0]
            y1 = bombs[i][1]
            x2 = bomb[0]        
            y2 = bomb[1]
            if (diffTwoPoints(x1, x2, y1, y2) <= bomb[2]):
                maximumDetonationAux(bombs, )
                
def diffTwoPoints(x1, x2, y1, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**(1/2)