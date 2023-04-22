import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
# to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"

from_dir = "C:/Users/Hamsini/Downloads"
to_dir = "C:/Users/Hamsini//Desktop/Downloaded_Files"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        name,extension = os.path.splitext(event.src_path)
        time.sleep(1)
        for key,value in dir_tree .items ():
            time.sleep(1)
            if extension in value : 
                file_name = os.path.basename (event.src_path)
                print("download " + file_name)
                path1 = from_dir + "/"+ file_name
                path2 = to_dir + "/"+ key 
                path3 = to_dir +"/"+ key + "/" + file_name
                time.sleep(1)
                if os.path.exists(path2):
                    print("folder exsits")
                    time.sleep(1)
                    if os.path.exists (path3):
                        print("file already exsits" + key)
                        print("renaming file" + file_name)
                        new_filename = os.path.splitext(file_name)[0]+ str ( random.randint(0,999))+os.path.splitext(file_name)[1]
                        path4=to_dir+"/"+ key + "/"+ new_filename
                        print("moving "+new_filename)
                        shutil.move(path1,path4)
                        time.sleep(1)
                    else :
                        print("moving "+ file_name)
                        shutil.move(path1,path3)
                        time.sleep(1)
                else:
                    print("creating a new folder")
                    os.makedirs(path2)       
                    print("moving "+file_name)
                    shutil.move(path1,path3)
                    time.sleep(1) 

        print(event)
        print(event.src_path)


# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

try :

    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt :
    print("stoped")        
    observer.stop()

    