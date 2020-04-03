import os

source = 'C:\\Users\\Andrew\\Downloads'

listOfFiles = os.listdir(source)
print(f"Original number of files: {len(listOfFiles)}")

for file in listOfFiles:
    source = 'C:\\Users\\Andrew\\Downloads'
    destination = 'C:\\Users\\Andrew\\Documents\\UnsortedFiles\\UnsortedImages'

    if file.__contains__('.jpg'):
        src = source + '\\' + file
        destination = destination + '\\' + file

        os.rename(src, destination)

        print(f"Moved file: {file}")


print(f"\nNumber of files moved: {len(listOfFiles) - len(os.listdir(source))}")










# print(f"This is a list of: {os.listdir(source)}")

# fileText = listOfFiles[3]

# src = source + '\\' + fileText
# destination = destination + '\\' + fileText


# print(fileText)
# print(f"source file {src}")
# print(f"dest file {destination}")

# os.rename(src, destination)

# print(f"\nThis is a list of: {os.listdir(source)}")