import requests
from bs4 import BeautifulSoup

class RadioBBC:

    def __init__(self, url):
        self.url = url



    def show_info_about_song(self):
        try:
            song_name = ''
            song_performer = ''
            r = requests.get(self.url)
            soup = BeautifulSoup(r.text, 'html.parser')
            song_attrs = soup.find(attrs={'class': 'on-air__track-now-playing__playlister'}).attrs
            for phrase in song_attrs:
                if phrase == 'data-tracktitle':
                    song_name = song_attrs[phrase]
                if phrase == 'data-artistname':
                    song_performer = song_attrs[phrase]

            print("__________________________________________________________")
            print("      Now you listen to BBC Radio:")
            print("Song: " + song_name + '\nPerformer: ' + song_performer )
            print("__________________________________________________________")
        except:
            print("Internet isn't available. Please, verify your connection")
            print("__________________________________________________________" + '\n')
