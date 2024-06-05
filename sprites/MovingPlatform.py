import pyxel
import config

def drawPlatform():
    for el in config.PLATFORM:
        pyxel.blt(el[2]+el[0],el[1],0,config.PLATFORM_IMG_COORD[0][0],config.PLATFORM_IMG_COORD[0][1],8,8,config.COLKEY)
        for i in range(1,el[4]-1):
            pyxel.blt(el[2]+el[0]+8*i,el[1],0,config.PLATFORM_IMG_COORD[1][0],config.PLATFORM_IMG_COORD[1][1],8,8,config.COLKEY)
        pyxel.blt(el[2]+el[0]+(8*(el[4]-1)),el[1],0,config.PLATFORM_IMG_COORD[2][0],config.PLATFORM_IMG_COORD[2][1],8,8,config.COLKEY)


def updatePlatform():
    for i in range(len(config.PLATFORM)):
        if (pyxel.frame_count % config.PLATFORM_SPEED) == 0:
            config.PLATFORM[i][0] += config.PLATFORM[i][5]
        if config.PLATFORM[i][5] == -1:
            if (config.PLATFORM[i][0] + config.PLATFORM[i][2]) < config.PLATFORM[i][2]:
                config.PLATFORM[i][5] = 1
        else:
            if (config.PLATFORM[i][0] + config.PLATFORM[i][2]) > config.PLATFORM[i][3]:
                config.PLATFORM[i][5] = -1

def updatedPlatformCollisionList(playerWidth):
    """
    input the player width for mesurement
    output a tuple with the lists of the platform's pixel x coords
    """
    listOfXCoords: list = [] # list of x coords where collision with a platform is possible
    listOfYCoords: list = [] # list of y coords where collision with a platform is possible
    for i in range(len(config.PLATFORM)):
        x = config.PLATFORM[i][0] + config.PLATFORM[i][2]
        listOfXCoords.append([x for x in range(x,x + playerWidth - 1 + (config.PLATFORM[i][4]*8))])
        listOfYCoords.append(config.PLATFORM[i][1])
    return (listOfXCoords,listOfYCoords)

def elementIsInList(x, list_):
    """
    input (x, list_)
    x is the element (here a x position)
    list_ is the list we check wether x is in, it must be a double list
    it return (True/False, [indices])
    the indices returned are in this case the ones of the sub lists x was found in
    """
    listeOfIndices = []
    for i in range(len(list_)):
        if x in list_[i]:
            listeOfIndices.append(i)
    return (bool(len(listeOfIndices)),listeOfIndices)

