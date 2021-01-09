import json

from flask_cors import cross_origin
from flask_socketio import emit, SocketIO

from Utilities.Tocken import verify

mySocket = SocketIO(cors_allowed_origins="*")

@mySocket.on('connect')
def on_connect():
    print('socket connected')
    emit('test', 'AAAAA')

@mySocket.on('message')
def handle_message(data):
    authDetails = json.loads(data)

    if authDetails["type"] != "authorization":
        print('Nu e bine!!')
    else:
        verify(authDetails['payload']['token'])