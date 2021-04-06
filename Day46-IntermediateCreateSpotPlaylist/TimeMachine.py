date = input("Which year do you want to travel to? YYYY-MM-DD:")

from bs4 import BeautifulSoup
import requests
import spotipy
import config
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id= config.clientId,
        client_secret= config.clientSecret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

URL = "https://www.billboard.com/charts/hot-100/"

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
print(soup.title)
song_span = soup.find_all("span", class_="chart-element__information__song")

song_names = [song.getText() for song in song_span]

print(song_names)