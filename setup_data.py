from sys import exit as sys_exit

from os import path, chdir, makedirs

import logging

from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth


# ENSURANCE

# print warnings
print(f"The content of the following file will get deleted and replaced:")
print("1. \"{env_dir}\"", "2. \"{cache_dir}\"", sep="\n")
print()

# await agreement
while True:
    match input("Do you want to proceed? [y/n] "):
        case "y":
            break
        case "n":
            sys_exit(0)
        case _:
            pass

print()


# PREPARATIONS

# set current working directory
chdir(cwd := path.dirname(path.realpath(__file__)))

# silence spotipy warnings
logging.getLogger('spotipy').setLevel(logging.ERROR)

# set paths
base_dir: str = f"{cwd}/data/spotipy"
env_dir: str = f"{base_dir}/.env"
cache_dir: str = f"{base_dir}/.cache"

# create dir if necessary
if not path.exists(base_dir):
    makedirs(base_dir)


# GET CLIENT-DATA

# input client-data manually
client_id: str = input("CLIENT_ID: ")
client_secret: str = input("CLIENT_SECRET: ")

# save client-data in env file
with open(env_dir, "w") as file:
    file.write(f"CLIENT_ID={client_id}")
    file.write(f"CLIENT_SECRET={client_secret}")

# inform user
print(f"\n{env_dir} is now up to date.")


# GET TOKEN CACHE

# empty file
with open(cache_dir, "w") as file:
    pass

# trigger token access through action with token requirement to save it in cache file
Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri="http://localhost:8080",
    scope="user-modify-playback-state user-read-playback-state user-read-currently-playing",
    cache_path=cache_dir
)).current_user()

# inform user
print(f"{cache_dir} is now up to date.")


# hold window open
input("\nPress ENTER to close this window.")