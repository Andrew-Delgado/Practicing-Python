"""
This file contains arrays that contain similar of file types. 
Each array is used to find the correct path of where files should go.

"""
__author__ = "Andrew Delgado"
__version__ = 1.0
__status__ = "Prototype"

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

