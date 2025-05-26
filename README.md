# SpotifyGestures
Gesture control for Spotify via Raspberry Pi

## Needed components:
- Raspberry Pi with Internet connection
- Grove Gesture Sensor (PAJ7620U2)
- Jumper-Wires
- possibly Crimp equipment (if wire endings do not fit DuPont)

### 1. Connect Pins as follows:
- VCC -> 3.3V
- GND -> GND
- SDA -> GPIO2
- SCL -> GPIO3

> [!IMPORTANT]
> Check if Pull-Up-Resistors are required and install them if neccessary.

> [!NOTE]
> Some models (as Raspberry Pi 5) have them built in.

### 2. Enable I2C on your Raspberry Pi
1. sudo raspi-config
2. Interface Options
3. I2C
4. Yes
5. Finish

### 3. Install required Python-Packages:
- dotenv

> sudo apt install python-dotenv

### 4. Insert code
- spotipy, .cache, .env, grove_gesture_sensor.py & main.py -> /usr/local/bin/SpotifyGestures
- SpotifyGestures.service -> /etc/systemd/system

### 5. Run the following commands to start your service:
- sudo systemctl daemon-reload
- sudo systemctl enable SpotifyGestures.service
- sudo systemctl start SpotifyGestures.service

### The logs are visible under:
- sudo journalctl -u SpotifyGestures.service (for all logs)
- sudo journalctl -u SpotifyGestures.service -r (for all logs, but the last entries are on top)
- sudo journalctl -u SpotifyGestures.service -f (for only the logs since the last boot)
