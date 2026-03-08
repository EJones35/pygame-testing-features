import os
import sys
import json
import random
import pygame
import datetime
import darkdetect
from mutagen import File

os.system("cls")

screen_width = 1280
screen_height = 700
screen_centre_width = screen_width/2
screen_centre_height = screen_height/2

def load_default_save_values():
	global saved_values
	saved_values = {
		"Colour Mode": "dark",
		"Song Page Number": 1,
		"Current Song": None,
		"Pause State": "pause",
		"Current Page": "Main Menu",
		"Repeat": False
		}

load_default_save_values()

colours = {}

light_mode_colours = {
	"general":(30,30,30),
	"background":(245,245,240),
	"selected button": (99, 102, 241)
}

dark_mode_colours = {
	"general":(220,220,220),
	"background":(20,20,20),
	"selected button": (129, 140, 248)
}

window_title = "TESTING WINDOW"
screen_title = "Main Menu"
greeting_message = ""

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_endevent(pygame.USEREVENT)
screen = pygame.display.set_mode((screen_width,screen_height),pygame.RESIZABLE)
clock = pygame.time.Clock()
if hasattr(sys, "_MEIPASS"):
	file_dir = sys._MEIPASS
else:
	file_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(file_dir, "window_icon.ico")
window_icon = pygame.image.load(image_path)
pygame.display.set_icon(window_icon)

colour_mode = darkdetect.theme().lower()
colour_mode_button = None
quit_button	= None
ah_button = None
abs_button = None
ms_button = None
tsot_button = None
tss_button = None
fr_button = None
ybb_button = None
rhm_button = None
awb_button = None
h_button = None
s_button = None
tsotr_button = None
wfi_button = None
sa_button = None
tdc_button = None
mmi_button = None
twbe_button = None
gas_button = None
hhieon_button = None
y_button = None
wcn_button = None
dt_button = None
ns_button = None
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
play_pause_button = None
repeat_button = None
repeat = False
song_length = 0
song_track_pos = 0
song_page = 1
max_song_pages = 3

ppom_button = None
jo_button = None
mi_button = None
eot_button = None

pause_state = "pause"
text_pause_state = "No song playing"


if hasattr(sys, "_MEIPASS"):
	current_directory = os.path.dirname(sys.executable)
else:
	current_directory = os.path.dirname(os.path.abspath(__file__))

save_file_path = None
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

def draw_button_with_offset_from_corner(colour,x_offset,y_offset,width,height,label,text_colour,text_size,song_name=None):
	global playing_song
	if song_name is not None and playing_song == song_name:
		colour = colours["selected button"]
	button = draw_rectangle_with_offset_from_corner(colour,x_offset,y_offset,width,height)
	draw_text_with_offset_from_corner(x_offset,y_offset,label,text_size,text_colour)
	return button

def load_and_play_song(song,file_ending,forever=False):
	global pause_state, song_length, song_file
	pause_state = "play"
	song_dir_path = os.path.join(file_dir,"Songs")
	loading_song = os.path.join(song_dir_path,song)
	song_to_play = loading_song + file_ending
	song_file = File(song_to_play)
	pygame.mixer.music.load(song_to_play)
	if forever == True:
		pygame.mixer.music.play(-1)
	else:
		pygame.mixer.music.play()
	song_length = song_file.info.length
	if song_length < 0:
		song_length = 0

def check_touching_song_button(button_name,song):
	global playing_song, pause_state, file_ending
	song_path = os.path.join(file_dir,"Songs")
	song_path = os.path.join(song_path,song)
	if os.path.exists(song_path + ".flac"):
		file_ending = ".flac"
	elif os.path.exists(song_path + ".mp3"):
		file_ending = ".mp3"
	elif os.path.exists(song_path + ".ogg"):
		file_ending = ".ogg"
	elif os.path.exists(song_path + ".wav"):
		file_ending = ".wav"

	if button_name is not None:
		touching_button = button_name.collidepoint(event.pos)
		if touching_button:
			load_and_play_song(song,file_ending)
			playing_song = song

def finish_song_action():
	global playing_song, file_ending
	if repeat == True:
		load_and_play_song(playing_song,file_ending)
	else:
		playing_song = None

def format_song_times():
	global song_track_pos, song_length
	if song_track_pos < 0:
		song_track_min = "00"
		song_track_secs = "00"
		song_length_min = "00"
		song_length_secs = "00"
	else:
		song_track_min = int(song_track_pos//60)
		song_track_secs = int(song_track_pos%60)
		if song_track_min < 0:
			song_track_min = 0
		if song_track_secs < 0:
			song_track_secs = 0
		if song_track_min < 10:
			song_track_min = "0" + str(song_track_min)
		if song_track_secs < 10:
			song_track_secs = "0" + str(song_track_secs)
		song_length_min = int(song_length//60)
		song_length_secs = int(song_length%60)
		if song_length_min < 0:
			song_length_min = 0
		if song_length_secs < 0:
			song_length_secs = 0
		if song_length_min < 10:
			song_length_min = "0" + str(song_length_min)
		if song_length_secs < 10:
			song_length_secs = "0" + str(song_length_secs)
	formatted_song_time = f"{song_track_min}:{song_track_secs}"
	formatted_song_length = f"{song_length_min}:{song_length_secs}"
	
	return formatted_song_time, formatted_song_length

def save_values_to_dictionary():
	global colour_mode, song_page, playing_song, pause_state, screen_title, repeat
	saved_values["Colour Mode"] = colour_mode
	saved_values["Song Page Number"] = song_page
	saved_values["Current Song"] = playing_song
	saved_values["Pause State"] = pause_state
	saved_values["Current Page"] = screen_title
	saved_values["Repeat"] = repeat

def save_to_file(file_path):
	with open(file_path,"w") as file:
		save_values_to_dictionary()
		json.dump(saved_values,file,indent=4)

def load_values_from_dictionary():
	global save_file_path, colour_mode, song_page, playing_song, pause_state, screen_title, repeat
	try:
		colour_mode = saved_values["Colour Mode"]
		song_page = saved_values["Song Page Number"]
		playing_song = saved_values["Current Song"]
		pause_state = saved_values["Pause State"]
		screen_title = saved_values["Current Page"]
		repeat = saved_values["Repeat"]
	except KeyError:
		os.remove(save_file_path)

def load_from_file(file_path):
	global saved_values
	if os.path.exists(file_path):
		with open(file_path,"r") as file:
			try:
				saved_values = json.load(file)
			except json.JSONDecodeError:
				print("JSON file was empty or corrupted.")
				print("Loading default values.")
				load_default_save_values()
		load_values_from_dictionary()

	else:
		print("File not found.")

def make_save_folder():
	global save_file_path
	save_file_path = os.path.join(current_directory,"Saves")
	os.makedirs(save_file_path,exist_ok=True)
	save_file_path = os.path.join(save_file_path,"saves.json")

make_save_folder()
load_from_file(save_file_path)

while running:
	if playing_song == None:
		text_pause_state = "No song playing"
	else:
		if pause_state == "play":
			text_pause_state = "pause"
		else:
			text_pause_state = "play"
	song_track_pos = pygame.mixer.music.get_pos()/1000

	formatted_song_time, formatted_song_length = format_song_times()

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
			save_to_file(save_file_path)
		if event.type == pygame.USEREVENT:
			finish_song_action()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				if colour_mode == "dark":
					colour_mode = "light"
				else:
					colour_mode = "dark"
			if event.key == pygame.K_ESCAPE:
				save_to_file(save_file_path)
				sys.exit()
			if event.key == pygame.K_0:
				screen_title = "Main Menu"
			if event.key == pygame.K_1:
				screen_title = "Example Title"
			if event.key == pygame.K_2:
				screen_title = f"Songs - Page {song_page}"
			if event.key == pygame.K_p:
				if pause_state == "play":
					pause_state = "pause"
					pygame.mixer.music.pause()
				else:
					pause_state = "play"
					pygame.mixer.music.unpause()
			if event.key == pygame.K_r:
				repeat = bool(1-int(repeat))

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
						save_to_file(save_file_path)
						sys.exit()
				if next_page_button is not None:
					touching_next_page_button = next_page_button.collidepoint(event.pos)
					if touching_next_page_button:
						song_page += 1
						if song_page > max_song_pages:
							song_page -= 1
						screen_title = f"Songs - Page {song_page}"
				if previous_page_button is not None:
					touching_previous_page_button = previous_page_button.collidepoint(event.pos)
					if touching_previous_page_button:
						song_page -= 1
						if song_page < 1:
							song_page += 1
						screen_title = f"Songs - Page {song_page}"
				if play_pause_button is not None:
					touching_play_pause_button = play_pause_button.collidepoint(event.pos)
					if touching_play_pause_button:
						if playing_song == None:
							text_pause_state = "No song playing"
						else:
							if pause_state == "play":
								text_pause_state = "pause"
							else:
								text_pause_state = "play"
							if pause_state == "play":
								pause_state = "pause"
								pygame.mixer.music.pause()
							else:
								pause_state = "play"
								pygame.mixer.music.unpause()
				if repeat_button is not None:
					touching_repeat_button = repeat_button.collidepoint(event.pos)
					if touching_repeat_button:
						repeat = bool(1-int(repeat))

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
				if screen_title == "Songs - Page 3":
					check_touching_song_button(ppom_button,"Phantom Peak Overworld Music")
					check_touching_song_button(jo_button,"Jonaco Oath")
					check_touching_song_button(mi_button,"Monstermon Intro")
					check_touching_song_button(eot_button,"Eggs Of Truth")

	screen.fill(colours["background"])
	next_page_button = None
	previous_page_button = None
	colour_mode_button = None
	quit_button = draw_button_with_offset_from_corner("gray",screen_width-120,screen_height-75,100,50,"Quit","black",35)
	if screen_title == "Main Menu":
		surface = draw_text_with_offset_from_centre(0,-50,greeting_message,True,colours["general"],100)
		surface = draw_text_with_offset_from_centre(0,0,f"Current Song: {playing_song}",True,colours["general"],50)
		surface = draw_text_with_offset_from_centre(0,50,"Subtitle 2",True,colours["general"],50)
		colour_mode_button = draw_button_with_offset_from_centre("gray",0,200,200,50,f"{other_colour_mode.capitalize()} Mode","black",35)
		date = draw_text_with_offset_from_corner(0,10,f"Date: {year}-{month}-{date}",35,colours["general"])
		time = draw_text_with_offset_from_corner(0,35,f"Time: {hour}:{minute}:{second}",35,colours["general"])
		help_menu = draw_text_with_offset_from_centre(screen_centre_width-150,0-screen_centre_height+100,"Space - Light/dark mode\nEscape - Quit\n0-2 - Change menu",True,colours["general"],35)
	if screen_title == "Example Title":
		surface = draw_text_with_offset_from_centre(0,-50,greeting_message,True,colours["general"],100)
		surface = draw_text_with_offset_from_centre(0,0,f"Current Song: {playing_song}",True,colours["general"],50)
		if pause_state == "pause":
			surface = draw_text_with_offset_from_centre(0,50,f"{formatted_song_time}/{formatted_song_length} - Paused",True,colours["general"],50)
		else:
			surface = draw_text_with_offset_from_centre(0,50,f"{formatted_song_time}/{formatted_song_length}",True,colours["general"],50)
	if screen_title == "Songs - Page 1":
		# Column 1 (songs 1-12)
		ah_button = draw_button_with_offset_from_corner("gray",10,30,600,50,"Alexander Hamilton","black",35,"Alexander Hamilton")
		abs_button = draw_button_with_offset_from_corner("gray",10,90,600,50,"Aaron Burr, Sir","black",35,"Aaron Burr, Sir")
		ms_button = draw_button_with_offset_from_corner("gray",10,150,600,50,"My Shot","black",35,"My Shot")
		tsot_button = draw_button_with_offset_from_corner("gray",10,210,600,50,"The Story of Tonight","black",35,"The Story of Tonight")
		tss_button = draw_button_with_offset_from_corner("gray",10,270,600,50,"The Schuyler Sisters","black",35,"The Schuyler Sisters")
		fr_button = draw_button_with_offset_from_corner("gray",10,330,600,50,"Farmer Refuted","black",35,"Farmer Refuted")
		ybb_button = draw_button_with_offset_from_corner("gray",10,390,600,50,"You'll Be Back","black",35,"You'll Be Back")
		rhm_button = draw_button_with_offset_from_corner("gray",10,450,600,50,"Right Hand Man","black",35,"Right Hand Man")
		awb_button = draw_button_with_offset_from_corner("gray",10,510,600,50,"A Winter's Ball","black",35,"A Winter's Ball")
		h_button = draw_button_with_offset_from_corner("gray",10,570,600,50,"Helpless","black",35,"Helpless")
		s_button = draw_button_with_offset_from_corner("gray",10,630,600,50,"Satisfied","black",35,"Satisfied")
		tsotr_button = draw_button_with_offset_from_corner("gray",10,690,600,50,"The Story of Tonight (Reprise)","black",35,"The Story of Tonight (Reprise)")

		# Column 2 (songs 13-23)
		wfi_button = draw_button_with_offset_from_corner("gray",650,30,600,50,"Wait For It","black",35,"Wait for It")
		sa_button = draw_button_with_offset_from_corner("gray",650,90,600,50,"Stay Alive","black",35,"Stay Alive")
		tdc_button = draw_button_with_offset_from_corner("gray",650,150,600,50,"Ten Duel Commandments","black",35,"Ten Duel Commandments")
		mmi_button = draw_button_with_offset_from_corner("gray",650,210,600,50,"Meet Me Inside","black",35,"Meet Me Inside")
		twbe_button = draw_button_with_offset_from_corner("gray",650,270,600,50,"That Would Be Enough","black",35,"That Would Be Enough")
		gas_button = draw_button_with_offset_from_corner("gray",650,330,600,50,"Guns and Ships","black",35,"Guns and Ships")
		hhieon_button = draw_button_with_offset_from_corner("gray",650,390,600,50,"History Has Its Eyes On You","black",35,"History Has Its Eyes On You")
		y_button = draw_button_with_offset_from_corner("gray",650,450,600,50,"Yorktown (The World Turned Upside Down)","black",35,"Yorktown (The World Turned Upside Down)")
		wcn_button = draw_button_with_offset_from_corner("gray",650,510,600,50,"What Comes Next?","black",35,"What Comes Next")
		dt_button = draw_button_with_offset_from_corner("gray",650,570,600,50,"Dear Theodosia","black",35,"Dear Theodosia")
		ns_button = draw_button_with_offset_from_corner("gray",650,630,600,50,"Non-Stop","black",35,"Non-Stop")

		next_page_button = draw_button_with_offset_from_corner("gray",650,690,600,50,"Next Page ->","black",35,"Next Page ->")
		play_pause_button = draw_button_with_offset_from_corner("gray",10,750,600,50,text_pause_state.capitalize(),"black",35,text_pause_state.capitalize())
		repeat_button = draw_button_with_offset_from_corner("gray",1290,30,130,75,f"Repeat: \n{repeat}","black",35,f"Repeat: \n{repeat}")

	if screen_title == "Songs - Page 2":
		# Column 1 (songs 24-35)
		wim_button = draw_button_with_offset_from_corner("gray",10,30,600,50,"What'd I Miss","black",35,"What'd I Miss")
		cb1_button = draw_button_with_offset_from_corner("gray",10,90,600,50,"Cabinet Battle #1","black",35,"Cabinet Battle #1")
		tab_button = draw_button_with_offset_from_corner("gray",10,150,600,50,"Take A Break","black",35,"Take a Break")
		sntt_button = draw_button_with_offset_from_corner("gray",10,210,600,50,"Say No To This","black",35,"Say No To This")
		trwih_button = draw_button_with_offset_from_corner("gray",10,270,600,50,"The Room Where It Happens","black",35,"The Room Where It Happens")
		sd_button = draw_button_with_offset_from_corner("gray",10,330,600,50,"Schuyler Defeated","black",35,"Schuyler Defeated")
		cb2_button = draw_button_with_offset_from_corner("gray",10,390,600,50,"Cabinet Battle #2","black",35,"Cabinet Battle #2")
		woys_button = draw_button_with_offset_from_corner("gray",10,450,600,50,"Washington On Your Side","black",35,"Washington On Your Side")
		olt_button = draw_button_with_offset_from_corner("gray",10,510,600,50,"One Last Time","black",35,"One Last Time")
		ikh_button = draw_button_with_offset_from_corner("gray",10,570,600,50,"I Know Him","black",35,"I Know Him")
		taa_button = draw_button_with_offset_from_corner("gray",10,630,600,50,"The Adams Administration","black",35,"The Adams Administration")
		wk_button = draw_button_with_offset_from_corner("gray",10,690,600,50,"We Know","black",35,"We Know")

		# Column 2 (songs 36-46)
		hu_button = draw_button_with_offset_from_corner("gray",650,30,600,50,"Hurricane","black",35,"Hurricane")
		trp_button = draw_button_with_offset_from_corner("gray",650,90,600,50,"The Reynolds Pamphlet","black",35,"The Reynolds Pamphlet")
		b_button = draw_button_with_offset_from_corner("gray",650,150,600,50,"Burn","black",35,"Burn")
		buaa_button = draw_button_with_offset_from_corner("gray",650,210,600,50,"Blow Us All Away","black",35,"Blow Us All Away")
		sar_button = draw_button_with_offset_from_corner("gray",650,270,600,50,"Stay Alive (Reprise)","black",35,"Stay Alive (Reprise)")
		iqu_button = draw_button_with_offset_from_corner("gray",650,330,600,50,"It's Quiet Uptown","black",35,"It's Quiet Uptown")
		teo1800_button = draw_button_with_offset_from_corner("gray",650,390,600,50,"The Election of 1800","black",35,"The Election of 1800")
		yos_button = draw_button_with_offset_from_corner("gray",650,450,600,50,"Your Obedient Servant","black",35,"Your Obedient Servant")
		bowabow_button = draw_button_with_offset_from_corner("gray",650,510,600,50,"Best of Wives and Best of Women","black",35,"Best of Wives and Best of Women")
		twwwe_button = draw_button_with_offset_from_corner("gray",650,570,600,50,"The World Was Wide Enough","black",35,"The World Was Wide Enough")
		wlwdwtys_button = draw_button_with_offset_from_corner("gray",650,630,600,50,"Who Lives, Who Dies, Who Tells Your Story","black",35,"Who Lives, Who Dies, Who Tells Your Story")

		next_page_button = draw_button_with_offset_from_corner("gray",650,690,600,50,"Next Page ->","black",35,"Next Page ->")
		play_pause_button = draw_button_with_offset_from_corner("gray",10,750,600,50,text_pause_state.capitalize(),"black",35,text_pause_state.capitalize())
		previous_page_button = draw_button_with_offset_from_corner("gray",650,750,600,50,"<- Previous Page","black",35,"<- Previous Page")
		repeat_button = draw_button_with_offset_from_corner("gray",1290,30,130,75,f"Repeat: \n{repeat}","black",35,f"Repeat: \n{repeat}")

	if screen_title == "Songs - Page 3":
		ppom_button = draw_button_with_offset_from_corner("gray",10,30,600,50,"Overworld Music","black",35,"Phantom Peak Overworld Music")
		jo_button = draw_button_with_offset_from_corner("gray",10,90,600,50,"Jonaco Oath","black",35,"Jonaco Oath")
		mi_button = draw_button_with_offset_from_corner("gray",650,30,600,50,"Monstermon Intro","black",35,"Monstermon Intro")
		eot_button = draw_button_with_offset_from_corner("gray",650,90,600,50,"Eggs of Truth","black",35,"Eggs Of Truth")
		play_pause_button = draw_button_with_offset_from_corner("gray",10,750,600,50,text_pause_state.capitalize(),"black",35)
		previous_page_button = draw_button_with_offset_from_corner("gray",650,750,600,50,"<- Previous Page","black",35)
		repeat_button = draw_button_with_offset_from_corner("gray",1290,30,130,75,f"Repeat: \n{repeat}","black",35)
	
	title = pygame.display.set_caption(f"{window_title} - {colour_mode.capitalize()} Mode")

	pygame.display.flip()
