import py_game
import sys

WHITE = (255, 255, 255)
BLACK = ( 0, 0, 0)

def main():
    py_game.init()
    py_game.display.set_caption("初めてのPY GAME")
    screen = py_game.display.set_mode((800,600))
    clock = py_game.time.Clock()
    font = py_game.font.Font(None,80)
    tmr = 0

    while True:
        tmr = tmr +1
        for event in py_game.event.get():
            if event.type == py_game.QUIT:
                py_game.quit()
                sys.exit()
        
        txt = font.render(str(tmr),True, WHITE)
        screen.fill(BLACK)
        screen.blit(txt,[300,200])

        py_game.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()