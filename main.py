import pyxel
import config
import pause
import sound

from sprites.MovingPlatform import *
from sprites.PinguinClass import Pinguin
from sprites.PlayerClass import Player


state = config.STATE_FIRST_LAUNCH
player = Player()
pinguins = []
sounds = sound.Sound("sounds.json")

def restart():
    global state
    state = config.STATE_PLAY
    player.__init__()

def draw():
    if state == config.STATE_PLAY:
        tm = pyxel.tilemaps[0]
        pyxel.cls(config.COLOR_BG)
        pyxel.bltm(0, 0, tm, 0, 0, 5000, config.HEIGHT, config.COLKEY)
        player.drawSprite()
        drawPlatform()
    
        for pinguin in pinguins:
            pinguin.draw()

    elif state == config.STATE_GAMEOVER:
        tm = pyxel.tilemaps[1]
        pyxel.bltm(player.real_x2camera_x(0), 0, tm,
                   config.WIDTH, 0, config.WIDTH, config.HEIGHT)
        pyxel.text(player.real_x2camera_x(config.WIDTH/2-18),
                   config.HEIGHT/2-2, "GAME OVER", pyxel.COLOR_RED)
        pyxel.text(player.real_x2camera_x(config.WIDTH/2-13),
                   config.HEIGHT/2+30, "RESTART", pyxel.COLOR_RED)
        if pause.button_colide_with_mouse((48,88,32,16)) and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            restart()
    else:
        if state == config.STATE_FIRST_LAUNCH:
            pyxel.cls(config.COLOR_BG_MENU)
        else:
            tm = pyxel.tilemaps[0]
            pyxel.cls(config.COLOR_BG)
            pyxel.bltm(0, 0, tm, 0, 0, config.WIDTH,
                       config.HEIGHT, config.COLKEY)
            player.drawSprite()
            for pinguin in pinguins:
                pinguin.draw()
        pause.draw_pause(player)


def update():
    global state

    if player.coords[1] > 128: # if the player fall under y == 128 he dies
        state = config.STATE_GAMEOVER

    if pyxel.btn(config.KEY_PAUSE): # if the pause key is pressed, pause menu comes up
        state = config.STATE_PAUSE

    if state == config.STATE_PLAY: # default state, everything is normal in this state
        updatePlatform()
        player.move()
        player.focus()
        player.animation()
        for pinguin in pinguins:
            pinguin.update()
            if pinguin.colide_with_player(player): # death by collision with a pinguin
                state = config.STATE_GAMEOVER
    elif state == config.STATE_GAMEOVER:
        pass
    else:
        state = pause.update_pause(state)


def main():
    pyxel.init(config.WIDTH, config.HEIGHT, config.TITLE, config.FPS)

    pyxel.load("res.pyxres")

    player.focus()

    sounds.play_sound()

    for pinguin in config.PINGUINS: # pinguin initialisation
        pinguins.append(Pinguin(*pinguin))

    pyxel.run(update, draw)


if __name__ == "__main__":
    main()
