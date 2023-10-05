import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

date = input("What year whould you like to travel to ? (YYYY-MM-DD)\n")
url = "https://www.billboard.com/charts/hot-100/"+date+"/"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

divs = soup.find_all(name="div", class_="o-chart-results-list-row-container")

songs = []
for div in divs:
    songs.append(div.h3.text.strip())

# SPOTIFY PART

SPOTIPY_CLIENT_ID = "7a0162e215964818b5c5765f816b7362"
SPOTIPY_CLIENT_SECRET = "3e2bfd2ccdad43fbadb977f4b3146e50"
SPOTIPY_REDIRECT_URI = "http://example.com"
SPOTIPY_SCOPE = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope=SPOTIPY_SCOPE,
        show_dialog=True,
        cache_path="token.txt"
        )
)
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in songs:
    try:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        pass

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print(f"New playlist '{date} Billboard 100' successfully created on Spotify!")
