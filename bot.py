import platform
import pyfiglet
import os
import random
import datetime
import pyttsx3
#import pyautogui as pt
import time 
import pywhatkit

engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

music_dir_loc = 'C:\\Users\\RS21\\Music'
video_dir_loc = "c:\\Users\\RS21\\Videos"

def open_new_shell(x):
	import pyautogui as pt
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
	say(x)

def say(t):
	engine.say(t)
	engine.runAndWait()
def send_mail(send_to,text):
	import smtplib
	username="tony60687@gmail.com"
	passwd = "!2021rohan2021!"
	smtpObj = smtplib.SMTP('smtp.gmail.com',587)
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.login(username, passwd)
	print_and_say('login attempt successful')
	smtpObj.sendmail(username,send_to,text)
	print_and_say('message send successfully.')
def motivation():

	motivational_quotes = ["Don’t say you don’t have enough time. You have exactly the same number of hours per day that were given to Helen Keller, Pasteur, Michelangelo, Mother Teresa, Leonardo Da Vinci, Thomas Jefferson, and Albert Einstein.",
'Hard work beats talent when talent doesn’t work hard.','If everything seems to be under control, you’re not going fast enough.',
"don't ever stop doing your best just because someone doesn’t give you credit.",'If you work on something a little bit every day, you end up with something that is massive.',
'Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. And the only way to do great work is to love what you do. If you haven’t found it yet, keep looking. Don’t settle. As with all matters of the heart, you’ll know when you find it.',
' Two roads diverged in a wood, and I took the one less traveled by, And that has made all the difference.',
'We become what we think about.','The most common way people give up their power is by thinking they don’t have any.',
'If you want to find the secrets of the universe, think in terms of energy, frequency and vibration.','Of all things, I liked books best.',
'I dont care that they stole my idea . . I care that they dont have any of their own','Be alone, that is the secret of invention; be alone, that is when ideas are born.',
'The present is theirs; the future, for which I really worked, is mine.','I shouldn’t be alive, unless it was for a reason. I’m not crazy. I just finally know what I have to do. And I know in my heart that it’s right.'

]	
	#for i in range(int(cmd[2])):
	g = random.randint(0,int(len(motivational_quotes))-1)
	print_and_say(motivational_quotes[g])

if os.name == 'nt':
	os.system('color 0a')
	os.system('cls')
else:
	pass

greeting = pyfiglet.figlet_format("WELCOME BOSS !")
print(greeting)


#say('initialising sequence..')
#say('importing prefences from the home interface.')
print()
print('ASSISTANT NAME : FRIDAY-FEMALE REPLACEMENT INTELLIGENT DIGITAL ASSISTANT YOUTH')
print("SYSTEM : ",platform.system() + ' ' + platform.release())

# motivational_quotes = ["Don’t say you don’t have enough time. You have exactly the same number of hours per day that were given to Helen Keller, Pasteur, Michelangelo, Mother Teresa, Leonardo Da Vinci, Thomas Jefferson, and Albert Einstein.",
# 'Hard work beats talent when talent doesn’t work hard.','If everything seems to be under control, you’re not going fast enough.',
# "don't ever stop doing your best just because someone doesn’t give you credit.",'If you work on something a little bit every day, you end up with something that is massive.',
# 'Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. And the only way to do great work is to love what you do. If you haven’t found it yet, keep looking. Don’t settle. As with all matters of the heart, you’ll know when you find it.',
# ' Two roads diverged in a wood, and I—I took the one less traveled by, And that has made all the difference.',
# 'We become what we think about.','The most common way people give up their power is by thinking they don’t have any.'
# ]
chat = {'hi ':'hello','who is jarvis ':'JARVIS stands for JUST A RATHER VERY INTELLIGENT SYSTEM.',
'boom ':'superboom','who is ironman ':'He is just a man in can. well by the way sir, you are the real IRONMAN and i am your JARVIS.',
'who ? ':'I am JARVIS. your virtual ASSISTANT.','why ':'what why? ask complete questions.. ','wtf ':'what the FUCK.',
'how ': 'what how? ask complete questions..','okay ':'all right !','oky ':'alright !','kk ':'alright !','when ':'what ? ask complete questions.',
'bye ': 'have a good day sir .','shutdown ': 'shutting down the system...','love u ':'love you too sir.', 
'what ': 'what what ? ', 'who ': 'what who?  ask complete questions.','haha':'why are you laughing sir ?',
'who are you ? ':'I am JARVIS. your virtual ASSISTANT.','good morning':'good morning sir !'
}

while True:
	x = input("YOU :")
	if x in chat.keys():
		print_and_say(chat[x])
	else:
		cmd = x.split()
		import webbrowser as wb

		if 'wiki' in x:
			topic = x.replace('wiki', '')
			import wikipedia
			print_and_say(wikipedia.summary(topic,sentences=2))

	
		elif 'help' in x :
			for i in chat:
				print(i + ": " + chat[i])
				total_commands = len(chat.keys())
			#print_and_say('total number of commands is '+ str(total_commands) + '.')
		elif 'typing_speed' in x:
			wb.open('https://10fastfingers.com/typing-test/english')
			print_and_say('Here you go sir !')
		
		# elif "random_song " in x:
		# 	import random
		# 	import playsound
		# 	songs_list = os.listdir(music_dir_loc)
		# 	j = len(songs_list)
		# 	r = random.randint(0,j)
		# 	print_and_say("plyaing some random song..")
		# 	print("Song Name: ",songs_list[int(r)])
		# 	playsound.playsound(music_dir_loc + "\\" + songs_list[int(r)])

		elif 'cmd' in x:
			command = x.replace('cmd', '')
			open_new_shell(command)

		elif 'sys' in x :
			sys_command = x.replace('sys', '')
			os.system(sys_command)
		# elif cmd[0].lower() =="quotes":
		# 	import random
		# 	g = random.randint(0,len(motivational_quotes))
		# 	print(motivational_quotes[g])
		
		elif 'quote' in x:
			motivation()

		elif x == 'bye bye ' or x == 'exit ':
			print_and_say('exiting jarvis-shell-mode..')
			break
		elif 'play' in x:
			song = x.replace('play', '')
			print_and_say('Playing ' + 'song '+song.upper() + '!')
			pywhatkit.playonyt(song)
		elif 'info' in x:
			topic = x.replace('info', '')
			#print('title= ',topic)
			print_and_say(pywhatkit.info(topic,lines=1))
		
			

		elif 'flood' in x :
			m =  x.replace('flood', '')
			#print('m = ',m)
			c = m.split(' ')
			#print('c = ',c)

			app = c[1]
			n = c[2]
			for i in range(int(n)):
				os.system('%windir%\\system32\\notepad.exe')


		elif 'open' in x :
			programs = x.replace('open', '')
			p_l = programs.split(' ')
			if 'firefox' in p_l:
				os.system('"C:\\Program Files\\Mozilla Firefox\\firefox.exe"')
			if 'sublime' in p_l:
				os.system("C:\\Program Files\\Sublime Text 3\\sublime_text.exe")
			if 'notepad' in p_l:
				os.system('%windir%\\system32\\notepad.exe')
			if 'vlc' in p_l:
				os.system('"C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"')
			if 'youtube' in p_l:
				wb.open('https://www.youtube.com/')
			if 'quora' in p_l:
				wb.open('https://www.quora.com/')
			if 'keybr' in p_l:
				wb.open('https://www.keybr.com/')
			if 'whatsapp' in p_l:
				wb.open('web.whatsapp.com')
			if 'google' in p_l:
				wb.open('www.google.com')


			if 'code' in p_l:
				os.system('"C:\\Users\\RS21\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"')
		elif 'joke' in x :
			import pyjokes
			joke = pyjokes.get_joke()
			print_and_say(joke)

		elif 'time' in x:
			time = datetime.datetime.now().strftime('%I:%M %p')
			print_and_say('current time is ' + str(time))
		elif 'music' in x:
			import playsound
			os.chdir(music_dir_loc)
			songs_list = os.listdir(music_dir_loc)
			for i in range(len(songs_list)):
				print(str(i) + ' ' + songs_list[i])
			y = input(': ')
			print_and_say("playing  " + str(songs_list[int(y)]))
			print_and_say("opening new shell while you are listening to music..")
			open_new_shell()
			playsound.playsound(music_dir_loc + '\\' + songs_list[int(y)])
		elif 'video' in x :
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
			say("what should it say: ")
			msg= input("what should it say? \n " + ': ')
			send_mail(send_to=mail_to,text=msg)

		else:
			print_and_say('unable to process the query.')


