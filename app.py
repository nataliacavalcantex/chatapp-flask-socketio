  
from flask import Flask, render_template
from flask_socketio import SocketIO, send
from idea import get_encryp_message, get_decryp_message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app,cors_allowed_origins="*")

@app.route('/')
def sessions():
    return render_template('index.html')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    chave = list(range(16))
    print('received my event: ' + str(json))
    message = ''
    if 'message' in json:
        message = get_encryp_message(json['message'], chave)
    
    share(message, json)

@socketio.on('json')
def share(message, j):
    chave = list(range(16))
    ans = None
    json = None
    if message != '':
        ans = get_decryp_message(message, chave)
        json = {
            'user_name': j['user_name'],
            'message': j['message']
        }
    else:
        json = j
    socketio.emit('my response', json, callback=handle_json(json))

def handle_json(json):
    print('received json: ' + str(json))


if __name__ == '__main__':
	socketio.run(app)
    