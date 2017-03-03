import pygame
import time
import random

pygame.init()

display_width=800
display_height=600

black=(0,0,0)
white=(255,255,255)

red=(150,0,0)
green=(0,150,0)
blue=(0,0,255)
light_red=(255,0,0)
light_green=(0,255,0)

pause=False

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("My First Game")
clock=pygame.time.Clock()

car_image=pygame.image.load("Untitled.png")
icon_image=pygame.image.load("Untitled2.png")
pygame.display.set_icon(icon_image)

def things_dodged(count):
	font=pygame.font.SysFont(None,30)
	text=font.render("Dodged: "+str(count), True, green)
	gameDisplay.blit(text,(0,0))

def things(thingx,thingy,thingw,thingh,color):
	pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def car(x,y):
	gameDisplay.blit(car_image,(x,y))

def text_objects(text,font,color):
	textSurface=font.render(text, True, color)
	return textSurface,textSurface.get_rect()

def message_display(text):
	largeText=pygame.font.Font(None,120)
	TextSurf,TextRect =text_objects(text,largeText,red)
	TextRect.center=((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf,TextRect)
	pygame.display.update();
	time.sleep(1)
	game_loop()

def button(text,color,acolor,x,y,w,h,action=None):
	mouse=pygame.mouse.get_pos()
	click=pygame.mouse.get_pressed()
	#print(click)
	if mouse[0]<x+w and mouse[0]>x and mouse[1]<y+h and mouse[1]>y:
		pygame.draw.rect(gameDisplay,acolor,(x,y,w,h))
		if click[0]==1 and action != None:
			action()
	else:
		pygame.draw.rect(gameDisplay,color,(x,y,w,h))
	smallText=pygame.font.Font("freesansbold.ttf",25)
	TextSurf,TextRect=text_objects(text,smallText,black)
	TextRect.center=((x+w/2),(y+h/2))
	gameDisplay.blit(TextSurf,TextRect)
        
def crash():
	largeText=pygame.font.Font("freesansbold.ttf",70)
	TextSurf,TextRect =text_objects("YOU CRASHED",largeText,blue)
	TextRect.center=((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf,TextRect)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		button("PLAY AGAIN!",red,light_red,200,450,160,50,game_loop)
		button("Quit",green,light_green,500,450,100,50,quit)

		pygame.display.update()
		clock.tick(70)

def game_intro():
	intro=True
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			gameDisplay.fill(white)
			largeText=pygame.font.Font("freesansbold.ttf",100)
			TextSurf,TextRect =text_objects("CAR RASH",largeText,black)
			TextRect.center=((display_width/2),(display_height/2))
			gameDisplay.blit(TextSurf,TextRect)
			button("Play",red,light_red,200,450,100,50,game_loop)
			button("Quit",green,light_green,500,450,100,50,quit)

			pygame.display.update()
			clock.tick(70)

def unpause():
	global pause
	pause=False

def paused():
	global pause
	pause=True
	largeText=pygame.font.Font("freesansbold.ttf",70)
	TextSurf,TextRect =text_objects("PAUSED",largeText,black)
	TextRect.center=((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf,TextRect)
	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		button("CONTINUE",red,light_red,200,450,160,50,unpause)
		button("Quit",green,light_green,500,450,100,50,quit)

		pygame.display.update()
		clock.tick(70)


def game_loop():
		x=(display_width * 0.40)
		y=(display_height * 0.767)
		i=0
		car_width=120
		x_change=0
		dodged=0

		thing_width=100
		thing_startx=random.randrange(0,display_width-thing_width)
		thing_starty=-600
		thing_speed=4
		thing_height=100

		crashed=False

		while not crashed:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				i+=0.02
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						x_change=-(8+i)
					if event.key == pygame.K_RIGHT:
						x_change=8+i
					if event.key == pygame.K_p:
						paused()
				if event.type ==pygame.KEYUP:
					if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
						x_change=0

			x+=x_change
			gameDisplay.fill(white)
			things(thing_startx,thing_starty,thing_width,thing_height,black)
			thing_starty+=thing_speed
			car(x,y)
			things_dodged(dodged)

			if x > display_width-car_width or x<0:
				crash()
			
			if thing_starty > display_height:
				thing_starty=0-thing_height
				thing_startx=random.randrange(0,display_width-thing_width)
				dodged+=1
				thing_speed+=0.33

			if y<thing_starty+thing_height:
				print("y crossover")
				if x>thing_startx and x<thing_startx+thing_width or x+car_width>thing_startx and x+car_width<thing_startx+thing_width or x<thing_startx and x+car_width>thing_startx+thing_width: 
					print("x crossover")
					crash()

			pygame.display.update()
			clock.tick(70)

game_intro()
game_loop()
pygame.quit()

