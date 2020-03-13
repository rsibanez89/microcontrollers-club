# Remove directory if exists
rm -r -f /home/pi/microcontrollers-club

# Clone repository
git clone https://github.com/rsibanez89/microcontrollers-club.git /home/pi/microcontrollers-club

python /home/pi/microcontrollers-club/tank-interface/app.py