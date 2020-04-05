""" main.py aka General File Sorter

This program sorts files from the downloads folder into other folders based on 
the file's type.

This project is dependent on a func.py file I created to find the correct
PATH that the file should go to.

A benifit of this implementation of sorting files is the minimal imports used.
The imports 'os' and 'time' already come with any python installation.

"""
__author__ = "Andrew Delgado"
__version__ = 1.0
__status__ = "Prototype"

import func
import os
import time

source = 'C:\\Users\\Andrew\\Desktop'
YELLOW = '\033[33m'
GREEN  = '\033[32m'
RED    = '\033[31m'
RESET  = '\033[0m'
CYAN   = '\033[36m'

if __name__ == "__main__":

    print(GREEN + "Running..." + RESET)
    try:
        while True:
            listOfFiles = os.listdir(source)

            if len(listOfFiles) > 0:
                if len(listOfFiles) == 1 and listOfFiles[0] == 'desktop.ini':
                    continue
                else:
                    print(f"\nOriginal number of files: {CYAN}{len(listOfFiles)}{CYAN}")
                    for file in listOfFiles:

                        # if file == 'desktop.ini':
                        #     continue

                        source = 'C:\\Users\\Andrew\\Desktop'
                        destination = func.getDestDir(file)

                        src = source + '\\' + file
                        dest = destination + '\\' + file

                        os.rename(src, dest)

                        print(f"{YELLOW}Moved file:{RESET} {file}")

                    print(f"\nNumber of files moved: {CYAN}{len(listOfFiles) - len(os.listdir(source))}{RESET}")
                    
            time.sleep(2)
    except KeyboardInterrupt:
        print(RED + "...Not Running" + RESET)
        SystemExit