from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET'] = 'secret!12'
socketio = SocketIO(app, cors_allowed_origins="*")

#triggers the handle message function
@socketio.on('message')
def handle_message(message):
    # when a message has been sent to someone
    print("Recieved message: " + message)
    if message != "User connected!":
        # send message here
        send(message,broadcast=True)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '"__main__':
    socketio.run(app,host="localhost")



