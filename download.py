import os
from pytube import YouTube

url = 'https://www.youtube.com/watch?v=x5oXSGhK7EY'
file_name = 'Test_File'

mp4 = file_name + '.mp4'

yt = YouTube(url)

print(yt.streams.filter(only_audio=True))

sel = input('Select stream itag:')

stream = yt.streams.get_by_itag(int(sel))
stream.download(filename=file_name)