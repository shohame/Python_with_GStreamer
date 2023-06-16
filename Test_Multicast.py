
import cv2
print(cv2.getBuildInformation())
txt_org = "udpsrc port=5000 ! application/x-rtp,media=video,encoding-name=H264 ! queue ! rtpjitterbuffer latency=500 ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! video/x-raw,format=BGR ! queue ! appsink drop=1"
txt = 'udpsrc multicast-group=224.1.1.1 auto-multicast=true port=5000 ! application/x-rtp,media=video,clock-rate=90000,encoding-name=H264,payload=96 ! rtph264depay ! avdec_h264 ! appsink'
#txt = 'udpsrc multicast-group=224.1.1.1 auto-multicast=true port=5000 ! application/x-rtp,media=video,clock-rate=90000,encoding-name=H264,payload=96 ! rtph264depay ! avdec_h264 ! appsink drop=1'

cap = cv2.VideoCapture(txt, cv2.CAP_GSTREAMER)

# For NVIDIA using NVMM memory
#cap = cv2.VideoCapture("udpsrc port=5000 ! application/x-rtp,media=video,encoding-name=H264 ! queue ! rtpjitterbuffer latency=500 ! rtph264depay ! h264parse ! nvv4l2decoder ! nvvidconv ! video/x-raw,format=BGRx ! videoconvert ! video/x-raw,format=BGR ! queue ! appsink drop=1", cv2.CAP_GSTREAMER)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
#fps = cap.get(cv2.CAP_PROP_FPS) #doesn't work with python in my case so forcing below...you may have to adjust for your case
fps = 30

if not cap.isOpened():
   print('Failed to open camera')
   exit

print('Source opened, framing %dx%d@%d' % (width,height,fps))

while True:
    ret_val, img = cap.read();
    if not ret_val:
        break
    cv2.imshow('image', img)
    cv2.waitKey(1)

cap.release()