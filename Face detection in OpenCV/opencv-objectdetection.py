## Sarthak
import cv2 as cv
from imutils.video import VideoStream
import imutils
import time
import argparse

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
args = vars(ap.parse_args())

# if the video argument is None, then we are reading from webcam
if args.get("video", None) is None:
    vs = VideoStream(src=0).start()
    time.sleep(2.0)

# initialize the first frame in the video stream
firstFrame = None

# loop over the frames of the video 
while True:
    # grab the current frame and initialize the occupied/unoccupied text
    frame = vs.read()
    frame = frame if args.get("video", None) is None else frame[1]
    text="static"

    if frame is None:
        break

    # resize the frame, convert it to grayscale, and blur it
    frame = imutils.resize(frame, width=500)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray = cv.GaussianBlur(gray, (21,21), 0)

    if firstFrame is None:
        firstFrame = gray
        continue

    frameDelta = cv.absdiff(firstFrame, gray)
    thresh = cv.threshold(frameDelta, 100, 255, cv.THRESH_BINARY)[1]

    thresh = cv.dilate(thresh, None, iterations=2)
    cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    # loop over the contours
    for c in cnts:
        if cv.contourArea(c) < args["min_area"]:
            continue

        # Compute the bonding box for the contour, draw it on the frame, and update the text
        (x,y,w,h) = cv.boundingRect(c)
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        text="person"

    cv.putText(frame, "Status: {}".format(text), (10,20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)

    cv.imshow("Security feed", frame)
    cv.imshow("Thresh", thresh)
    cv.imshow("Frame Delta", frameDelta)
    key = cv.waitKey(1) & 0xFF

    if key==ord("q"):
        break

vs.stop() if args.get("video", None) is None else vs.release()
cv.destroyAllWindows()


