from __future__ import unicode_literals
import youtube_dl

print("""
################################################
###      JMERSER YouTube MP3 Downloader      ###
###  Credits to Juan Manuel Merlini Serasio  ###
################################################
""")

ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',}],
        'outtmpl': 'Musica/%(title)s.%(ext)s'
    }

links = []
agrega = True

while agrega:
    links.append(input('Ingresa la url del video: '))
    if input('¿Agregar otra url? (s/n): ').lower() == 'n':
        agrega = False
        
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(links)

print('\nLa/s descarga/s se realizó/aron en la carpeta "Musica".')
input('\nPresiona Enter para terminar..')

