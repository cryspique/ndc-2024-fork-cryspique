import pyxel

# ======================================
# SCREEN RESOLUTION
# ======================================
WIDTH = 128
HEIGHT = 128

# ======================================
# STATE
# ======================================
STATE_FIRST_LAUNCH = 0
STATE_PAUSE = 1
STATE_PLAY = 2
STATE_GAMEOVER = 3

# ======================================
# DIR_PLAYER
# ======================================
DIR_PLAYER_EAST = 0
DIR_PLAYER_WEST = 1
PLAYER_JUMP_LIST = [0,-1,-5,-3,-1,2,3]

# ======================================
# TITLE
# ======================================
TITLE = "Pinguin-Run"

# ======================================
# FPS
# ======================================
FPS = 30

# ======================================
# COLISION LIST
# ======================================
COLISION_LIST = [
    (0, 26), (1, 26), (2, 26), (3, 26), (7, 26),
    (8, 26), (9, 26), (10, 26), (11, 26), (12, 26),
    (0, 27), (1, 27), (2, 27), (3, 27), (4, 27),
    (5, 27), (6, 27), (7, 27), (8, 27), (9, 27),
    (10, 27), (11, 27), (12, 27), (13, 27), (14, 27),
    (15, 27), (16, 27), (17, 27), (0, 28), (1, 28),
    (2, 28), (3, 28), (4, 28), (5, 28), (6, 28),
    (7, 28), (8, 28), (9, 28), (10, 28), (11, 28),
    (12, 28), (13, 28), (14, 28), (15, 28), (16, 28),
    (17, 28), (0, 29), (1, 29), (2, 29), (3, 29),
    (4, 29), (5, 29), (6, 29), (7, 29), (8, 29),
    (9, 29), (10, 29), (11, 29), (12, 29),
    (13, 29), (14, 29), (15, 29), (16, 29), (17, 29),
    (0, 30), (1, 30), (2, 30), (3, 30), (4, 30),
    (5, 30), (6, 30), (9, 30), (10, 30), (11, 30),
    (12, 30), (13, 30), (14, 30), (15, 30), (0, 31),
    (1, 31), (2, 31), (3, 31), (4, 31), (5, 31),
    (6, 31), (9, 31), (10, 31), (11, 31), (12, 31),
    (13, 31), (14, 31), (15, 31),
]
COLISION_LIST_ONLY_DOWN = [(0, 25), (1, 25), (2, 25),
                           (3, 25), (4, 25), (5, 25),]
COLISION_LIST_SPE = [(4, 23), (5, 23), (6, 23)]
# ======================================
# PAUSE
# ======================================
BUTTON_PLAY = 32, 48, 64, 32
BUTTON_RESET = 32, 80, 64, 32
BUTTON_SOUND = 112, 8, 8, 8

TEXT_PAUSE_PLAY_X_OFF = BUTTON_PLAY[0]+BUTTON_PLAY[2]/2 - 16/2
TEXT_PAUSE_PLAY_Y_OFF = BUTTON_PLAY[1]+BUTTON_PLAY[3]/2 - 4/2

TEXT_PAUSE_RESET_X_OFF = BUTTON_RESET[0]+BUTTON_RESET[2]/2 - 20/2
TEXT_PAUSE_RESET_Y_OFF = BUTTON_RESET[1]+BUTTON_RESET[3]/2 - 4/2

IMG_PAUSE_SOUND_OFFSET_X_IMG = 136

COLOR_PLAY = pyxel.COLOR_RED
COLOR_RESET = pyxel.COLOR_RED


# ======================================
# KEY
# ======================================

KEY_LEFT = pyxel.KEY_LEFT
KEY_RIGHT = pyxel.KEY_RIGHT
KEY_JUMP = pyxel.KEY_SPACE
KEY_PAUSE = pyxel.KEY_P

# ======================================
# COLKEY
# ======================================
COLKEY = pyxel.COLOR_DARK_BLUE

# ======================================
# COLOR
# ======================================
COLOR_BG_MENU = pyxel.COLOR_GRAY
COLOR_BG = pyxel.COLOR_DARK_BLUE

# ======================================
# PINGUIN
# ======================================
PINGUIN_SPEED = 1
PINGUIN_SPEED_DIV = 2
PINGUIN_IMG_OFFSET_X = 80
PINGUIN_IMG_OFFSET_Y = 56

PINGUINS = [(8, 32, 24),(51*8,10*8,57*8),(55*8,7*8,58*8)]

# ======================================
# MOUVIN PLATFORM
# ======================================
PLATFORM_SPEED = 3 # number of frames neede for the platform to move for 1 pixel
PLATFORM_IMG_COORD = ((80,208),(88,208),(96,208))
PLATFORM = [
    [0,# relative x (put it to 0 by default)
    32,# y
    32,# x1 (starting point of the platform on the left)
    40,# x2 (loopîng point of the platform on the right)
    3,# lenght (lenght of the platform by unit of 8 pixel)
    1 # direction (used for directionnal purposes)
     ]
]




