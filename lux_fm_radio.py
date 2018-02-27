import requests
from bs4 import BeautifulSoup

class RadioLuxFM:

    def __init__(self, url):
        self.url = url

    def show_info_about_song(self):
        try:
            r = requests.get(self.url)
            soup = BeautifulSoup(r.text, 'html.parser')
            song_name = soup.find(attrs={'id': 'song-name'}).string.strip()
            song_performer1 = soup.find(attrs={'id': 'song-name'}).find_parent()
            soup1 = BeautifulSoup(song_performer1.text, 'html.parser')
            text1 = str(soup1)
            text2 = text1.splitlines()
            song_performer = text2[3].strip()

            print("__________________________________________________________")
            print("      Now you listen to Lux FM:")
            print("Song: " + song_name + '\nPerformer: ' + song_performer )
            print("__________________________________________________________")
        except:
            print("Internet isn't available. Please, verify your connection")
            print("__________________________________________________________" + '\n')