import platform
import pyfiglet
import os
import random
import datetime
import pyttsx3
import pyautogui as pt
import time 
import playsound
import pywhatkit

engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

os.chdir('c:\\users\\RS21\\Desktop\\Python@Projects')

def starting():
	print('[*] ',end='')
	print('Initialising sequence..')
	print('[*] ',end='')
	print('Importing prefences from the home interface..')
	print()
	#playsound.playsound(random.choice(['jarvis_on.mp3','jarvis_morning_boost.mp3']))
	playsound.playsound('jarvis_on.mp3')
	playsound.playsound('jarvis_access.mp3')
	print('ASSISTANT NAME : FRIDAY-FEMALE REPLACEMENT INTELLIGENT DIGITAL ASSISTANT YOUTH')
	print("SYSTEM : ",platform.system() + ' ' + platform.release())
	#log('I HAVE INDEED BEEN UPLOADED SIR. WE ARE ONLINE AND READY.. ')
	# log('WELCOME BACK SIR !')

def open_new_shell(x):
	pt.hotkey('winleft','r')
	pt.typewrite('cmd')
	pt.typewrite(['enter'])
	time.sleep(0.5)
	pt.typewrite('color  0a')
	pt.typewrite(['enter'])
	pt.typewrite('cd Desktop//Python@Projects')
	pt.typewrite(['enter'])
	time.sleep(0.5)
	pt.typewrite(x)
	pt.typewrite(['enter'])

def print_and_say(x):
	print(x)
	speak(x)

def speak(t):
	engine.say(t)
	engine.runAndWait()

def log(var):
	print_and_say(var)
	log_file = open(r'C:\Users\RS21\Desktop\Python@Projects\log.txt','a')
	log_file.write(var + '\n')
	log_file.close()

def only_log(var):
	log_file = open(r'C:\Users\RS21\Desktop\Python@Projects\log.txt','a')
	log_file.write(var + '\n')
	log_file.close()

def send_mail(send_to,text):
	import smtplib
	username="tony60687@gmail.com"
	passwd = "!2021rohan2021!"
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
	playsound.playsound(music_dir_loc + '\\' + songs_list[int(song_index)])

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
		while type(song_index) != "<class 'int'>":

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

check_os()

greeting = pyfiglet.figlet_format("WELCOME BOSS !")
print(greeting)

cur_time = datetime.datetime.now().strftime('%I:%M %p')
cur_date = datetime.datetime.now().strftime('%d ' '%b ' '%Y')
time = int(datetime.datetime.now().strftime('%H'))

if time < 12:
	log('A very Good Morning sir !')
elif time > 18:
	log('Good Evening sir !')
else:
	log('Good Afternoon Sir !')
only_log('______________________________________________________________________________________________________' + ' \n'
+ cur_date + ' ' + cur_time + '\n'
)

starting()

chat = {'who is jarvis ':'JARVIS stands for JUST A RATHER VERY INTELLIGENT SYSTEM.',
'boom ':'superboom !','who is ironman ':'He is just a man in can. well by the way sir, you are the real IRONMAN and i am your JARVIS.',
'who ? ':'I am JARVIS. your virtual ASSISTANT.','why ':'what why? ask complete questions.. ','wtf ':'what the FUCK.',
'how ': 'what how? ask complete questions..','okay ':'all right !','oky ':'alright !','kk ':'alright !','when ':'what ? ask complete questions.',
'shutdown ': 'shutting down the system...','love u ':'love you too sir.', 
'what ': 'what what ? ', 'who ': 'what who?  ask complete questions.','haha ':'why are you laughing sir ?',
'who are you ? ':'I am JARVIS. your virtual ASSISTANT.','good morning':'good morning sir !','hello ':'hello sir ! '
}

user_input = ['hi ','hello ']
greeting_close = ['bye ','nice talking to you ','have a good day ' , 'we will meet soon ','get lost ','bye bye ']
say_intro_line = ['who are you ','who ','who ? ' ,'what is your name ? ','your name ? ']

try:
	while True:
		x = input("YOU :")
		only_log(var='YOU : ' + x )
		if x in chat.keys():
			log(chat[x]  + '\n')

		else:
			cmd = x.split()
			import webbrowser as wb

			if 'wiki' in x:
				topic = x.replace('wiki', '')
				import wikipedia
				log(wikipedia.summary(topic,sentences=2) + '\n')

			elif 'help' in x :
				for i in chat:
					print(i + ": " + chat[i])
					total_commands = len(chat.keys())
				#log('total number of commands is '+ str(total_commands) + '.')

			elif 'cat' in x :
				file_name =  x.replace('cat ', '')
				try:
					open_file = open(os.getcwd() + '\\' + file_name,'r')
					text = open_file.readlines()
					for i in range(len(text)):
						print(text[i].replace('\\n','\n'))
					only_log('< Displays text inside ' + file_name + '>')					

				except Exception as e :
					log(str(e) + '\n')

			elif 'typing_speed' in x:
				wb.open('https://10fastfingers.com/typing-test/english')
				log('Here you go sir !' + '\n')
			
			# elif "random_song " in x:
			# 	import random
			# 	import playsound
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
				(random.choice(user_input) + '! ')
			elif x.lower() in say_intro_line:
				log('I am JARVIS. your virtual ASSISTANT.' + '\n')
			elif x.lower() in greeting_close:
				log(random.choice(greeting_close) + 'sir !' + '\n')
				os.system('cls')
				break
			


			elif 'sys' in x :
				sys_command = x.replace('sys', '')
				os.system(sys_command)
			# elif cmd[0].lower() =="quotes":
			# 	import random
			# 	g = random.randint(0,len(motivational_quotes))
			# 	print(motivational_quotes[g])
			
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

			elif 'open' in x :
				programs = x.replace('open', '')
				p_l = programs.split(' ')
				if 'firefox' in p_l:
					log('opening Firefox !' + '\n')
					os.system('"C:\\Program Files\\Mozilla Firefox\\firefox.exe"')
					
				if 'sublime' in p_l:
					log('opening Sublime !' + '\n')
					os.system('"C:\\Program Files\\Sublime Text 3\\sublime_text.exe"')
					
				if 'notepad' in p_l:
					log('opening Notepad !' + '\n')
					os.system('%windir%\\system32\\notepad.exe')
					
				if 'vlc' in p_l:
					log('opening VLC Media Player !' + '\n')
					os.system('"C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"')
					
				if 'youtube' in p_l:
					log('opening Youtube !' + '\n')
					wb.open('www.youtube.com')

				if 'whatsapp' in p_l: 
					log('opening Whatsapp !' + '\n')
					wb.open('web.whatsapp.com')
					
				if 'google' in p_l:
					log('opening Google !' + '\n')
					wb.open('www.google.com')

				if 'code' in p_l:
					os.system('"C:\\Users\\RS21\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"')

			elif 'joke' in x :
				import pyjokes
				joke = pyjokes.get_joke()
				log(joke + '\n')

			elif 'time' in x:
				time = datetime.datetime.now().strftime('%I:%M %p')
				log('current time is ' + str(time) + '\n')
			
			elif 'shutdown -h now ' in x :
				os.system('shutdown -s -t 0')
				log('shutting down the system ..')

			elif 'music' in x:
				music_dir_loc = 'C:\\Users\\RS21\\Music\\audio_file'
				os.chdir(music_dir_loc)
				songs_list = os.listdir(music_dir_loc)
				while True:
					play_song()
					if other_song =='y':
						play_song()
					else:
						break

			elif 'video' in x :
				video_dir_loc = "c:\\Users\\RS21\\Videos"
				from moviepy.editor import *
				os.chdir(video_dir_loc)
				videos_list = os.listdir(video_dir_loc)
				for i in range(len(videos_list)):
					print(str(i) + ' ' + videos_list[i])
				y = input(': ')
				clip = VideoFileClip('c:\\users\\RS21\\Videos' + '\\'+videos_list[int(y)])
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
				print(x)
				if x == 'easy':
					a = random.randint(10,40)
					b = random.randint(10,40)
					print('A: ',a)
					print('B: ',b)
					output = input('output: ')
					if int(output) == a * b:
						print_and_say('YOU WIN !')
					else:
						print_and_say('Try Again !')
				elif x =='medium':
					a = random.randint(41,70)
					b = random.randint(41,70)
					print('A: ',a)
					print('B: ',b)
					output = input('output: ')
					if int(output) == a * b:
						print_and_say('YOU WIN !')
					else:
						print_and_say('Try Again !')
				elif x =='hard':
					a = random.randint(71,99)
					b = random.randint(71,99)
					print('A: ',a)
					print('B: ',b)
					output = input('output: ')
					if int(output) == a * b:
						print_and_say('YOU WIN !')
					else:
						print_and_say('Try Again !')

			else:
				log('Unable to process the query..')
except Exception as error:
	only_log(error + '\n')

