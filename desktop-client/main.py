import pygame

display_width = 100
display_height = 100
pygame.init()
black=(0,0,0)
screen = pygame.display.set_mode((800,600))
screen.fill((60,100,100))

#Text through GUI
myFont = pygame.font.SysFont("Times New Roman", 30)

val = "100"
a = myFont.render("THOR: Your Score is:", 1, black)
b = myFont.render(val, 1, black)
screen.blit(a, (300, 30))
screen.blit(b, (520, 30))

thorImg = pygame.image.load('thor.png')

def thor(x,y):
    screen.blit(thorImg, (x,y))

x =  (display_width * 0.45)
y = (display_height * 0.8)

### main loop
run = True
while run:
    thor(x,y)	
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    pygame.display.flip()
