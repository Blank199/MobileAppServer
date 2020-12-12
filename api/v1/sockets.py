from flask_socketio import send

from app import mySocket


@mySocket.on('message')
def handle_message(message):
    send(message)
