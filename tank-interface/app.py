from flask import Flask, render_template, request, url_for, jsonify, Response
import serial
import sys
import socket
import time

# Getting IP Address
hostname = socket.gethostname()    
ip = "ip:" + socket.gethostbyname(hostname + ".local")

ser = serial.Serial("/dev/ttyACM0",9600)
ser.baudrate=9600
time.sleep(5) # Wait until Arduino is Connected.
ser.write(ip.encode())

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/forward', methods=['GET'])
def mov_forward():
    ser.write(b'forward 1 ')

@app.route('/stop', methods=['GET'])
def stop():
    ser.write(b'stop ')

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0',port=8080, threaded=True)
    finally:
        sys.exit()