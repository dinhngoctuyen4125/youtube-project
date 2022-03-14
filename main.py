from pytube import YouTube
import os

urls_inp = open('main.inp', 'r')
path = input('Enter path: ') or os.path.join(os.path.expanduser('~'), 'Downloads')

for url in urls_inp.readlines():
    try:
        my_video = YouTube(url)
        my_video.streams.get_highest_resolution().download(path)
        print(my_video.title, '- **download successfully!**')
    except:
        print('- Cannot find video!')