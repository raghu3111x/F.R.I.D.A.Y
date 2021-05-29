import os 
modules = 'pyautogui numpy pandas OS-Platform pyfiglet pyttsx3 pywhatkit selenium'
print("Python Modules to be installed: ")
list = modules.split()
print(list)
for i in range(0,len(list)):
	print(str(i+1) + '. ' + list[i])

print()
os.system('pip install ' + modules)
os.system('pip install automateboringstuff')
print('\n'+'DONE installing pkgs...')
