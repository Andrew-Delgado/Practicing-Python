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

source = 'C:\\Users\\Andrew\\Downloads'

if __name__ == "__main__":

    print("Running...")
    try:
        while True:
            listOfFiles = os.listdir(source)

            if len(listOfFiles) > 0:
                print(f"Original number of files: {len(listOfFiles)}")
                for file in listOfFiles:
                    source = 'C:\\Users\\Andrew\\Downloads'
                    destination = func.getDestDir(file)

                    src = source + '\\' + file
                    dest = destination + '\\' + file

                    os.rename(src, dest)

                    print(f"Moved file: {file}")

                print(f"\nNumber of files moved: {len(listOfFiles) - len(os.listdir(source))}")

            time.sleep(2)
    except KeyboardInterrupt:
        print("...Not Running")
        SystemExit