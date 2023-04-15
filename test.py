import cv2
import base64
from flask_socketio import SocketIO, emit
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')


@socketio.on('play')
def emit_video_frames():

    caps = []

    camURLs = [0, "7681061748.mp4"]
    for camItem in camURLs:
        cap = cv2.VideoCapture(camItem)
        caps.append(cap)
    while True:
        # ret1, frame1 = cap1.read()
        # ret2, frame2 = cap2.read()
        
        if not ret1:
            break
        # Convert the frame to a JPEG image
        _, img_encoded = cv2.imencode('.jpg', frame)
        # Convert the JPEG image to a base64-encoded string
        img_base64 = base64.b64encode(img_encoded).decode('utf-8')

        # Emit the base64-encoded image string to the frontend
        emit('video_frame', img_base64)


@socketio.on('pause')
def stop_stream_video():
    print("pause")
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # socketio.start_background_task(emit_video_frames)
    socketio.run(app, debug=True)