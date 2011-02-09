import pygame, random, math
        
## INIT -------------------------------------------------

pygame.init()
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("S-kuru")
running = True
FPSClock = pygame.time.Clock() # FPS Limiter

## FUNCTIONS --------------------------------------------

def playSound(filename):
    pygame.mixer.Sound(filename).play()

## MAIN -------------------------------------------------
    
while running == True:
    FPSClock.tick(60)
    screen.fill((33,33,33))    

    print "FPS:", FPSClock.get_fps()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if pygame.K_SPACE:
                playSound("Music1.wav")
            elif pygame.K_RETURN:
                playSound("Sound2.wav")
                
    pygame.display.flip() # Display from frame buffer
    
pygame.quit()
