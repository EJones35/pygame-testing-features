import os
import sys
import random
import pygame
import datetime
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
pygame.mixer.init()
screen = pygame.display.set_mode((screen_width,screen_height),pygame.RESIZABLE)
clock = pygame.time.Clock()
print(__file__)
image_path = os.path.abspath(__file__)
file_dir = os.path.dirname(image_path)
image_path = os.path.join(file_dir, "window_icon.png")
window_icon = pygame.image.load(image_path)
pygame.display.set_icon(window_icon)

colour_mode = darkdetect.theme().lower()
colour_mode_button = None
quit_button	= None
wim_button = None
cb1_button = None
tab_button = None
sntt_button = None
trwih_button = None
sd_button = None
cb2_button = None
woys_button = None
olt_button = None
ikh_button = None
taa_button = None
wk_button = None
hu_button = None
trp_button = None
b_button = None
buaa_button = None
sar_button = None
iqu_button = None
teo1800_button = None
yos_button = None
bowabow_button = None
twwwe_button = None
wlwdwtys_button = None
playing_song = None
last_playing_song = None
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

def load_and_play_song(song,file_ending,forever=False):
	song_dir_path = os.path.join(file_dir,"Songs")
	loading_song = os.path.join(song_dir_path,song)
	song_to_play = loading_song + file_ending
	pygame.mixer.music.load(song_to_play)
	if forever == True:
		pygame.mixer.music.play(-1)
	else:
		pygame.mixer.music.play()

def check_touching_song_button(button_name,song,file_ending=".flac"):
	global playing_song
	if button_name is not None:
		touching_button = button_name.collidepoint(event.pos)
		if touching_button:
			load_and_play_song(song,file_ending)
			playing_song = song

while running:
	if last_playing_song != playing_song and playing_song != None:
		print(playing_song)
		last_playing_song = playing_song
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
			if event.key == pygame.K_2:
				screen_title = "Songs - Page 1"
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
					touching_quit_button = quit_button.collidepoint(event.pos)
					if touching_quit_button:
						sys.exit()
				if next_page_button is not None:
					touching_next_page_button = next_page_button.collidepoint(event.pos)
					if touching_next_page_button:
						screen_title = "Songs - Page 2"
				if previous_page_button is not None:
					touching_previous_page_button = previous_page_button.collidepoint(event.pos)
					if touching_previous_page_button:
						screen_title = "Songs - Page 1"

				if screen_title == "Songs - Page 1":
					check_touching_song_button(ah_button,"Alexander Hamilton")
					check_touching_song_button(abs_button,"Aaron Burr, Sir")
					check_touching_song_button(ms_button,"My Shot")
					check_touching_song_button(tsot_button,"The Story of Tonight")
					check_touching_song_button(tss_button,"The Schuyler Sisters")
					check_touching_song_button(fr_button,"Farmer Refuted")
					check_touching_song_button(ybb_button,"You'll Be Back")
					check_touching_song_button(rhm_button,"Right Hand Man")
					check_touching_song_button(awb_button,"A Winter's Ball")
					check_touching_song_button(h_button,"Helpless")
					check_touching_song_button(s_button,"Satisfied")
					check_touching_song_button(tsotr_button,"The Story of Tonight (Reprise)")
					check_touching_song_button(wfi_button,"Wait for It")
					check_touching_song_button(sa_button,"Stay Alive")
					check_touching_song_button(tdc_button,"Ten Duel Commandments")
					check_touching_song_button(mmi_button,"Meet Me Inside")
					check_touching_song_button(twbe_button,"That Would Be Enough")
					check_touching_song_button(gas_button,"Guns and Ships")
					check_touching_song_button(hhieon_button,"History Has Its Eyes On You")
					check_touching_song_button(y_button,"Yorktown (The World Turned Upside Down)")
					check_touching_song_button(wcn_button,"What Comes Next")
					check_touching_song_button(dt_button,"Dear Theodosia")
					check_touching_song_button(ns_button,"Non-Stop")

				if screen_title == "Songs - Page 2":
					check_touching_song_button(wim_button,"What'd I Miss")
					check_touching_song_button(cb1_button,"Cabinet Battle #1")
					check_touching_song_button(tab_button,"Take a Break")
					check_touching_song_button(sntt_button,"Say No To This")
					check_touching_song_button(trwih_button,"The Room Where It Happens")
					check_touching_song_button(sd_button,"Schuyler Defeated")
					check_touching_song_button(cb2_button,"Cabinet Battle #2")
					check_touching_song_button(woys_button,"Washington On Your Side")
					check_touching_song_button(olt_button,"One Last Time")
					check_touching_song_button(ikh_button,"I Know Him")
					check_touching_song_button(taa_button,"The Adams Administration")
					check_touching_song_button(wk_button,"We Know")
					check_touching_song_button(hu_button,"Hurricane")
					check_touching_song_button(trp_button,"The Reynolds Pamphlet")
					check_touching_song_button(b_button,"Burn")
					check_touching_song_button(buaa_button,"Blow Us All Away")
					check_touching_song_button(sar_button,"Stay Alive (Reprise)")
					check_touching_song_button(iqu_button,"It's Quiet Uptown")
					check_touching_song_button(teo1800_button,"The Election of 1800")
					check_touching_song_button(yos_button,"Your Obedient Servant")
					check_touching_song_button(bowabow_button,"Best of Wives and Best of Women")
					check_touching_song_button(twwwe_button,"The World Was Wide Enough")
					check_touching_song_button(wlwdwtys_button,"Who Lives, Who Dies, Who Tells Your Story")

	screen.fill(colours["background"])
	next_page_button = None
	previous_page_button = None
	colour_mode_button = None
	quit_button = draw_button_with_offset_from_corner("gray",screen_width-120,screen_height-75,100,50,"Quit","black",35)
	if screen_title == "Example Title":
		surface = draw_text_with_offset_from_centre(0,-50,greeting_message,True,colours["general"],100)
		surface = draw_text_with_offset_from_centre(0,0,f"Current Song: {playing_song}",True,colours["general"],50)
		surface = draw_text_with_offset_from_centre(0,25,"Subtitle 2",True,colours["general"],25)
		colour_mode_button = draw_button_with_offset_from_centre("gray",0,200,200,50,f"{other_colour_mode.capitalize()} Mode","black",35)
		date = draw_text_with_offset_from_corner(0,10,f"Date: {year}-{month}-{date}",35,colours["general"])
		time = draw_text_with_offset_from_corner(0,35,f"Time: {hour}:{minute}:{second}",35,colours["general"])
		help_menu = draw_text_with_offset_from_centre(screen_centre_width-150,0-screen_centre_height+100,"Space - Light/dark mode\nEscape - Quit\n0-3 - Change menu",True,colours["general"],35)
	if screen_title == "Main Menu":
		surface = draw_text_with_offset_from_centre(0,-50,greeting_message,True,colours["general"],100)
		surface = draw_text_with_offset_from_centre(0,0,f"Current Song: {playing_song}",True,colours["general"],50)
	if screen_title == "Songs - Page 1":
		# Column 1 (songs 1-12)
		ah_button = draw_button_with_offset_from_corner("gray",10,30,600,50,"Alexander Hamilton","black",35)
		abs_button = draw_button_with_offset_from_corner("gray",10,90,600,50,"Aaron Burr, Sir","black",35)
		ms_button = draw_button_with_offset_from_corner("gray",10,150,600,50,"My Shot","black",35)
		tsot_button = draw_button_with_offset_from_corner("gray",10,210,600,50,"The Story of Tonight","black",35)
		tss_button = draw_button_with_offset_from_corner("gray",10,270,600,50,"The Schuyler Sisters","black",35)
		fr_button = draw_button_with_offset_from_corner("gray",10,330,600,50,"Farmer Refuted","black",35)
		ybb_button = draw_button_with_offset_from_corner("gray",10,390,600,50,"You'll Be Back","black",35)
		rhm_button = draw_button_with_offset_from_corner("gray",10,450,600,50,"Right Hand Man","black",35)
		awb_button = draw_button_with_offset_from_corner("gray",10,510,600,50,"A Winter's Ball","black",35)
		h_button = draw_button_with_offset_from_corner("gray",10,570,600,50,"Helpless","black",35)
		s_button = draw_button_with_offset_from_corner("gray",10,630,600,50,"Satisfied","black",35)
		tsotr_button = draw_button_with_offset_from_corner("gray",10,690,600,50,"The Story of Tonight (Reprise)","black",35)
		# Column 2 (songs 13-23)
		wfi_button = draw_button_with_offset_from_corner("gray",650,30,600,50,"Wait For It","black",35)
		sa_button = draw_button_with_offset_from_corner("gray",650,90,600,50,"Stay Alive","black",35)
		tdc_button = draw_button_with_offset_from_corner("gray",650,150,600,50,"Ten Duel Commandments","black",35)
		mmi_button = draw_button_with_offset_from_corner("gray",650,210,600,50,"Meet Me Inside","black",35)
		twbe_button = draw_button_with_offset_from_corner("gray",650,270,600,50,"That Would Be Enough","black",35)
		gas_button = draw_button_with_offset_from_corner("gray",650,330,600,50,"Guns and Ships","black",35)
		hhieon_button = draw_button_with_offset_from_corner("gray",650,390,600,50,"History Has Its Eyes On You","black",35)
		y_button = draw_button_with_offset_from_corner("gray",650,450,600,50,"Yorktown (The World Turned Upside Down)","black",35)
		wcn_button = draw_button_with_offset_from_corner("gray",650,510,600,50,"What Comes Next?","black",35)
		dt_button = draw_button_with_offset_from_corner("gray",650,570,600,50,"Dear Theodisia","black",35)
		ns_button = draw_button_with_offset_from_corner("gray",650,630,600,50,"Non-Stop","black",35)

		next_page_button = draw_button_with_offset_from_corner("gray",650,750,600,50,"Next Page ->","black",35)

	if screen_title == "Songs - Page 2":
		# Column 1 (songs 24-35)
		wim_button = draw_button_with_offset_from_corner("gray",10,30,600,50,"What'd I Miss","black",35)
		cb1_button = draw_button_with_offset_from_corner("gray",10,90,600,50,"Cabinet Battle #1","black",35)
		tab_button = draw_button_with_offset_from_corner("gray",10,150,600,50,"Take A Break","black",35)
		sntt_button = draw_button_with_offset_from_corner("gray",10,210,600,50,"Say No To This","black",35)
		trwih_button = draw_button_with_offset_from_corner("gray",10,270,600,50,"The Room Where It Happens","black",35)
		sd_button = draw_button_with_offset_from_corner("gray",10,330,600,50,"Schuyler Defeated","black",35)
		cb2_button = draw_button_with_offset_from_corner("gray",10,390,600,50,"Cabinet Battle #2","black",35)
		woys_button = draw_button_with_offset_from_corner("gray",10,450,600,50,"Washington On Your Side","black",35)
		olt_button = draw_button_with_offset_from_corner("gray",10,510,600,50,"One Last Time","black",35)
		ikh_button = draw_button_with_offset_from_corner("gray",10,570,600,50,"I Know Him","black",35)
		taa_button = draw_button_with_offset_from_corner("gray",10,630,600,50,"The Adams Administration","black",35)
		wk_button = draw_button_with_offset_from_corner("gray",10,690,600,50,"We Know","black",35)
		# Column 2 (songs 36-46)
		hu_button = draw_button_with_offset_from_corner("gray",650,30,600,50,"Hurricane","black",35)
		trp_button = draw_button_with_offset_from_corner("gray",650,90,600,50,"The Reynolds Pamphlet","black",35)
		b_button = draw_button_with_offset_from_corner("gray",650,150,600,50,"Burn","black",35)
		buaa_button = draw_button_with_offset_from_corner("gray",650,210,600,50,"Blow Us All Away","black",35)
		sar_button = draw_button_with_offset_from_corner("gray",650,270,600,50,"Stay Alive (Reprise)","black",35)
		iqu_button = draw_button_with_offset_from_corner("gray",650,330,600,50,"It's Quiet Uptown","black",35)
		teo1800_button = draw_button_with_offset_from_corner("gray",650,390,600,50,"The Election of 1800","black",35)
		yos_button = draw_button_with_offset_from_corner("gray",650,450,600,50,"Your Obedient Servant","black",35)
		bowabow_button = draw_button_with_offset_from_corner("gray",650,510,600,50,"Best of Wives and Best of Women","black",35)
		twwwe_button = draw_button_with_offset_from_corner("gray",650,570,600,50,"The World Was Wide Enough","black",35)
		wlwdwtys_button = draw_button_with_offset_from_corner("gray",650,630,600,50,"Who Lives, Who Dies, Who Tells Your Story","black",35)

		previous_page_button = draw_button_with_offset_from_corner("gray",650,750,600,50,"<- Previous Page","black",35)
	
	title = pygame.display.set_caption(f"{window_title} - {colour_mode.capitalize()} Mode")

	pygame.display.flip()
