audioVideo = ['mp3','mp4']
code = ['txt','class']
image_files = ['jpeg','jpg','png','gif','tiff','ai','raw','svg']
installers = ['msi']
microsoft = ['doc','docx','dotx','xlsx','xlsm','xlm','ppt','pps','pptx','pptm','ppsx','sldx']
pdf = ['pdf']
software = ['exe']
zipped_folders = ['zip']

# Gets destination of folder that the file should go in.
def getDestDir(fileType):

    # Gets the extention of the file
    start = fileType.rfind('.') + 1
    end = len(fileType)
    extention = fileType[start:end]

    # Checks each array if it contains the file extention.
    if code.__contains__(extention):
        return 'C:\\Users\\Andrew\\Documents\\UnsortedFiles\\UnsortedCode'
    elif image_files.__contains__(extention):
        return 'C:\\Users\\Andrew\\Documents\\UnsortedFiles\\UnsortedImages'
    elif installers.__contains__(extention):
        return 'C:\\Users\\Andrew\\Documents\\UnsortedFiles\\UnsortedInstallers'
    elif microsoft.__contains__(extention):
        return 'C:\\Users\\Andrew\\Documents\\UnsortedFiles\\UnsortedMicrosoft'
    elif pdf.__contains__(extention):
        return 'C:\\Users\\Andrew\\Documents\\UnsortedFiles\\UnsortedPDF'
    elif software.__contains__(extention):
        return 'C:\\Users\\Andrew\\Documents\\UnsortedFiles\\UnsortedSoftware'
    elif zipped_folders.__contains__(extention):
        return 'C:\\Users\\Andrew\\Documents\\UnsortedFiles\\UnsortedZip'
    elif audioVideo.__contains__(extention):
        return 'C:\\Users\\Andrew\\Documents\\UnsortedFiles\\UnsortedAudioAndVideo'
    else:
        return 'C:\\Users\\Andrew\\Documents\\UnsortedFiles\\ZZZ-UnsortedOtherFiles'




# main I used to test this function
if __name__ == "__main__":
    destination = getDestDir('andrewdelgado017@gmail.com.ical')
    print(destination)

    # destination = getDestDir('asdfa.pptx')
    # print(destination)

