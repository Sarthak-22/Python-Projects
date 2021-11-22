## Problem Statement
Real time face detection model using conventional Computer Vision methods in OpenCV

## Approach
* The input data can be taken as an image or a video. This can be done via inbuilt OpenCV methods to read images/videos or one can also use _utils_ library package for easy access to **VideoStream**.
* The input image/frame is then converted to a contour map to detect a change in movement.
