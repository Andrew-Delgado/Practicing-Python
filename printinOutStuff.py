from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import time
import json
import os

class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "\\" + filename
            new_destination = folder_destination + "\\" + filename
            os.rename(src, new_destination)


folder_to_track = 'C:\\Users\Andrew\\Desktop\\Desktop'
folder_destination = 'C:\\Users\\Andrew\\Desktop\\TestFolder'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()