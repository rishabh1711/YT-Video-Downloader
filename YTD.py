from pytube import YouTube
from pytube import Playlist

n=int(input("Press 1 to Download Youtube Video or Press 2 for Download Playlist and any other to exit..."))
if n==1:
    link=input("Paste the YouTube video Link here: ")
    youtube_1=YouTube(link)
    print()
    print("Title of your YouTube Video is\n","=>",youtube_1.title)
    print()
    print("Video Thubnail Link is\n","=>",youtube_1.thumbnail_url)
    c=int(input("Press 1 to downlaod Video or Press 2 to download the audio and any other to exit..."))
    if c==1:
        videos=youtube_1.streams.filter(only_video=True)
        vid=list(enumerate(videos))
        for i in vid:
            print(i)
        print()
        strm=int(input("enter your Choice to start download: "))
        print("Please Wait... download is in process...")
        videos[strm].download() 
        print('Your video is Successfully downloaded')
        input()
        
    elif c==2:
        videos=youtube_1.streams.filter(only_audio=True)
        vid=list(enumerate(videos))
        for i in vid:
            print(i)
        print()
        strm=int(input("enter your Choice to start download: "))
        print("Please Wait... download is in process...")
        videos[strm].download() 
        print('Your audio is Successfully downloaded')
        input()
    else:
        print("Exiting.....")
        input()
elif n==2:
    link=input("Paste the YouTube video Link here: ")
    py=Playlist(link)
    print()
    print("Title of your YouTube Video is\n","=>",py.title)
    print("Your Playlist Download is in Process Please wait.....")
    for video in py.videos:
        video.streams.first().download()
    print("Playlist is downloaded Successfully.")
    input()
else:
    print("Exiting.....")
    input()