import os
from pytubefix import YouTube

url = input('Enter URL: ')
filename = input('Enter filename: ')

yt = YouTube(url)
print(yt.streams.filter(only_audio=True))
sel = input('Select stream itag:')


stream = yt.streams.get_by_itag(int(sel))
stream.download(filename=filename+'.mp3')