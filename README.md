# SpotifyGestures
Gesture control for Spotify via Raspberry Pi

Needed components: Raspberry Pi with Internet connection, Grove Gesture Sensor (PAJ7620U2), Jumper-Wires and possibly Crimp equipment (if wire endings do not fit DuPont)

Connect Pins as follows:
 - VCC -> 3.3V
 - GND -> GND
 - SDA -> GPIO2
 - SCL -> GPIO3

Check if Pull-Up-Resistors are required (Raspberry Pi 5 has them built in)

Enable I2C on your Raspberry Pi

Install required Python-Packages: 
 - dotenv

Preparations should be complete now.

If you want to run ist as a service (as I do),
make sure it starts after Internet connection is ready.
