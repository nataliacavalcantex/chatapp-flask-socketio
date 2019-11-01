  
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app,cors_allowed_origins="*")

@app.route('/')
def sessions():
    return render_template('index.html')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=handle_json(json))

def handle_json(json):
    print('received json: ' + str(json))


if __name__ == '__main__':
	socketio.run(app)
    