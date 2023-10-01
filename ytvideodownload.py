from pytube import YouTube,Playlist
link=input("Enter The Link: ")
yt=YouTube(link)
print(yt.title)
print("See the Thumbnail here "+yt.thumbnail_url)
print("Apply a for audio+video download or p for playlist download")
wyw=input("").lower()
if (wyw=="a"):
     videos=yt.streams.all()
     vid=list(enumerate(videos))
     for i in vid:
      print(i)
      print()
      strm=int(input("Enter the Number: "))
      videos[strm].download()
      print("Downloaded Succesfully")
elif(wyw=="p"):
    py=Playlist(link)
    print(f'Downloading: {py.title}')
    for video in py.videos:
        video.streams.first().download()
else:
    print("Enter correct format only")
    

