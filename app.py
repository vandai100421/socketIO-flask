import time
import cv2
import base64
from flask_socketio import SocketIO, emit
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*', async_mode='threading')
# socketio = SocketIO(app, ping_timeout=10000,cors_allowed_origins='*'
#                     ping_interval=500, async_mode='threading')


# define function
def frameToBase64 (frame):
    # Convert the frame to a JPEG image
    _, img_encoded = cv2.imencode('.jpg', frame)
    # Convert the JPEG image to a base64-encoded string
    img_base64 = base64.b64encode(img_encoded).decode('utf-8')
    return img_base64

def emitFrame64 (cap, i):
    print(i, "_____________+++++++++++++++")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        img_base64 = frameToBase64(frame)
        # emit('test' +( i + 1), img_base64)

# end define function

caps = [None] * 4
# rtsp 304    "rtsp://admin:Admin123@117.4.240.104:8084/Streaming/Channels/101/"
@socketio.on("multicamera")
def handleGetMultiPath (paths):
    global cap1
    global cap2
    cap1 = cv2.VideoCapture(paths[0])
    cap2 = cv2.VideoCapture(paths[1])
    while True:
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()
        if not ret1 and not ret2:
            break
        img1_base64 = frameToBase64(frame1)
        img2_base64 = frameToBase64(frame2)
        emit('test', [img1_base64,img2_base64])

@socketio.on("camera1")
def multiCamera (path): 
    global cap1
    cap1 = cv2.VideoCapture(path)
    while True:
        ret, frame = cap1.read()
        if not ret:
            break
        img_base64 = frameToBase64(frame)
        emit('test1', img_base64)

@socketio.on("camera2")
def multiCamera (path): 
    global cap2
    cap2 = cv2.VideoCapture(path)
    while True:
        ret, frame = cap2.read()
        if not ret:
            break
        img_base64 = frameToBase64(frame)
        emit('test2', img_base64)

@socketio.on("camera3")
def multiCamera (path): 
    global cap3
    cap3 = cv2.VideoCapture(path)
    while True:
        ret, frame = cap3.read()
        if not ret:
            break
        img_base64 = frameToBase64(frame)
        emit('test3', img_base64)

@socketio.on("camera4")
def multiCamera (path): 
    global cap4
    cap4 = cv2.VideoCapture(path)
    while True:
        ret, frame = cap4.read()
        if not ret:
            break
        img_base64 = frameToBase64(frame)
        emit('test4', img_base64)

@socketio.on("positions")
def receive (arrPositions):
    print(arrPositions, "========================")

@socketio.on('pause')
def stop_stream_video():
    print("stopped video")
    cap1.release()
    cap2.release()


if __name__ == '__main__':
    # socketio.start_background_task(emit_video_frames)
    socketio.run(app, debug=True)