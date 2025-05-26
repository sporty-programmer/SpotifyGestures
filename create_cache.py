from os import path, chdir

from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth


# PREPARATIONS

chdir(cwd := path.dirname(path.realpath(__file__)))


# INITIALIZE SPOTIPY

spotify: Spotify = Spotify(auth_manager=SpotifyOAuth(
    client_id=input("CLIENT_ID: "),
    client_secret=input("CLIENT_SECRET: "),
    redirect_uri="http://localhost:8080",
    scope="user-modify-playback-state user-read-playback-state user-read-currently-playing",
    cache_path=f"{cwd}/.cache"
))

print("Spotipy initialized.")

spotify.current_user()

print("Cache is now written.")

input("Press ENTER to close this window.")