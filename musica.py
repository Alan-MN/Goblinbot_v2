import youtube_dl 
import os

class Musica:
    def __init__(self,link):
        self.link = link

    def pegaInfo(self):
        ydl_opts = {
        'format': '249/250/251',
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(self.link,download = False)
            self.nome = info['title']
            self.True_url = info['formats'][0]['url']