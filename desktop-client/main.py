import serial
import pygame
from playsound import playsound
from time import sleep

ser = serial.Serial("/dev/tty.SLAB_USBtoUART", 9600);
ser.close()

display_width = 100
display_height = 100
pygame.init()
black=(0,0,0)
screen = pygame.display.set_mode((800,600))
screen.fill((60,100,100))

#Text through GUI
myFont = pygame.font.SysFont("Times New Roman", 30)

a = myFont.render("THOR: Your Score is:", 1, black)
screen.blit(a, (300, 30))

thorImg = pygame.image.load('thor.png')

x =  (display_width * 0.45)
y = (display_height * 0.8)
def thor(x,y):
	screen.blit(thorImg, (x,y))

def render():
	ser.open()
	val = ser.readline()
	sleep(1)
	b = myFont.render(val, 1, black)
	screen.blit(b, (620, 30))
	ser.close()
	playsound('thor.wav')

thor(x,y)
render()
### main loop
while True:
	#thor(x,y)
	#render()
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			run = False
	pygame.display.flip()