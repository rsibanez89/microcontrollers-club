# first time
# git clone https://github.com/rsibanez89/microcontrollers-club.git

while :; do
   ping -c 1 -w 3 8.8.8.8; echo $? > /tmp/ping.status
   sleep 1
done

cd /home/pi/microcontrollers-club
git pull

python tank-interface/app.py