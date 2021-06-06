import wget
import pyperclip
import requests
import pyttsx3
#from tqdm import tqdm

engine = pyttsx3.init()
def print_and_say(x):
	print(x)
	engine.say(x)
	engine.runAndWait()

#url = pyperclip.paste()
urls_l = ['https://fsa.zobj.net/download/bCkEg_uRwftKc1xFF8dk3GJbM5kGOII2_toGguvyOuiXjHRU1ZJKhIcjSykojzjWKoLJrgisCmsVRgrVP3C4JE2GJNJncoh9VRbwcpWTJMj97DmevrPK-RsN_9Zw/?a=web&c=72&f=jarvis_on.mp3&special=1622207823-Y%2FRcPwUEwLHIObiJhIgtUlt7Ej5lCQNI36ERYnxj6i8%3D','https://fsa.zobj.net/download/bLT60hCnMyw56lCBuLAJR4sQsCX6bZN3nm8ztvoTcv9IN124B0A1SIvUz4eOCvmj7ZIqWvn-yzRjwRyPwgFPQWetk29ICwss9oZ-Cc9Lk5T9xRG4JSQDGBT1q0wE/?a=web&c=72&f=jarvis_access.mp3&special=1622208022-8iRXWI25mYoKsKge0M8%2FlH%2FmrYtpLk9IurfCq96Tb74%3D','https://fsa.zobj.net/download/bqXruBbUezqmQvHTfwxq3RQdHdF0HMCMs5VdmbIyCsHM1n-NQaflJfju0cliUcZtNi-jlUl5sdvPHfiP60oCN6ghz595PWCYOpCN8ygC8LE-Zn7RPGMu_QUWQNwE/?a=web&c=72&f=jarvis_message_sent.mp3&special=1622208464-ikNzqkd1tjzPrDC6VfkDmMIa%2FTytY%2FVyWfZXI%2F7XsRI%3D']
file_names_l = ['jarvis_on.mp3','jarvis_access.mp3','jarvis_message_sent.mp3']
for i in range(len(urls_l)):
	save_as = file_names_l[i]
	url = urls_l[i]
	r = requests.get(url,stream=True)
	total_size_in_bytes = int(r.headers.get('content-length',0))
	block_size = 1024
	#progress_bar = tqdm(total=total_size_in_bytes,unit='iB',unit_scale=True)
	print('File Size: ',total_size_in_bytes)
	print_and_say('Download Started !')
	with open(save_as,'wb') as file:
		for chunk in r.iter_content(block_size):
			#progress_bar.update(len(chunk))
			file.write(chunk)
	print_and_say('saved ' + save_as)

print('Done !')
