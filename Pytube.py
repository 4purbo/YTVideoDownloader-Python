from pytube import *#getting access from the link

def Download(link):
    youtubeObject=YouTube(link)
    youtubeObject.streams.get_highest_resolution().download()
    print("Download completed successfully !")
    print("PLease check the folder where this Python file is located")


link=input("Enter your link : ")
Download(link)