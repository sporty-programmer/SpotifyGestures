# SpotifyGestures
Gesture control for Spotify via Raspberry Pi

## Required components:
- Raspberry Pi with Internet connection and HTTPS available
- Grove Gesture Sensor (PAJ7620U2)
- Jumper-Wires
- Possibly Crimp equipment (if wire endings do not fit DuPont)
- Spotify Application

### 1. Connect Pins as follows:
- VCC -> 3.3V
- GND -> GND
- SDA -> GPIO2
- SCL -> GPIO3

> Check if Pull-Up-Resistors are required and install them if neccessary.

> Some models (as Raspberry Pi 5) have them built in.

### 2. Enable I2C on your Raspberry Pi
1. sudo raspi-config
2. Interface Options
3. I2C
4. Yes
5. Finish

### 3. Install required Python-Packages:
- dotenv
- redis
- urllib3
- requests

> sudo apt install python3-dotenv python3-redis python3-urllib3 python3-requests

### 4. Insert code
- "main.py", "create_data.py" & "grove_gesture_sensor" -> "/usr/local/bin/SpotifyGestures"
- Dowload <a href="https://github.com/spotipy-dev/spotipy/archive/refs/tags/2.25.1.zip">spotipy.zip</a> and paste "spotipy-2.25.1/spotipy" into the project directory
- "SpotifyGestures.service" -> "/etc/systemd/system"

### 5. Configure settings
1. Execute "setup_data.py.py" on a Desktop-Device.\
2. This will open Spotify in Firefox, where you need to login and give permissions to your Application.\
3. After this, ".env" & ".cache" are created in "data/spotipy/".

4. If you want to run the Script on a Device without a Desktop, like on a Raspi with a Lite-OS,\
do Steps 1 to 3 on a Desktop-Device and copy the "data"-folder to the project directoy.

### 6. Run the following commands to load, enable & start your service:
- sudo systemctl daemon-reload
- sudo systemctl enable SpotifyGestures.service
- sudo systemctl start SpotifyGestures.service

### The logs are visible under:
- sudo journalctl -u SpotifyGestures.service (for all logs)
- sudo journalctl -u SpotifyGestures.service -r (for all logs, but the last entries are on top)
- sudo journalctl -u SpotifyGestures.service -f (for only the logs since the last boot)
