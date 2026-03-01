import os
import shutil

os.chdir("/Users/Administrator/Desktop/")
current_path = (os.getcwd())
folders = "My_projects/Images/Videos/Docs/Music/Others"
files_folders = "My_projects"
images_folder = "Images"
videos_folder = "Videos"
docs_folder = "Docs"
music_folder = "Music"
others_folder = "Others"
path = "/Users/Administrator/Desktop/"
separated_files = []
all_files = ['ChatGPT.lnk', 'code.py', 'desktop.ini', 'Gmail.lnk', 'Javascript-projects', 'Microsoft Word.lnk', 'movie.mp4', 'My python projects', 'New folder', 'PC Health Check.lnk', 'PdaNetA5232b.exe', 'Personal - Edge.lnk', 'photo.jpg', 'song.mp3', 'test.pdf.txt', 'Visual Studio Code.lnk', 'VLC', 'vlc - Shortcut.lnk']

for file in all_files:
      root, extension = os.path.splitext(file)
      separated_files.append({"filename": root, "extension": extension}) #This code separtate the filename and extension of the files in the desktop.

for item in separated_files:
    print(f"filename:{item['filename']}, ext:{item['extension']}")    # This code list all the files and extensions on the desktop.

folder_input_2 = input(f"\nPress C to create these folders {folders}: ").lower()
if folder_input_2 == "c":
      os.makedirs(folders)
      print("\nCreated folder for user:")
      print(files_folders)
      print("\nFiles:")
      print(["photo.jpg","movie.mp4", "test.pdf.txt", "song.mp3", "code.py"]) # This code create the folders for the user asnd list the files the user has on the desktop they want to move into the folders.

      folder_input_2 = input("\nPress m to move files into their right folders: ").lower()
      if folder_input_2 == "m":
            shutil.copy("photo.jpg", "My_projects/Images/photo.jpg")
            print(f"Moved photo.jpg to",images_folder,"folder succesfully...")
            shutil.copy("movie.mp4", "My_projects/Images/Videos/movie.mp4")
            print(f"Moved movies.mp4 to",videos_folder,"folder succesfully...")
            shutil.copy("test.pdf.txt", "My_projects/Images/Videos/Docs/test.pdf.txt")  # This code moves the files into the folders created for the user.
            print(f"Moved test.pdf to",docs_folder,"folder succesfully...")
            shutil.copy("song.mp3", "My_projects/Images/Videos/Docs/Music/song.mp3")
            print(f"Moved song.mp3 to",music_folder,"folder succesfully...")
            shutil.copy("code.py", "My_projects/Images/Videos/Docs/Music/Others/code.py")
            print(f"Moved code.py to",others_folder,"folder succesfully...")
            quit()            





    

