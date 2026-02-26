import os
import sys
import random
import pygame
import datetime
os.system("pip install darkdetect")
import darkdetect

os.system("cls")

screen_width = 1280
screen_height = 700
screen_centre_width = screen_width/2
screen_centre_height = screen_height/2

colours = {}

light_mode_colours = {
	"general":(30,30,30),
	"background":(245,245,240)
}

dark_mode_colours = {
	"general":(220,220,220),
	"background":(20,20,20)
}

window_title = "Example Title"
screen_title = "Example Title"
greeting_message = ""

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height),pygame.RESIZABLE)
clock = pygame.time.Clock()
window_icon = pygame.image.load("C:/Users/ethan/Python/Pygame/window_icon.png")
pygame.display.set_icon(window_icon)

colour_mode = darkdetect.theme().lower()
colour_mode_button = None
quit_button	= None
running = True

def draw_rectangle_with_offset_from_centre(colour,offset_x,offset_y,width,height):
	x = screen_centre_width + (offset_x) - (width / 2)
	y = screen_centre_height + (offset_y) - (height / 2)
	return pygame.draw.rect(screen,colour,(x,y,width,height))

def draw_rectangle_with_offset_from_corner(colour,offset_x,offset_y,width,height):
	return pygame.draw.rect(screen,colour,(offset_x,offset_y-10,width,height))

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

def draw_text_with_offset_from_corner(x_offset,y_offset,text,size,colour):
	font = pygame.font.Font(None,size)
	surface = font.render(text,True,colour)
	screen.blit(surface,(x_offset+20,y_offset))

def draw_button_with_offset_from_centre(colour,x_offset,y_offset,width,height,label,text_colour,text_size):
	button = draw_rectangle_with_offset_from_centre(colour,x_offset,y_offset,width,height)
	draw_text_with_offset_from_centre(x_offset,y_offset,label,True,text_colour,text_size)
	return button

def draw_button_with_offset_from_corner(colour,x_offset,y_offset,width,height,label,text_colour,text_size):
	button = draw_rectangle_with_offset_from_corner(colour,x_offset,y_offset,width,height)
	draw_text_with_offset_from_corner(x_offset,y_offset,label,text_size,text_colour)
	return button

while running:
	now = datetime.datetime.now()
	hour = now.hour
	minute = now.minute
	second = now.second
	date = now.day
	month = now.month
	year = now.year
	
	if 0 <= hour < 6:
		greeting_message = "It's very early..."
	elif 6 <= hour < 12:
		greeting_message = "Good morning!"
	elif 12 <= hour < 13:
		greeting_message = "Lunchtime!"
	elif 13 <= hour < 17:
		greeting_message = "Good afternoon!"
	elif 17 <= hour < 20:
		greeting_message = "Good evening!"
	elif 20 <= hour:
		greeting_message = "Good night!"

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

	if colour_mode == "light":
		colours = light_mode_colours
		other_colour_mode = "dark"
	else:
		colours = dark_mode_colours
		other_colour_mode = "light"

	screen_width = screen.get_width()
	screen_height = screen.get_height()
	screen_centre_width = screen_width / 2
	screen_centre_height = screen_height / 2
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				if colour_mode == "dark":
					colour_mode = "light"
				else:
					colour_mode = "dark"
			if event.key == pygame.K_ESCAPE:
				sys.exit()
			if event.key == pygame.K_0:
				screen_title = "Example Title"
			if event.key == pygame.K_1:
				screen_title = "Main Menu"
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1: # Left click
				if colour_mode_button is not None:
					touching_button = colour_mode_button.collidepoint(event.pos)
					if touching_button:
						if colour_mode == "dark":
							colour_mode = "light"
						else:
							colour_mode = "dark"
				if quit_button is not None:
					touching_button = quit_button.collidepoint(event.pos)
					if touching_button:
						sys.exit()

	screen.fill(colours["background"])
	if screen_title == "Example Title":
		surface = draw_text_with_offset_from_centre(0,-50,greeting_message,True,colours["general"],100)
		surface = draw_text_with_offset_from_centre(0,0,"Subtitle",True,colours["general"],50)
		surface = draw_text_with_offset_from_centre(0,25,"Subtitle 2",True,colours["general"],25)
		colour_mode_button = draw_button_with_offset_from_centre("gray",0,200,200,50,f"{other_colour_mode.capitalize()} Mode","black",35)
		date = draw_text_with_offset_from_corner(0,10,f"Date: {year}-{month}-{date}",35,colours["general"])
		time = draw_text_with_offset_from_corner(0,35,f"Time: {hour}:{minute}:{second}",35,colours["general"])
		help_menu = draw_text_with_offset_from_centre(screen_centre_width-150,0-screen_centre_height+100,"Space - Light/dark mode\nEscape - Quit\n0-1 - Change menu",True,colours["general"],35)
		quit_button = draw_button_with_offset_from_corner("gray",screen_width-120,screen_height-75,100,50,"Quit","black",35)
	if screen_title == "Main Menu":
		surface = draw_text_with_offset_from_centre(0,-50,greeting_message,True,colours["general"],100)
		surface = draw_text_with_offset_from_centre(0,0,"Subtitle :)",True,colours["general"],50)
		quit_button = draw_button_with_offset_from_corner("gray",screen_width-120,screen_height-75,100,50,"Quit","black",35)
	
	title = pygame.display.set_caption(f"{window_title} - {colour_mode.capitalize()} Mode")

	pygame.display.flip()
