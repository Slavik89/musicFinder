import requests
from bs4 import BeautifulSoup

class RadioBBC:

    def __init__(self, url):
        self.url = url



    def show_info_about_song(self):
        try:
            r = requests.get(self.url)
            soup = BeautifulSoup(r.text, 'html.parser')

            song_name = soup.find(attrs={'class': 'track', 'itemprop': 'name'}).string

            song_performer1 = soup.find(attrs={'class': 'artist', 'itemprop': 'byArtist'}).string
            text1 = str(song_performer1)
            text2 = text1.splitlines()
            song_performer = text2[4].strip()

            print("__________________________________________________________")
            print("      Now you listen to Capital FM:")
            print("Song: " + song_name + '\nPerformer: ' + song_performer )
            print("__________________________________________________________")
        except:
            print("Internet isn't available. Please, verify your connection")
            print("__________________________________________________________" + '\n')
