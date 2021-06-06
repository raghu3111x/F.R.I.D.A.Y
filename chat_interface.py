import time
start = time.perf_counter()
import tkinter as tk
from tkinter import ttk 
from tkinter import *
from tkinter import scrolledtext
from PIL import ImageTk,Image
import platform
import pyfiglet
import os
import random
import datetime
import pyttsx3
import playsound
import pywhatkit
import pyautogui as pt
import webbrowser as wb
import keyboard
import getpass
from moviepy.editor import *
import wikipedia
import pyjokes

stop = time.perf_counter()

print(stop - start)

uname = getpass.getuser()
main_directory = os.getcwd()
engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

user_input = ['hi ','hello ']
greeting_close = ['bye ','nice talking to you ','have a good day ' , 'we will meet soon ','get lost ','bye bye ']
say_intro_line = ['who are you ','who ','who ? ' ,'what is your name ? ','your name ? ']

chat = {'who is jarvis ':'JARVIS stands for JUST A RATHER VERY INTELLIGENT SYSTEM.',
'boom ':'superboom !','who is ironman ':'He is just a man in can. well by the way sir, you are the real IRONMAN and i am your JARVIS.',
'who ? ':'I am JARVIS. your virtual ASSISTANT.','why ':'what why? ask complete questions.. ','wtf ':'what the FUCK.',
'how ': 'what how? ask complete questions..','okay ':'all right !','oky ':'alright !','kk ':'alright !','when ':'what ? ask complete questions.',
'shutdown ': 'shutting down the system...','love u ':'love you too sir.', 
'what ': 'what what ? ', 'who ': 'what who?  ask complete questions.','haha ':'why are you laughing sir ?',
'who are you ? ':'I am JARVIS. your virtual ASSISTANT.','good morning':'good morning sir !','hello ':'hello sir ! ','hi ':'hello sir ...!'
}

def close_window():
	win.destroy()

def del_inputtext(selff):
	inputtext.delete('0','end')

def starting():
	import time
	only_log('[*] ',end='')
	#time.sleep(0.5)
	only_log('Initialising sequence..')
	#time.sleep(0.5)
	only_log('[*] ',end='')
	only_log('Importing prefences from the home interface..')
	#ime.sleep(0.5)
	print()
	#playsound.playsound(random.choice(['jarvis_on.mp3','jarvis_morning_boost.mp3']))
	playsound.playsound('jarvis_on.mp3')
	playsound.playsound('jarvis_access.mp3')
	only_log('ASSISTANT NAME : JUST A VERY INTELLIGENT SYSTEM')
	only_log("SYSTEM : ",platform.system() + ' ' + platform.release())
	#log('I HAVE INDEED BEEN UPLOADED SIR. WE ARE ONLINE AND READY.. ')
	# log('WELCOME BACK SIR !')

def open_new_shell(x):
	import pyautogui as pt
	import time
	pt.hotkey('winleft','r')
	pt.typewrite('cmd')
	pt.typewrite(['enter'])
	time.sleep(0.5)
	pt.typewrite('color  0a')
	pt.typewrite(['enter'])
	pt.typewrite(main_directory)
	pt.typewrite(['enter'])
	time.sleep(0.5)
	pt.typewrite(x)
	pt.typewrite(['enter'])

def print_and_say(x):
	print(x)
	say(x)

def say(t):
	engine.say(t)
	engine.runAndWait()

def log(var):
	output.insert(END, 'YOU : ' + x + '\n')
	output.insert(END, var + '\n' +'\n')
	output.see(tk.END)
	say(var)
	del_inputtext(selff)
	log_file = open(main_directory + '\\log.txt','a')
	log_file.write(var + '\n')
	log_file.close()

def only_log(var):
	log_file = open(main_directory + '\\log.txt','a')
	log_file.write(var + '\n')
	log_file.close()
	output.insert(END, 'YOU : ' + x + '\n')
	output.insert(END, var + '\n' +'\n')
	output.see(tk.END)
	del_inputtext(selff)

def send_mail(send_to,text):
	import smtplib
	username=input('Enter the username: ')
	passwd = input('Enter the password: ')
	smtpObj = smtplib.SMTP('smtp.gmail.com',587)
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.login(username, passwd)
	log('login attempt successful')
	smtpObj.sendmail(username,send_to,text)
	log('message send successfully.')
	playsound.playsound('jarvis_message_sent.mp3')

def only_play_song():
	log("playing  " + str(songs_list[int(song_index)]))
	speak('Sir, Do you want me to open new command prompt ?')
	new_terminal = input('Sir, Do you want me to open new command prompt ?(Y/N)' + '\n' + ': ')
	if new_terminal.lower() =='y':
		log("opening new shell while you are listening to music..")
		open_new_shell('cls')
	else:
		pass
	try:
		playsound.playsound(music_dir_loc + '\\' + songs_list[int(song_index)])
	except KeyboardInterrupt :
		pass

def play_song():
	for i in range(len(songs_list)):
		print(str(i) + ' ' + songs_list[i])
				
	engine.say('Enter the index of the song sir !')
	engine.runAndWait()
	global song_index
	song_index = input(': ')
	if song_index.isnumeric():
		only_play_song()

	else:
		while song_index.isnumeric() != "True":

			log('only enter an integer without space sir !' + '\n')
			song_index = input(': ')
			if song_index.isnumeric():
				play_song()
				global other_song
				other_song = input('Sir, Do you want me to play other song ?(Y/N) ' + '\n' + ': ')
				speak('Sir, Do you want me to play other song ? ')
				only_log('Sir, Do you want me to play other song ? ')


def motivation():
	motivational_quotes = ["Don’t say you don’t have enough time. You have exactly the same number of hours per day that were given to Helen Keller, Pasteur, Michelangelo, Mother Teresa, Leonardo Da Vinci, Thomas Jefferson, and Albert Einstein.",
'Hard work beats talent when talent doesn’t work hard.','If everything seems to be under control, you’re not going fast enough.',
"don't ever stop doing your best just because someone doesn’t give you credit.",'If you work on something a little bit every day, you end up with something that is massive.',
' Two roads diverged in a wood, and I took the one less traveled by, And that has made all the difference.',
'We become what we think about.','The most common way people give up their power is by thinking they don’t have any.',
'If you want to find the secrets of the universe, think in terms of energy, frequency and vibration.','Of all things, I liked books best.',
'I dont care that they stole my idea . . I care that they dont have any of their own','Be alone, that is the secret of invention; be alone, that is when ideas are born.',
'The present is theirs; the future, for which I really worked, is mine.','I shouldn’t be alive, unless it was for a reason. I’m not crazy. I just finally know what I have to do. And I know in my heart that it’s right.'

]	
	# #for i in range(int(cmd[2])):
	# g = random.randint(0,int(len(motivational_quotes))-1)
	# log(motivational_quotes[g])
	log(random.choice(motivational_quotes))
def check_os():
	if os.name == 'nt':
		os.system('color 0a')
		os.system('cls')
	else:
		pass

def cur_time():
	cur_time = datetime.datetime.now().strftime('%I:%M %p')
	log(cur_time)

def cur_date():
	cur_date = datetime.datetime.now().strftime('%d ' '%b ' '%Y')
	log(cur_date)

def change_color():
	bg = [0,1,2,3,4,5,6,7]
	fg = [8,9,'a','b','c','d','e','f']
	pt.typewrite('color ' + str(random.choice(bg)) + str(random.choice(fg)))

def take_input(selff):
	global x
	x = inputtext.get()
	if x in chat.keys():
		log(chat[x]  + '\n')
	elif x in greeting_close:
		close_window()		

	else:
		cmd = x.split('&&')
		for i in range(len(cmd)):
			x = cmd[i]
			if 'wiki' in x:
				topic = x.replace('wiki', '')
				log(wikipedia.summary(topic,sentences=2) + '\n')

			elif 'help' in x :
				for i in chat:
					print(i + ": " + chat[i])
					total_commands = len(chat.keys())
				#log('total number of commands is '+ str(total_commands) + '.')
			elif 'change color' in x :
				change_color()

			elif 'cat' in x :
				file_name =  x.replace('cat ', '')
				try:
					open_file = open(os.getcwd() + '\\' + file_name,'r')
					text = open_file.readlines()
					for i in range(len(text)):
						only_log(text[i].replace('\\n','\n'))
					only_log('< Displays text inside ' + file_name + '>')					

				except Exception as e :
					only_log(str(e) + '\n')
					only_log(str(e) + '\n' )

			elif 'typing_speed' in x:
				wb.open('https://10fastfingers.com/typing-test/english')
				log('Here you go sir !' + '\n')
				close_window()
			# elif "random_song " in x:
			# 	songs_list = os.listdir(music_dir_loc)
			# 	j = len(songs_list)
			# 	r = random.randint(0,j)
			# 	log("plyaing some random song..")
			# 	print("Song Name: ",songs_list[int(r)])
			# 	playsound.playsound(music_dir_loc + "\\" + songs_list[int(r)])
			elif x =='oye ' or x =='oye jarvis ':
				log(random.choice(['G sir ? ','yes sir ? ']) + '\n')

			elif 'cmd' in x:
				command = x.replace('cmd', '')
				open_new_shell(command)

			elif x.lower() in user_input:
				log(random.choice(user_input) + '! ')
			elif x.lower() in say_intro_line:
				log('I am JARVIS. your virtual ASSISTANT.' + '\n')
			elif x.lower() in greeting_close:
				log(random.choice(greeting_close) + 'sir !' + '\n')
				close_window()
			
			elif x =='reboot ':
				log('Rebooting the Jarvis-Shell-Interface !')
				os.system('cls && python bot.py')
				break
			# elif cmd[0].lower() =="quotes":
			# 	g = random.randint(0,len(motivational_quotes))
			# 	print(motivational_quotes[g])
			
			elif x=='crash ':
				open_new_shell(x)
				for i in range(random.randint(500, 600)):
					change_color()
				os.system('color 0a')


			elif 'quote' in x:
				motivation()

			elif 'play' in x:
				song = x.replace('play', '')
				log('Playing ' +song.upper() + '!' + '\n')
				pywhatkit.playonyt(song)

			elif 'jarvis' and 'remember ' in x:
				memory = x.replace('jarvis','')
				mem_file = open(os.getcwd() + '\\'+'remember.txt','a')
				mem_file.write(' and ' + memory)
				mem_file.close()
				log('Message added to the remember list..')

			elif 'remember-list ' in x :
				mem_file = open(os.getcwd() + '\\'+'remember.txt','r')
				mem_lines = mem_file.readlines()
				log(mem_lines[0])

			elif 'download' in x :
				try:
					topic = x.replace('download', '')
					lines = input("Enter the number of lines : ")
					info = wikipedia.summary(topic,sentences=int(lines))
					topic_file = open(os.getcwd() + '\\' + topic + '.txt','a')
					topic_file.write(info)
					topic_file.close()
					log('File saved as ' + topic + '.txt')
				except Exception as error:
					log('Download Incomplete !')
					only_log(error)
			elif 'dream journal' in x :
				blog = input('\n' + ': ')
				dream_file = open('dream_journal.txt','w')
				dream_file.write(blog)
				dream_file.close()
				print()

			elif 'open' in x :
				programs = x.replace('open', '')
				p_l = programs.split(' ')
				if 'firefox' in p_l:
					log('opening Firefox !' + '\n')
					os.system('"C:\\Program Files\\Mozilla Firefox\\firefox.exe"')
					
				if 'sublime' in p_l:
					log('opening Sublime !' + '\n')
					os.system('"C:\\Program Files\\Sublime Text 3\\sublime_text.exe"')
					
				if 'keybr' in p_l:
					log("Opening Keybr !")
					wb.open('www.keybr.com')

				if 'notepad' in p_l:
					log('opening Notepad !' + '\n')
					os.system('%windir%\\system32\\notepad.exe')
					
				if 'vlc' in p_l:
					log('opening VLC Media Player !' + '\n')
					os.system('"C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"')
					
				if 'youtube' in p_l:
					log('opening Youtube !' + '\n')
					wb.open('www.youtube.com')

				elif 'task manager' in x:
					log("Opening Task-Manager !")
					os.system(r'%windir%\system32\taskmgr.exe /7')

				if 'whatsapp' in p_l: 
					log('opening Whatsapp !' + '\n')
					wb.open('web.whatsapp.com')
					
				if 'google' in p_l:
					log('opening Google !' + '\n')
					wb.open('www.google.com')

				if 'impress' in p_l:
					log('Opening Microsoft Impress !')
					os.system(r'C:\Program Files\LibreOffice\program\simpress.exe')

				if 'wordpad' in p_l:
					log('Opening Microsoft Wordpad')
					os.system(r"%ProgramFiles%\Windows NT\Accessories\wordpad.exe")

				if 'sticky notes' in p_l:
					log('Opening sticky notes !')
					os.system(r"%windir%\system32\StikyNot.exe")

				if 'quora' in p_l:
					wb.open('quora.com')


				if 'code' in p_l:
					os.system('"C:\\Users\\' + uname + '\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"')

			elif 'joke' in x :
				joke = pyjokes.get_joke()
				log(joke + '\n')

			elif 'time' in x:
				time = datetime.datetime.now().strftime('%I:%M %p')
				log('current time is ' + str(time) + '\n')
			
			elif 'shutdown -h now ' in x :
				os.system('shutdown -s -t 0')
				log('shutting down the system ..')

			elif 'music' in x:
				music_dir_loc = 'C:\\Users\\' + uname + '\\Music\\audio_file'
				os.chdir(music_dir_loc)
				songs_list = os.listdir(music_dir_loc)
				while True:
					play_song()
					if other_song =='y':
						play_song()
					else:
						break

			elif 'video' in x :
				video_dir_loc = "c:\\Users\\' + uname + '\\Videos"
				os.chdir(video_dir_loc)
				videos_list = os.listdir(video_dir_loc)
				for i in range(len(videos_list)):
					only_log(str(i) + ' ' + videos_list[i])
				y = input(': ')
				clip = VideoFileClip('c:\\users\\' + uname + '\\Videos' + '\\'+videos_list[int(y)])
				clip.ipython_display(width=280)
			
			elif 'send mail' in x :
				mail_to = x.replace('send mail to','')
				speak("what should it say: ")
				msg= input("what should it say? \n " + ': ')
				send_mail(send_to=mail_to,text=msg)

			elif 'mute' in x :
				try:
					x = x.replace('mute ','' )
					for i in range(int(x)):
						pt.typewrite(['volumemute'])
					#only_log(' < Volume Muted > ')
				except Exception:
					pt.typewrite(['volumemute'])
			elif 'volume up' in x:
				x = x.replace('volume up ','')
				for i in range(int(x)):
					pt.typewrite(['volumeup'])
			elif 'volume down' in x :
				x = x.replace('volume down ','')
				for i in range(int(x)):
					pt.typewrite(['volumedown'])

			elif 'calc-game' in x :
				x = x.replace('calc-game ','')
				if 'easy' in x :
					a = random.randint(10,40)
					b = random.randint(10,40)
					only_log('A: ',a)
					only_log('B: ',b)
					output = input('output: ')
					if int(output) == a * b:
						log('YOU WIN !' + '\n')
					else:
						while int(output) != a * b:
							log('Try Again !')
							only_log('\n')
							output = input('output: ')
							if int(output) == a * b:
								log('YOU WIN !' + '\n')


				elif 'medium' in x :
					a = random.randint(41,70)
					b = random.randint(41,70)
					only_log('A: ',a)
					only_log('B: ',b)
					output = input('output: ')
					if int(output) == a * b:
						log('YOU WIN !')
					else:
						while int(output) != a * b:
							log('Try Again !')
							only_log('\n')
							output = input('output: ')
							if int(output) == a * b:
								log('YOU WIN !' + '\n')
				elif 'hard' in x :
					a = random.randint(71,99)
					b = random.randint(71,99)
					only_log('A: ',a)
					only_log('B: ',b)
					output = input('output: ')
					if int(output) == a * b:
						log('YOU WIN !')
					else:
						while int(output) != a * b:
							log('Try Again !')
							only_log('\n')
							output = input('output: ')
							if int(output) == a * b:
								log('YOU WIN !' + '\n')
				elif x=='exit':
					close_window()

			else:
				only_log(os.popen(x).read())
					

global selff
selff = None


win = tk.Tk()
ironman_img = ImageTk.PhotoImage(Image.open('ironman.jpg'))
panel = tk.Label(win,image=ironman_img)
panel.pack(side='right',fill='both',expand='yes')

win.title('ARTIFICIAL INTELLIGENCE')
greeting = tk.Label(text='I am Jarvis. Your virtual assistant : )')
greeting.pack()
inputtext = tk.Entry(width=106)
#inputtext.bind('<Return>',lambda x:[take_input,del_inputtext])
inputtext.bind('<Return>',take_input)
label1 = tk.Label(text = 'Jarvis Interface !',width = 100,height=1)
# button1 = tk.Button(text ='Click Me !')
# button2 = tk.Button(text ='QUIT ?')
#button1.pack()
#button2.pack()
output = tk.scrolledtext.ScrolledText(height=30)
output.pack()
output.insert(END, 'Output will be displayed here !' + '\n')
inputtext.pack()
#x = inputtext.get('0',tk.END)
label1.pack(fill=tk.X)
inputtext.insert(0,'Type Here !')
# close_button = tk.Button(win,text='QUIT ?',command =close_window)
# close_button.pack()

# events_list = []

# def handle_keypress(event):
# 	print(event.char)

# Bind keypress event to handle_keypress
#win.bind('<Return>',handle_keypress)
win.mainloop()
