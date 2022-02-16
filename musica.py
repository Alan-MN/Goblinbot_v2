import youtube_dl 

class Musica:
    def __init__(self,link):
        self.link = link
        with youtube_dl.YoutubeDL() as ydl:
            info = ydl.extract_info(self.link,download = False)
            self.nome = info['title']
            self.True_url = info['formats'][0]['url']