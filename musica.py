import youtube_dl 
import os

class Musica:
    def __init__(self,link):
        self.link = link

    def pegaInfo(self):
        with youtube_dl.YoutubeDL() as ydl:
            info = ydl.extract_info(self.link,download = False)
            self.nome = info['title']
            self.duracao = info['duration']

    def download(self):
        ydl_opts = {
        'format': '249/250/251',
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.link])
        for file in os.listdir('./'):
            if file.endswith('.webm'):
                os.rename(file, 'song.webm')
        
