import pygame
import random

color =(0,0,0)
def draw_grid(screen):
    #Draw vertical lines
    for i in range(1, 21):
        pygame.draw.line(screen, color, (i*32, 0),(i*32, 512))
    #Draw horizontal lines
    for i in range(1, 17):
        pygame.draw.line(screen, color, (0, i*32), (640,i*32))



def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        #commit test
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        x_pos = 0
        y_pos = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #coordinates of the click
                    x, y = event.pos
                    #assign random numbers to x and y position if click is within bounds
                    if x_pos <= x < x_pos+32 and y_pos <= y < y_pos+32:
                        x_pos = random.randrange(0, 19) * 32
                        y_pos = random.randrange(0, 15) * 32
            screen.fill("light green")
            draw_grid(screen)
            screen.blit(mole_image, mole_image.get_rect(topleft=(x_pos, y_pos)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
