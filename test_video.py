from flask import Flask, Response, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

def generate():
    # Generate frames for the video stream
    while True:
        # Generate a frame here
        frame = ...
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    # Route for serving the video stream
    return Response(generate(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@socketio.on('connect')
def test_connect():
    print('Client connected')

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app)