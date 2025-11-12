import os
from pytubefix import YouTube
import pytubefix.request

# Change the value here to something smaller to decrease chunk sizes,
#  thus increasing the number of times that the progress callback occurs
# pytubefix.request.default_range_size = 9437184  # 9MB chunk size
# pytubefix.request.default_range_size = 1048576  # 1MB chunk size

def on_progress(stream, chunk, bytes_remaining):
    """Callback function"""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100
    # print(f"Status: {round(pct_completed, 2)} %")

url = input('Enter URL: ')
filename = input('Enter filename: ')

yt = YouTube(url, on_progress_callback=on_progress)

streams = yt.streams.filter(only_audio=True)

for stream in streams:
    print(stream)

sel = input('Select stream itag:')


stream = yt.streams.get_by_itag(int(sel))
stream.download(filename=filename+'.mp3')

print(f'Download complete: {filename}.mp3')
