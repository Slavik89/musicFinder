import requests
from bs4 import BeautifulSoup

class RadioMaximum:

    def __init__(self, url):
        self.url = url

    def show_info_about_song(self):
        try:
            r = requests.get(self.url)
            soup = BeautifulSoup(r.text, 'html.parser')
            song_name = soup.find('span', attrs={'class': 'name'}).string
            song_performer = soup.find('span', attrs={'class': 'author'}).string
            print("__________________________________________________________")
            print("      Now you listen to Maximum Radio:")
            print("Song: " + song_name + '\nPerformer: ' + song_performer )
            print("__________________________________________________________")
        except:
            print("Internet isn't available. Please, verify your connection")
            print("__________________________________________________________" + '\n')
