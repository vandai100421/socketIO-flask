import cv2
import threading

# Define a function to display a video on a separate thread
def display_video(video_file):
    # Open the video file
    cap = cv2.VideoCapture(video_file)

    # Loop through the frames and display them
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('Video', frame)
            cv2.waitKey(1)
        else:
            break

    # Release the video capture object and close the window
    cap.release()
    cv2.destroyAllWindows()

# Create a list of video files to display
video_files = ['test.mp4', '7681061748.mp4']

# Create a thread for each video file
threads = []
for video_file in video_files:
    thread = threading.Thread(target=display_video, args=(video_file,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()
