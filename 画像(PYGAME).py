import pygame
import sys 

def main():
    pygame.init()
    pygame.display.set_caption("pygameで画像")
    screen = pygame.display.set_mode((640, 360))

    clock = pygame.time.Clock()
    img_bg = pygame.image.load("image/pg_bg.png")
    img_choice = [
        pygame.image.load("image/pg_chara0.png"),
        pygame.image.load("image/pg_chara1.png")
    ]

    tmr = 0

    while True:
        tmr += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    screen = pygame.display.set_mode((640, 360), pygame.FULLSCREEN)

                if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                    screen = pygame.display.set_mode((640, 360))

        x = tmr & 160
        for I in range(5):
            screen.blit(img_bg, [I * 160 - x, 0])
        screen.blit(img_choice[tmr % 2], [224, 160])
        pygame.display.update()
        clock.tick(5)

if __name__ == '__main__':
    main()
