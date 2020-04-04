image_files = ['jpeg','jpg','png','gif','tiff','ai','raw']
zipped_folders = ['.zip']
installers = ['msi']
software = ['exe']

# Finish this
microsoft = ['']

# Gets destination of folder that the file should go in.
def getDestDir(fileType):

    # Gets the extention of the file
    start = fileType.find('.') + 1
    end = len(fileType)
    extention = fileType[start:end]

    # Checks each array if it contains the file extention.
    if image_files.__contains__(extention):
        return '\\another\\destinaton\\.txt'
    elif zipped_folders.__contains__(extention):
        return '\\sorting\\stuff\\.exe'





if __name__ == "__main__":
    destination = getDestDir('sdaf.txt')
    print(destination)

    destination = getDestDir('asdfa.exe')
    print(destination)

