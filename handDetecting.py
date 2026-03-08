
import cv2
from cvzone.HandTrackingModule import HandDetector

#isko use krke humara code short hoga bss -> ye older version hai
import mediapipe as mp

#detectionCon : Minimum confidence level for detecting a hand , accuracy bdaa di 
#maxHands=2 → Detect maximum 2 hands in the frame.
detector = HandDetector(detectionCon=0.8, maxHands=2)

cap = cv2.VideoCapture(0)

#.set identies hoti hai
#syntax : cap.set(property ID , value you are setting)
# refer table
cap.set(3,2120) #3 - frame widht id , 2120 - pixel width
cap.set(4,1080) #Frame height

"""
property ID -> 0 to 18
0. CV_CAP_PROP_POS_MSEC Current position of the video file in milliseconds.
1. CV_CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
2. CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file
3. CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
4. CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
5. CV_CAP_PROP_FPS Frame rate.
6. CV_CAP_PROP_FOURCC 4-character code of codec.
7. CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.
8. CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
9. CV_CAP_PROP_MODE Backend-specific value indicating the current capture mode.
10. CV_CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
11. CV_CAP_PROP_CONTRAST Contrast of the image (only for cameras).
12. CV_CAP_PROP_SATURATION Saturation of the image (only for cameras).
13. CV_CAP_PROP_HUE Hue of the image (only for cameras).
14. CV_CAP_PROP_GAIN Gain of the image (only for cameras).
15. CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
16. CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
17. CV_CAP_PROP_WHITE_BALANCE Currently unsupported
18. CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)
"""

while True: #This loop keeps running taki webcam video updates continuously

    #res -> True/False if frame was captured
     #frame -> webacam ki Actual image
    res, frame = cap.read() # ik fame ko capture

    hands, img = detector.findHands(frame) #main hand detection step

    if hands:
        hand = hands[0]  # first hand
        lmList = hand["lmList"]  # 21 landmark points
        bbox = hand["bbox"]  # rectangle around the hand

        print(lmList[8])  # index finger tip position

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()