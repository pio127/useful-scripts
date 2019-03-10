from pytube import YouTube, Playlist
import sys
import os.path
import glob

def getAllLinks(playList):
    allLinks = []
    youtubeLink = 'https://www.youtube.com'
    pl = Playlist(playList)
    for linkprefix in pl.parse_links():
        allLinks.append(youtubeLink + linkprefix)
    return allLinks

num_of_args = len(sys.argv)
arguments = sys.argv
if num_of_args > 1:
    links = getAllLinks(arguments[1])
    
    for link in links:
        yt = YouTube(link)
        yt.streams.filter(progressive=True, file_extension='mp4').first().download('yt')
        print('{} downloaded'.format(yt.title))
    else:
        print('Ending without action...')
else:
    print('No playlist provided...')