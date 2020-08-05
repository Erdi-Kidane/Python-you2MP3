from __future__ import unicode_literals
import youtube_dl

f = open("songList.txt", "r")
arry = []
counter = 0
SAVE_PATH = '/Downloads/'
for x in f:
    arry.append(x.split())

    ydl_opts = {
        'format':'bestaudio/best',
        'extractaudio':True,
        'audioformat':'mp3',
        'outtmpl':SAVE_PATH + arry[counter][1] +'.%(ext)s',
        'noplaylist':True,
        'nocheckcertificate':True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([arry[counter][0]])
    counter+=1


f.close()