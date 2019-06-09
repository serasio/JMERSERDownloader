
# coding: utf-8

# In[1]:


from __future__ import unicode_literals
import youtube_dl


# In[2]:


print("""
################################################
###      JMERSER YouTube MP3 Downloader      ###
###  Credits to Juan Manuel Merlini Serasio  ###
################################################
""")

opt = 0

while opt != 1 and opt != 2:
    print("""JMENU
    1 - Descargar vídeos (MP4).
    2 - Descargar audio (MP3).""")

    opt = int(input("Ingrese opcion: "))

if opt == 1:
    ydl_opts = {
            'videoformat' : "mp4",
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',}],
            'outtmpl': 'Videos/%(title)s.%(ext)s'
        }
elif opt == 2:
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

print("""
###########################################################################################################
#La conversión de formato puede tardar unos minutos, dependiendo del tamaño del archivo. Por favor espere.#
###########################################################################################################
        """)
        
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(links)

if opt == 1:
    print('\nLa/s descarga/s se realizó/aron en la carpeta "Videos".')
elif opt == 2:
    print('\nLa/s descarga/s se realizó/aron en la carpeta "Musica".')
    
input('\nPresiona Enter para terminar..')

