from typing import Callable

from time import sleep as delay

from os import path, chdir

from dotenv import dotenv_values

from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

from grove_gesture_sensor import gesture as GestureSensor # NOQA


# PREPARATIONS
chdir(cwd := path.dirname(path.realpath(__file__)))


# INITIALIZE SPOTIPY
client_data: dict[str, str] = dotenv_values()

spotify: Spotify = Spotify(auth_manager=SpotifyOAuth(
    client_id=client_data["CLIENT_ID"],
    client_secret=client_data["CLIENT_SECRET"],
    redirect_uri="http://localhost:8080",
    scope="user-modify-playback-state user-read-playback-state user-read-currently-playing",
    cache_path=f"{cwd}/.cache"
))

print("Spotipy initialized.")


# INITIALIZE GESTURE SENSOR

sensor: GestureSensor = GestureSensor()

while True:

    try:
        sensor.init()
        break

    except IOError:
        continue

print("Gesture Sensor initialized.")


# CONTROL FUNCTIONS

def spotify_control_function(function) -> Callable:

    def wrapper() -> None:

        current_playback: dict | None = spotify.current_playback()

        if not current_playback:
            print("No current playback found.")
            return
        
        function(current_playback)
    
    return wrapper


@spotify_control_function
def toggle_play(current_playback: dict) -> None:

    if current_playback["is_playing"]:
        spotify.pause_playback()
        print("Playback paused.")

    else:
        spotify.start_playback()
        print("Playback resumed.")


@spotify_control_function
def next_track(current_playback: dict) -> None:
    spotify.next_track()
    print("Skipped to next track.")


@spotify_control_function
def previous_track(current_playback: dict) -> None:
    spotify.previous_track()
    print("Skipped to previous track.")


@spotify_control_function
def volume_up(current_playback: dict) -> None:
    print(f"Turned up playback volume to {change_volume(current_playback, 10)}%.")


@spotify_control_function
def volume_down(current_playback: dict) -> None:
    print(f"Turned down playback volume to {change_volume(current_playback, -10)}%.")


def change_volume(current_playback: dict, percent: int) -> int:

    volume: int = current_playback["device"]["volume_percent"]
    
    volume += percent
    volume = 0 if volume < 0 else volume # ensure that volume is not below 0
    volume = 100 if volume > 100 else volume # ensure that volume is not over 100

    spotify.volume(volume)

    return volume


# MAIN LOOP
while True:

    try:

        match sensor.return_gesture():

            case 1: # forward
                toggle_play()
            
            case 3: # up
                volume_up()        

            case 4: # down
                volume_down()

            case 5: # left
                previous_track()    

            case 6: # right
                next_track()

            case _: # else
                pass

        delay(0.01)
    
    except KeyboardInterrupt:
        print("Stopping program.")
        break