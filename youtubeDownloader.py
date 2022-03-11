# import enum
# from pytube import YouTube

# link="https://youtu.be/PlsQisQhumY"
# youtube_1=YouTube(link)

# #print(youtube_1.title)
# #print(youtube_1.thumbnail_url)

# videos = youtube_1.streams.all() # all format
# #videos = youtube_1.streams.filter(only_audio=True) # all format

# vid=list(enumerate(videos))
# for i in vid:
#     print(i)

# strm=int(input("Enter : "))
# videos[strm].download()
# print("Successfully")

#playlist Download

from pytube import Playlist

py==Playlist("Playlist URL")

print(f'Downloading :{py.title}')

for video in py.videos:
    video.streams.first().download()



