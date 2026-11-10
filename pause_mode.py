import game_framework
import game_world
from pico2d import *

pause_font = None


def init():
    global pause_font
    pause_font = load_font('../DRILL13/ENCR10B.TTF', 36)


def finish():
    global pause_font
    pause_font = None


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_mode()


def update():
    pass


def render():
    clear_canvas()
    game_world.render()
    pause_font.draw(310, 320, 'PAUSE', (255, 255, 255))
    pause_font.draw(230, 270, 'Press P to resume', (255, 255, 255))
    update_canvas()
