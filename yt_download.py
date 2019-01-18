from pytube import YouTube
import sys

num_of_args = len(sys.argv)
arguments = sys.argv


print(num_of_args)
print(arguments)
if num_of_args > 1:
    print(arguments[1])
    YouTube(arguments[1]).streams.filter(progressive=True, file_extension='mp4').first().download('yt')
    print('Video downloaded')
else:
    print('No argument provided')