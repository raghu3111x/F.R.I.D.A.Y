import os 
import shutil
import getpass

uname = getpass.getuser()
main_directory = "c:\\Users\\" + uname + "\\"
desktop_dir =  "c:\\Users\\" + uname + "\\Desktop"
python_directory = "c:\\Users\\" + uname + "\\Desktop\\Python@Projects"
music_directory = "c:\\Users\\" + uname + "\\Music\\"
picturs_directory = "c:\\Users\\" + uname + "\\Pictures"
text_file_directory = "c:\\Users\\" + uname + "\\Desktop\\text_files"
video_directory = "c:\\Users\\" + uname + "\\Videos"
document_directory = "c:\\Users\\" + uname + "\\Documents"
executables_directory =  "c:\\Users\\" + uname + "\\Desktop\\executables"
iso_files_directory = "c:\\Users\\" + uname + "\\Desktop\\iso_files"
zip_file_directory = "c:\\Users\\" + uname + "\\Desktop\\zip_files"
python_module_directory = python_directory + "\\python_modules"

all_directories = [python_directory,music_directory,picturs_directory,text_file_directory,
video_directory,document_directory,executables_directory,iso_files_directory,zip_file_directory,python_module_directory]

for path in all_directories:
	if os.path.isdir(path) == 0:
		print('Creating directory : ',path.split('\\')[-1])
		os.makedirs(path)


dir = input("Enter the directory name: " + '\n' + ': ')
directory = main_directory + dir

os.chdir(directory)
print()
print("Current_Working_directory",os.getcwd())
#print(os.listdir(directory))
print()
print("moving files wait a sec...")
print()
folders_list = list()
for folders in os.listdir(directory):
	if os.path.isdir(folders):
		folders_list.append(folders)


def operation():
	for file in os.listdir(os.getcwd()):
		if file in folders_list:
			pass
		elif file.endswith('.py') or file.endswith('.pyw'):
			print("moving file ", file)
			os.system('move ' + '"' +file + '"' +' ' + python_directory)
		elif file.endswith('.mp3') or file.endswith('.wma') or file.endswith('.ogg') or file.endswith('.MP3'):
			print("moving file ",file)
			os.system('move ' + '"' + file + '"' +' ' + music_directory)
			#print('move ' + os.getcwd() + "\\" + '"' + file + '"' +' ' + music_directory)
		elif file.endswith('.txt'):
			print("moving file ",file)
			os.system('move ' + '"'+ file + '"'+' ' + text_file_directory)
			#print('move ' + main_directory + "\\" + file + ' ' + text_file_directory)
		elif file.endswith('.jpg') or file.endswith('.png') or file.endswith('.PNG') or file.endswith('.jpeg'):
			print("moving file ",file)
			os.system('move ' +  '"' +file + '"' + " " + picturs_directory)
		elif file.endswith('.mp4') or file.endswith('.mov') or file.endswith('.mkv'):
			print("moving file ",file)
			os.system('move ' + '"' +file + '"' +" " + video_directory)
		elif file.endswith('.pdf'):
			print("moving file ",file)
			os.system('move ' + '"' + file + '"' + " " + document_directory)
		elif file.endswith('.exe') or file.endswith('.msi') or file.endswith('.jar'):
			print('moving file ',file)
			os.system('move ' + '"' +file + '"' + " " +  executables_directory)
		elif file.endswith('.iso'):
			print('moving file ',file)
			os.system('move ' + '"' +file+ '"' + " " + iso_files_directory)
		elif file.endswith('.zip') or file.endswith('.gz'):
			print("moving file ",file)
			os.system('move ' + '"' +file + '"' + " " + zip_file_directory)
		elif file.endswith('.whl'):
			print("moving file ",file)
			os.system('move ' + '"' +file + '"' + " " + python_module_directory)
		elif file.endswith('.docx') or file.endswith('.odp'):
			print("moving file ",file)
			os.system('move ' + '"' +file + '"' + " " + document_directory)
		else:
			pass


# if want to operate inside the directory of a directory 
# for folder in folders_list:
# 	os.chdir(path=main_directory + '\\' + folder)
# 	operation()
# 	os.chdir(path=main_directory)
operation()

print("operation completed successfully..")
print("files positions have been changed accordingly..")
print()
#print(os.listdir(directory))
# print()
# print("list of all the folders is: ")
# print(folders_list)