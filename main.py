import func
import os
import time
# C:\\Users\\Andrew\\Downloads
source = 'C:\\Users\\Andrew\\Desktop\\Desktop'

if __name__ == "__main__":

    try:
        while True:
            listOfFiles = os.listdir(source)

            if len(listOfFiles) > 0:
                print(f"Original number of files: {len(listOfFiles)}")
                for file in listOfFiles:
                    source = 'C:\\Users\\Andrew\\Desktop\\Desktop'
                    destination = func.getDestDir(file)

                    src = source + '\\' + file
                    dest = destination + '\\' + file

                    os.rename(src, dest)

                    print(f"Moved file: {file}")

                print(f"\nNumber of files moved: {len(listOfFiles) - len(os.listdir(source))}")

            time.sleep(2)
    except KeyboardInterrupt:
        print("Keyboard Interrupt exception caught")
        SystemExit