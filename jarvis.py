import speech_recognition as sr
import pyttsx3
import threading
import platform
import pyfiglet
import os
import random
import datetime
import playsound
import pywhatkit
import pyautogui as pt
import time 
import webbrowser as wb
import getpass
import sys

engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

uname = getpass.getuser()


chat = {'who is jarvis ':'JARVIS stands for JUST A RATHER VERY INTELLIGENT SYSTEM.',
'boom ':'superboom !','who is ironman ':'He is just a man in can. well by the way sir, you are the real IRONMAN and i am your JARVIS.',
'who ? ':'I am JARVIS. your virtual ASSISTANT.','why ':'what why? ask complete questions.. ','wtf ':'what the FUCK.',
'how ': 'what how? ask complete questions..','okay ':'all right !','oky ':'okay !','kk ':'okay !','when ':'what ? ask complete questions.',
'shutdown ': 'shutting down the system...','love u ':'love you too sir.', 
'what ': 'what what ? ', 'who ': 'what who?  ask complete questions.','haha ':'why are you laughing sir ?',
'who are you ? ':'I am JARVIS. your virtual ASSISTANT.','good morning':'good morning sir !','hello ':'hello sir ! '
}

user_input = ['hi ','hello ']
greeting_close = ['bye ','nice talking to you ','have a good day ' , 'we will meet soon ','get lost ','bye bye ']
say_intro_line = ['who are you ','who ','who ? ' ,'what is your name ? ','your name ? ']

def only_log(var):
	# log_file = open('C:\\Users\\' + uname + '\\Desktop\\Python@Projects\\log.txt','a')
	# log_file.write(var + '\n')
	# log_file.close()
	import csv
	log_file = open('log.csv','a',newline='')
	writer = csv.writer(log_file)
	writer.writerow([var])
	log_file.close()

def speak(t):
	engine.say(t)
	engine.runAndWait()

def log(var):
	print_and_say(var)
	import csv
	# log_file = open('C:\\Users\\' + uname + '\\Desktop\\Python@Projects\\log.txt','a')
	# log_file.write(var + '\n')
	# log_file.close()
	log_file = open('log.csv','w',newline='')
	writer = csv.writer(log_file)
	writer.writerow([var])
	log_file.close()

def soup_obj():
	import requests 
	from bs4 import BeautifulSoup
	import random 
	global html_text,soup,url
	html_text = requests.get(url).text
	soup = BeautifulSoup(html_text,features='html.parser')

def send_mail(send_to,text):
	import smtplib
	username=input('Enter the Username: ')
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
		print_and_say('Playing ' + str(songs_list[int(song_index)]))
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
		t1 = threading.Thread(target=notify,args=('Playing ' + str(songs_list[int(song_index)]),))
		t2 = threading.Thread(target=only_play_song)
		t1.start()
		t2.start()

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
def get_quote():
	global url
	url = 'https://parade.com/937586/parade/life-quotes/'
	soup_obj()
	quotes = soup.find_all('p')
	print_and_say(str(quotes[random.randint(0,int(len(quotes)) - 1)]).split('"')[1])

def random_music():
	music_dir_loc = 'C:\\Users\\' + uname + '\\Music\\'
	random_music = random.choice(os.listdir(music_dir_loc))
	os.startfile(os.path.join(music_dir_loc,random_music))

def open_new_shell(x):
	os.system('start cmd')
	import pyautogui as pt
	pt.typewrite(x)
	pt.typewrite(['enter'])

def get_word_meaning(word):
	from bs4 import BeautifulSoup
	import requests

	url = 'https://www.dictionary.com/browse/' + word
	speak(random.choice(['Searching on Internet ... !','Searching ... !','Processing ... !','Checking ... !']))
	html_text = requests.get(url).text
	soup = BeautifulSoup(html_text,features='html.parser')
	try:
		means = soup.find('span',class_='one-click-content css-nnyc96 e1q3nk1v1').text
		log(means.text)
	except :
		speak("No meaning found  ... !")
		speak("searching on Internet ...")
		wb.open('https://www.google.com/search?client=firefox-b-d&q=' + word + ' meaning')

def usd_to_inr():
	from bs4 import BeautifulSoup
	import requests
	import re

	amount = re.find(r'(\d)+',x)
	url = 'https://www.xe.com/currencyconverter/convert/?Amount='+ amount + '&From=USD&To=INR'
	html_text = requests.get(url).text
	soup = BeautifulSoup(html_text,'lxml')
	value = soup.find('p',class_='result__BigRate-sc-1bsijpp-1 iGrAod').text
	print_and_say(value)


def cheat():
	import time
	import pyautogui as pt
	pt.hotkey('win','r')
	pt.typewrite('cmd')
	pt.typewrite(['enter'])
	time.sleep(1)
	pt.typewrite('cd Desktop\\Python@Projects')
	pt.typewrite(['enter'])
	time.sleep(1)
	pt.typewrite('python cheat.py')
	pt.typewrite(['enter'])

def check_os():
	if os.name == 'nt':
		os.system('cls')
	else:
		pass

def notify(x):
	from win10toast import ToastNotifier
	n = ToastNotifier()
	n.show_toast('J.A.R.V.I.S',x,duration=2)

def cur_time():
	cur_time = datetime.datetime.now().strftime('%I:%M %p')
	log(cur_time)

def cur_date():
	cur_date = datetime.datetime.now().strftime('%d ' '%b ' '%Y')
	log(cur_date)

def get_ip():
	from bs4 import BeautifulSoup
	import requests
	url = 'https://kinsta.com/tools/what-is-my-ip/'
	html_text = requests.get(url).text
	soup = BeautifulSoup(html_text , features='html.parser')
	print_and_say('ACCESSING THE DATABASE ....!')
	IP = soup.find('div',class_='ip-address heading--large').span.text
	print_and_say(IP + ' is the current IP sir ..')
	print()
def change_color():
	bg = [0,1,2,3,4,5,6,7]
	fg = [8,9,'a','b','c','d','e','f']
	os.system('color ' + str(random.choice(bg)) + str(random.choice(fg)))

def remember_list():
	mem_file = open(os.getcwd() + '\\'+'remember.txt','r')
	mem_lines = mem_file.readlines().replace('remember that','')
	speak("Sir, may i remind you ")
	log(mem_lines[0])



def print_and_say(x):
	print(x)
	speak(x)

r= sr.Recognizer()
while True:

    with sr.Microphone() as source2:
        playsound.playsound('beep.wav')
        r.adjust_for_ambient_noise(source2,duration=0.2)
        audio = r.listen(source2)
        x=r.recognize_google(audio).lower()
        print("YOU: " + x)
        only_log(var='YOU : ' + x )

        if x=='bnd hoja ':
            print_and_say(random.choice(greeting_close) + 'sir ...!')
            os.system('cls')
            sys.exit()

        if x.split()[0].lower() == 'q':
            wb.open('https://www.quora.com/search?q=' + x.replace('q ',''))

        if x in chat.keys():
            log(chat[x]  + '\n')

        elif x in greeting_close:
            print_and_say(random.choice(greeting_close) + 'sir ...!')
            os.system('cls')
            sys.exit()

        else:
            cmd = x.split('&&')
            for i in range(len(cmd)):
                x = cmd[i]
                import webbrowser as wb

                if 'wiki' in x:
                    topic = x.replace('wiki', '')
                    import wikipedia
                    print_and_say(wikipedia.summary(topic,sentences=2))
                    log(wikipedia.summary(topic,sentences=2) + '\n')

                elif 'help' in x :
                    for i in chat:
                        print(i + ": " + chat[i])
                        total_commands = len(chat.keys())
                    #log('total number of commands is '+ str(total_commands) + '.')
                elif 'change color' in x :
                    change_color()
                elif 'play' and  'random music' in x :
                    random_music()
                elif 'cat' in x :
                    file_name =  x.replace('cat ', '')
                    try:
                        open_file = open(os.getcwd() + '\\' + file_name,'r')
                        text = open_file.readlines()
                        for i in range(len(text)):
                            print(text[i].replace('\\n','\n'))
                        only_log('< Displays text inside ' + file_name + '>')					

                    except Exception as e :
                        print(str(e) + '\n')
                        only_log(str(e) + '\n' )

                elif 'typing_speed' in x:
                    wb.open('https://10fastfingers.com/typing-test/english')
                    log('Here you go sir !' + '\n')

                elif 'exam' and 'not prepared' in x:
                    log('Dont worry sir ! I am always there to help you. Just type < exam started > and I will do my best to serve you . :)')
                    print()

                elif 'meaning' in x :
                    word = x.replace(' meaning','') 
                    get_word_meaning(word)
                    print()
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

                elif 'joke' in x :
                    url = 'https://short-funny.com/'
                    soup_obj()
                    jokes = soup.find_all('li')
                    log(jokes[random.randint(0,99)].text.split('***')[0].replace('\n','').replace('\n\n',''))
                    print()

                elif 'weather' and 'update' in x :
                    url = 'https://www.weatheronline.in/weather/maps/city?LANG=in&CEL=C&SI=kph&MAPS=over&CONT=inin&LAND=II&REGION=0024&WMO=42103&UP=0&R=0&LEVEL=140&NOREGION=1'
                    soup_obj()
                    temp = soup.find('tbody')
                    print_and_say('Checking weather...')
                    print_and_say('Done ...!')
                    print(temp.text.split('\n\n')[2])
                    print()
                    print(temp.text.split('\n\n')[3])
                    print()

                elif 'cmd' in x:
                    command = x.replace('cmd', '')
                    open_new_shell(command)

                elif x.lower() in user_input:
                    print(random.choice(user_input) + '! ')
                elif x.lower() in say_intro_line:
                    log('I am JARVIS. your virtual ASSISTANT.' + '\n')
                # elif x.lower() in greeting_close:
                # 	log(random.choice(greeting_close) + 'sir !' + '\n')
                # 	os.system('cls')
                #	break
                elif x =='reboot ':
                    log('Rebooting the Jarvis-Shell-Interface !')
                    os.system('cls && python bot.py')
                    break
                # elif cmd[0].lower() =="quotes":
                # 	import random
                # 	g = random.randint(0,len(motivational_quotes))
                # 	print(motivational_quotes[g])
                
                elif x=='crash':
                    for i in range(random.randint(100, 200)):
                        change_color()
                    os.system('color 0a')


                elif 'quote' in x:
                    try:
                        get_quote()
                        print()
                    except Exception as err:
                        print_and_say('Failure connecting to the quotes website !')
                        print('Error: ' + err)


                elif 'best of' in x:
                    artist = x.replace('best of ', '')
                    url = 'https://en.wikipedia.org/wiki/Special:Search?search=' + artist + '+all+songs+&go=Go&ns0=1'
                    soup_obj()
                    try:
                        songs = soup.find_all('div',class_='mw-search-result-heading')
                    except Exception as error:
                        print(error,end='\n\n')
                        print_and_say('Artist not found...')
                    if len(songs) is None:
                        print_and_say('No song Found ...!')
                    else:
                        song = songs[random.randint(0,len(songs))].text.split('(')[0]
                        print_and_say(random.choice(['Search complete...','Enjoy the music Sir ... !']) + ' Playing best of ' + artist+' ...!')
                        pywhatkit.playonyt(song + ' by ' + artist )
                    print()

                elif 'playonyt' in x or 'play on youtube' in x :
                    song = x.replace('playonyt', '')
                    notify("playing " + song)
                    log('Playing ' +song.upper() + '!' + '\n')
                    pywhatkit.playonyt(song)

                elif x=='lock ':
                    import time
                    import pyautogui as pt
                    time.sleep(6)
                    pt.hotkey('winleft','l')

                elif 'jarvis' and 'remember ' in x:
                    memory = x.replace('jarvis','')
                    mem_file = open(os.getcwd() + '\\'+'remember.txt','a')
                    mem_file.write(' and ' + memory)
                    mem_file.close()
                    log('Message added to the remember list..')

                elif 'remember-list ' in x :
                    remember_list()
                elif 'download' in x :
                    try:
                        import wikipedia
                        topic = x.replace('download', '')
                        lines = input("Enter the number of lines : ")
                        info = wikipedia.summary(topic,sentences=int(lines)).replace('.','\n')
                        topic_file = open(os.getcwd() + '\\' + topic + '.txt','a',encoding='utf-8')
                        topic_file.write(info)
                        topic_file.close()
                        log('File saved as ' + topic + '.txt')
                    except Exception as error:
                        log('Download Incomplete !')
                        print(error)
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
                        os.startfile('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe')
                        
                    if 'sublime' in p_l:
                        log('opening Sublime !' + '\n')
                        os.startfile('C:\\Program Files\\Sublime Text\\sublime_text.exe')
                        
                    if 'keybr' in p_l:
                        log("Opening Keybr !")
                        wb.open('www.keybr.com')

                    if 'notepad' in p_l:
                        log('opening Notepad !' + '\n')
                        os.startfile('C:\\Windows\\system32\\notepad.exe')
                        
                    if 'vlc' in p_l:
                        log('opening VLC Media Player !' + '\n')
                        os.startfile('"C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"')
                        
                    if 'youtube' in p_l:
                        log('opening Youtube !' + '\n')
                        wb.open('www.youtube.com')

                    elif 'task manager' in x:
                        log("Opening Task-Manager !")
                        os.startfile('C:\\Windows\\system32\\Taskmgr.exe')

                    if 'whatsapp' in p_l: 
                        log('opening Whatsapp !' + '\n')
                        wb.open('https://web.whatsapp.com/')
                        
                    if 'google' in p_l:
                        log('opening Google !' + '\n')
                        wb.open('www.google.com')

                    if 'cmd' in p_l:
                        open_new_shell(x)
                    if 'impress' in p_l:
                        log('Opening Microsoft Impress !')
                        os.startfile(r'C:\Program Files\LibreOffice\program\simpress.exe')

                    if 'wordpad' in p_l:
                        log('Opening Microsoft Wordpad')
                        os.startfile('C:\\Program Files\\Windows NT\\Accessories\\wordpad.exe')

                    if 'sticky notes' in p_l:
                        log('Opening sticky notes !')
                        os.system('C:\\Windows\\system32\\StikyNot.exe')

                    if 'quora' in p_l:
                        wb.open('quora.com')


                    if 'code' in p_l:
                        log('opening visual studio code !')
                        os.startfile('C:\\Users\\dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')

                elif 'sys' in x :
                    cmd_query = x.replace('sys ','')
                    os.system(cmd_query)

                elif 'my' and 'ip' in x:
                    get_ip()
                elif 'time' in x:
                    # time = datetime.datetime.now().strftime('%I:%M %p')
                    # log('current time is ' + str(time) + '\n')
                    from bs4 import BeautifulSoup
                    import requests
                    url = 'https://24timezones.com/India/time#gref'
                    html_text = requests.get(url).text
                    soup = BeautifulSoup(html_text,'lxml')
                    time = soup.find('span',id='currentTime')
                    print_and_say(time.text)
                    print()

                elif 'shutdown -h now ' in x :
                    print_and_say('Shutting down the system ...!')
                    os.system('shutdown -s -t 0')
                    

                elif 'play music' in x:
                    music_dir_loc = 'C:\\Users\\' + uname + '\\Music\\'
                    os.chdir(music_dir_loc)
                    songs_list = os.listdir(music_dir_loc)
                    while True:
                        play_song()
                        if other_song =='y':
                            play_song()
                        else:
                            break

                elif 'play' and 'video' in x :
                    video_dir_loc = 'c:\\Users\\' + uname + '\\Videos'
                    videos_list = os.listdir(video_dir_loc)
                    if len(videos_list) ==0:
                        log('Sorry sir, Videos folder have no files....')
                    for i in range(len(videos_list)):
                        print(str(i) + ' ' + videos_list[i])
                    y = input(': ')
                    video_file = 'c:\\users\\' + uname + '\\Videos' + '\\'+videos_list[int(y)]
                    os.startfile(os.path.join(video_dir_loc,video_file))
                    notify("Playing " + video_file + ' ! ') 
                    print()
                    
                elif "play" in x:
                    x=x.replace("play ","").replace("song ","").replace("video ","")
                    pywhatkit.playonyt(x)

                elif 'google' in x :
                    query = x.replace('google ')
                    wb.open('https://www.google.com/search?client=firefox-b-d&q=' + query)
                elif 'wtsp' in x:
                    import time
                    import webbrowser as wb
                    name = x.replace('wtsp ','')
                    log('What should it say ?')
                    msg = input(':')
                    wb.open('https://web.whatsapp.com/')
                    import pyautogui as pt
                    time.sleep(15)
                    pt.typewrite(['tab'])
                    time.sleep(2)
                    pt.typewrite(name)
                    time.sleep(2)
                    pt.typewrite(['enter'])
                    time.sleep(2)
                    pt.typewrite(msg)
                    time.sleep(2)
                    pt.typewrite(['enter'])
                    time.sleep(2)
                    notify('Message Sent ...!')
                    playsound.playsound('jarvis_message_sent.mp3')



                elif x=='exam started ':
                    cheat()
                elif 'random video' in x :
                    video_dir_loc = 'c:\\users\\' + uname +'\\Videos'
                    videos_list = os.listdir(video_dir_loc)
                    video_file = random.choice(videos_list)
                    notify('Playing video file ' + video_file + " !")
                    os.startfile(os.path.join(video_dir_loc,video_file))

                elif 'send mail' in x :
                    mail_to = x.replace('send mail to','')
                    speak("what should it say: ")
                    msg= input("what should it say? \n " + ': ')
                    send_mail(send_to=mail_to,text=msg)
                    notify('Email sent successfully ...!')

                elif 'mute' in x :
                    import pyautogui as pt
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
                        print('A: ',a)
                        print('B: ',b)
                        output = input('output: ')
                        if int(output) == a * b:
                            print_and_say('YOU WIN !' + '\n')
                        else:
                            while int(output) != a * b:
                                print_and_say(random.choice(['Try Again ¿','Nope ¿','Wrong ¿','Wrong Answer ¿']))
                                print('\n')
                                output = input('output: ')
                                if int(output) == a * b:
                                    print_and_say(random.choice(['YOU WIN !','Well Done !','Appreciating !','Fantastic !','Awesome !','Really good ! ']) + '\n')
                                else:
                                    continue


                    elif 'medium' in x :
                        a = random.randint(41,70)
                        b = random.randint(41,70)
                        print('A: ',a)
                        print('B: ',b)
                        output = input('output: ')
                        if int(output) == a * b:
                            print_and_say('YOU WIN !')
                        else:
                            while int(output) != a * b:
                                print_and_say('Try Again !')
                                print('\n')
                                output = input('output: ')
                                if int(output) == a * b:
                                    print_and_say('YOU WIN !' + '\n')
                    elif 'hard' in x :
                        a = random.randint(71,99)
                        b = random.randint(71,99)
                        print('A: ',a)
                        print('B: ',b)
                        output = input('output: ')
                        if int(output) == a * b:
                            print_and_say('YOU WIN !')
                        else:
                            while int(output) != a * b:
                                print_and_say('Try Again !')
                                print('\n')
                                output = input('output: ')
                                if int(output) == a * b:
                                    print_and_say('YOU WIN !' + '\n')
"""                 else:
                    only_log(os.popen(x).read())
                    print() """




