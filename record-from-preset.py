# Thank you @Rotem for this code, which allows you to test your script even if you don't have a camera.
# I am responsible for the feature of changing default location for output files.
# https://stackoverflow.com/questions/60744825/python-3-opencv-unable-to-record-and-save-video

import numpy as np
import cv2
import os
default_location = './resulting-media/'
input_filename = 'configurable-preset.avi'

# Generate synthetic video to be used as input:
###############################################################################
width  = 640
height = 480

n_frames = 10

# Use motion JPEG codec (for testing)
synthetic_out = cv2.VideoWriter(default_location+input_filename, cv2.VideoWriter_fourcc(*'MJPG'), 25, (width, height))

for i in range(n_frames):
    img = np.full((height, width, 3), 60, np.uint8)
    cv2.putText(img, str(i), (width//2-100*len(str(i)), height//2+100), cv2.FONT_HERSHEY_DUPLEX, 10, (30, 255, 30), 20)
    #cv2.imshow('img',img)
    #cv2.waitKey(100)
    synthetic_out.write(img)

synthetic_out.release()
###############################################################################



filename = 'output-from-preset.avi'
frames_per_second = 24.0
res = '720p'

def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)

STD_DIMENSIONS =  {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160),
}

def get_dims(cap, res='1080p'):
    width, height = STD_DIMENSIONS["480p"]
    if res in STD_DIMENSIONS:
        width,height = STD_DIMENSIONS[res]
    ## change the current capture device
    ## to the resulting resolution
    change_res(cap, width, height)
    return width, height

VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    #'mp4': cv2.VideoWriter_fourcc(*'H264'),
    'mp4': cv2.VideoWriter_fourcc(*'mp4v'),
}

def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
      return  VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']


# Read video from file instead of from camera.
cap = cv2.VideoCapture(default_location+input_filename)
#cap = cv2.VideoCapture(0)

fourcc = get_video_type(filename)

# Get resolution of input video
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


# out = cv2.VideoWriter(filename, get_video_type(filename), 25, get_dims(cap, res))

# The second argument of VideoWriter is FOURCC code
# Set the size of the output video to be same as the input (get_dims is not working).
out = cv2.VideoWriter(default_location+filename, fourcc, frames_per_second, (width, height))

while True:
    ret, frame = cap.read()

    if not ret:
        # Break loop if ret is False
        break

    out.write(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
