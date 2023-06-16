



gst-launch-1.0 gdiscreencapsrc ! decodebin ! videoconvert ! x264enc tune=zerolatency bitrate=5000 speed-preset=superfast ! rtph264pay ! multiudpsink clients="224.1.1.1:5000" sync=false async=false udpsrc port=11000




gst-launch-1.0 udpsrc multicast-group=224.1.1.1 auto-multicast=true port=5000 ! application/x-rtp,media=video,clock-rate=90000,encoding-name=H264,payload=96 ! rtph264depay ! avdec_h264 ! autovideosink


change autovideosink to  appsink  for opencv2











Server to cuptuer the sreen:
#  gst-launch-1.0 gdiscreencapsrc ! decodebin ! videoconvert ! x264enc tune=zerolatency bitrate=5000 speed-preset=superfast ! rtph264pay ! multiudpsink clients="226.226.226.123:3333" sync=false async=false udpsrc port=11000
# udpsrc multicast-group=224.1.1.1 auto-multicast=true port=5000

#  gst-launch-1.0 udpsrc port=11000 ! application/x-rtp,media=video,clock-rate=90000,encoding-name=H264,payload=96 ! rtph264depay ! avdec_h264 ! autovideosink



# Server
#  gst-launch-1.0 -v filesrc location=D:\Work\PycharmProjects\Mulicast_Video\data\test_video.mp4 ! decodebin ! videoconvert ! x264enc tune=zerolatency ! rtph264pay ! udpsink host=localhost port=5000


# Client
#  gst-launch-1.0 udpsrc port=5000 ! application/x-rtp,media=video,clock-rate=90000,encoding-name=H264,payload=96 ! rtph264depay ! avdec_h264 ! autovideosink



#   for cv2 appsink at the end
#  autovideosink (to open window)



