import socketio

sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('connection established')

@sio.on('my message')
def on_message(data):
    print('Enviando Mensagem para servidor', data)
    sio.emit('message', data)

@sio.on('disconnect')
def on_disconnect():
    print('disconnected from server')

sio.connect('http://127.0.0.1:3000')
on_message({'Ola':'Mundo'})
sio.wait()