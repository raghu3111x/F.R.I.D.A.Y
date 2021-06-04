import os 
modules = 'pyautogui numpy pandas OS-Platform pyfiglet pyttsx3 pywhatkit selenium pyjokes playsound secure-smtplib wikipedia matplotlib pyPdf PyPDF2 docx'
print("Python Modules to be installed: ")
list = modules.split()
print(list)
for i in range(0,len(list)):
	print(str(i+1) + '. ' + list[i])

print()
os.system('color 0a')
os.system('pip install ' + modules)
print('\n'+'DONE installing pkgs...')
