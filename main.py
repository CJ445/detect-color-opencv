import cv2

from util import get_limits

yellow = [0, 255, 255] # yellow in BGR colorspace


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error reading frame. Exiting.")
        break

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # Converting colorspace

    lowerLimit, upperLimit = get_limits(color=yellow)


    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit) # defining interval

    cv2.imshow('frame', mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()