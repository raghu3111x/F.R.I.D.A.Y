import speech_recognition as sr
import os
import webbrowser as wb
import playsound

os.system('cls')
r = sr.Recognizer()

with sr.Microphone() as source:
	print('---------------------------------------------------------------------- SPEAK-UP -----------------------------------------------------------------------')
	playsound.playsound('beep.wav')	
	r.adjust_for_ambient_noise(source,duration=0.2)
	audio = r.listen(source)
	x = r.recognize_google(audio).lower()
	print('\nYOU: ' + x)

	if 'open' in x:
		x = x.replace('open','')
		p_l = x.split(' ')
		try:
			if 'firefox' in p_l:
				os.startfile('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe')
							
			if 'sublime' in p_l:
				os.startfile('C:\\Program Files\\Sublime Text\\sublime_text.exe')
				
			if 'keybr' in p_l:
				wb.open('www.keybr.com')

			if 'notepad' in p_l:
				os.startfile('C:\\Windows\\system32\\notepad.exe')
				
			if 'vlc' in p_l:
				os.startfile('"C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"')
				
			if 'youtube' in p_l:
				wb.open('www.youtube.com')

			if 'task manager' in p_l:
				os.startfile('C:\\Windows\\system32\\Taskmgr.exe')

			if 'whatsapp' in p_l: 
				wb.open('https://web.whatsapp.com/')
				
			if 'google' in p_l:
				wb.open('www.google.com')

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
				os.startfile('C:\\Users\\RS21\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')
		except FileNotFoundError as e:
			print('File not found: ' + e.split('\\')[-1])
			playsound.playsound('inverter.wav')
			