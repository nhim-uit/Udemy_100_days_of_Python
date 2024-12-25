import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()


def get_100_songs(date_):
    """
    Fetches the top 100 songs from the Billboard Hot 100 chart for a given date.

    :param date_: (str) the date in the format YYYY-MM-DD
    :return: list: a list of song titles.
    """
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) "
                            "Gecko/20100101 Firefox/131.0"}
    url = f'https://www.billboard.com/charts/hot-100/{date_}/'
    response = requests.get(url=url, headers=header)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    heading = soup.select('li ul li h3')

    titles = [head.getText().strip() for head in heading]
    # print(titles)

    return titles


def get_Spotify():
    """
    Authenticates and returns a Spotify client using Spotipy
    :return: spotipy.Spotify: an authenticated Spotify client.
    """
    scope = 'playlist-modify-private'

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        scope=scope,
        redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
        client_id=os.getenv('SPOTIPY_CLIENT_ID'),
        client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
        show_dialog=True,
        ))

    # user_id = sp.current_user()['id']
    # token_info = sp.auth_manager.get_access_token()
    # print(token_info)
    return sp


def create_playlist(sp, date, uris):
    """
    Create a new private playlist on Spotify and adds the given songs to it
    :param sp: (spotipy.Spotify) An authenticated Spotify client.
    :param date: (str) The date in the format YYYY-MM-DD
    :param uris: (list) A list of Spotify URIs for the songs to be added to the playlist.
    :return: void
    """
    USER_ID = sp.current_user()['id']
    playlist = sp.user_playlist_create(user=USER_ID, public=False, name=f"{date} BillBoard-100")
    sp.playlist_add_items(playlist_id=playlist["id"], items=uris)
