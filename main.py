import pygame

pygame.init()

# Display varibles
display_width = 800
display_height = 600

#Set window size and name
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('My Game')


#Set color
black=(0,0,0)
white=(255,255,255)


#Init time
clock = pygame.time.Clock()
crashed = False

#Images
playerImg = pygame.image.load('rsz_player.png')

def gamer(x,y):
    gameDisplay.blit(playerImg,(x,y))

x = (display_width/2-64)
y = (display_height*0.5)


while not crashed:

    #Events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            crashed = True

        print(event)
    #Checking inputs
    if pygame.key.get_pressed()[pygame.K_d]:
        x+=3
    if pygame.key.get_pressed()[pygame.K_a]:
        x-=3
        
    gameDisplay.fill(black)
    gamer(x,y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
