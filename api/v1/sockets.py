from flask_cors import cross_origin
from flask_socketio import emit

from app import mySocket


@mySocket.on('connect')
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def on_connect():
    print('user connected')
    emit('connect')
