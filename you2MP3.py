from __future__ import unicode_literals
import youtube_dl
import multiprocessing
from multiprocessing import Process, freeze_support
import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

f = open("C:/Users/Erdi/Desktop/Projects/python/testProjects/songList.txt", "r")
arry = []
counter = 0
SAVE_PATH = '/Downloads/'
def convert(counter):
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
    #counter+=1
for x in f:
    arry.append(x.split())
# for x in f:
#     arry.append(x.split())

#     ydl_opts = {
#         'format':'bestaudio/best',
#         'extractaudio':True,
#         'audioformat':'mp3',
#         'outtmpl':SAVE_PATH + arry[counter][1] +'.%(ext)s',
#         'noplaylist':True,
#         'nocheckcertificate':True,
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '192',
#         }],
#     }
#     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([arry[counter][0]])
#     counter+=1
#convert(0)
processes = []
for i in range(len(arry)):#support for parallel programming 
    if __name__ == '__main__':
        freeze_support()
        p = multiprocessing.Process(target=convert, args=[i])
        p.start()
        processes.append(p)
    #counter+=1
for process in processes:
    process.join()

f.close()