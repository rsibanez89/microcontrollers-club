from flask import Flask, render_template, request, url_for, jsonify, Response
import serial
import sys
import socket
from camera_pi import Camera
import time

ser = serial.Serial("/dev/serial0",9600)
ser.baudrate=9600

app = Flask(__name__)

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/orders', methods=['POST'])
def make_move():
    direction = request.get_json(force=True)
    if direction['payload'] == 'left':
        pass
    elif direction['payload'] == 'right':
        pass
    elif direction['payload'] == 'up':
        ser.write(b'forward 1 ')
    elif direction['payload'] == 'down':
        ser.write(b'stop ')
    else:
        pass

    return jsonify(direction=direction['payload'])

@app.route('/video_feed')
def video_feed():
   return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    try:
        for x in range(10):
            time.sleep(5)
            # Getting IP Address
            hostname = socket.gethostname()    
            ip = "ip:" + socket.gethostbyname(hostname + ".local") + " "
            ser.write(ip.encode())

        app.run(host='0.0.0.0',port=8080, threaded=True)
    finally:
        sys.exit()
