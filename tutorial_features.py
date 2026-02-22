import os
import random
import pygame
import darkdetect
import datetime

os.system("cls")

screen_width = 1280
screen_height = 700
screen_centre_width = screen_width/2
screen_centre_height = screen_height/2

window_title = "Example Title"

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height),pygame.RESIZABLE)
clock = pygame.time.Clock()
window_icon = pygame.image.load("C:/Users/ethan/Python/Pygame/window_icon.png")
pygame.display.set_icon(window_icon)

colour_mode = darkdetect.theme().lower()
button = None
running = True

def draw_rectangle_with_offset_from_centre(colour,offset_x,offset_y,width,height):
	x = screen_centre_width + offset_x - (width / 2)
	y = screen_centre_height + offset_y - (height / 2)
	return pygame.draw.rect(screen,colour,(x,y,width,height))

def draw_circle_with_offset_from_centre(colour,offset_x,offset_y,radius):
	x = screen_centre_width + offset_x
	y = screen_centre_height + offset_y
	pygame.draw.circle(screen,colour,(x,y),radius)

def draw_line_with_offset_from_centre(colour,start_offset_x,start_offset_y,end_offset_x,end_offset_y,line_width):
	start_x = screen_centre_width + start_offset_x
	start_y = screen_centre_height + start_offset_y
	end_x = screen_centre_width + end_offset_x
	end_y = screen_centre_height + end_offset_y

	pygame.draw.line(screen,colour,(start_x,start_y),(end_x,end_y),line_width)

def draw_text_with_offset_from_centre(x_offset,y_offset,text,anti_ailising,colour,size):
	font = pygame.font.Font(None,size)
	surface = font.render(text,anti_ailising,colour)
	x = screen_centre_width - (surface.get_width() / 2) + x_offset
	y = screen_centre_height - (surface.get_height() / 2) + y_offset
	return screen.blit(surface,(x,y))

def draw_button_with_offset_from_centre(colour,x_offset,y_offset,width,height,label,text_colour,text_size):
	button = draw_rectangle_with_offset_from_centre(colour,x_offset,y_offset,width,height)
	draw_text_with_offset_from_centre(x_offset,y_offset,label,True,text_colour,text_size)
	return button

def draw_time_with_offset_from_corner(x_offset,y_offset,text_size,text_colour):
	font = pygame.font.Font(None,text_size)
	surface = font.render(f"Time: {hour}:{minute}:{second}",True,text_colour)
	screen.blit(surface,(x_offset,y_offset))

def draw_date_with_offset_from_corner(x_offset,y_offset,text_size,text_colour):
	font = pygame.font.Font(None,text_size)
	surface = font.render(f"Date: {year}-{month}-{date}",True,text_colour)
	screen.blit(surface,(x_offset,y_offset))

while running:
	now = datetime.datetime.now()
	hour = now.hour
	minute = now.minute
	second = now.second
	date = now.day
	month = now.month
	year = now.year
	if hour < 10:
		hour = "0"+str(hour)
	if minute < 10:
		minute = "0"+str(minute)
	if second < 10:
		second = "0"+str(second)
	if date < 10:
		date = "0"+str(date)
	if month < 10:
		month = "0"+str(month)
	screen_centre_width = screen.get_width() / 2
	screen_centre_height = screen.get_height() / 2
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				if colour_mode == "dark":
					colour_mode = "light"
				else:
					colour_mode = "dark"
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1: # Left click
				if button is not None:
					touching_button = button.collidepoint(event.pos)
					if touching_button:
						if colour_mode == "dark":
							colour_mode = "light"
						else:
							colour_mode = "dark"

	if colour_mode == "dark":
		screen.fill((30,30,30))
		surface = draw_text_with_offset_from_centre(0,-50,"Title",True,(220,220,220),100)
		surface = draw_text_with_offset_from_centre(0,0,"Subtitle",True,(220,220,220),50)
		surface = draw_text_with_offset_from_centre(0,25,"Subtitle 2",True,(220,220,220),25)
		button = draw_button_with_offset_from_centre("gray",0,200,200,50,"Light Mode","black",35)
		date = draw_date_with_offset_from_corner(0,0,35,(220,220,220))
		time = draw_time_with_offset_from_corner(0,25,35,(220,220,220))
	else:
		screen.fill((245,245,240))
		surface = draw_text_with_offset_from_centre(0,-50,"Title",True,(30,30,30),100)
		surface = draw_text_with_offset_from_centre(0,0,"Subtitle",True,(30,30,30),50)
		surface = draw_text_with_offset_from_centre(0,25,"Subtitle 2",True,(30,30,30),25)
		button = draw_button_with_offset_from_centre("dimgray",0,200,200,50,"Dark Mode","white",35)
		date = draw_date_with_offset_from_corner(0,0,35,(30,30,30))
		time = draw_time_with_offset_from_corner(0,25,35,(30,30,30))
	
	title = pygame.display.set_caption(f"{window_title} - {colour_mode.capitalize()} Mode")

	pygame.display.flip()