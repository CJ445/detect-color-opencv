import cv2
from PIL import Image
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

    mask_ = Image.fromarray(mask) # Converting image in the form of NumPy array to actual Image in Pillow

    bbox = mask_.getbbox() # Draws an imaginary box around the detected object and returns the 4 coordinates

    if bbox is not None:
        x1, y1, x2, y2 = bbox # stores coordinates

        frame = cv2.rectangle(frame, (x1, y1, x2, y2), (0, 255, 0), 5) # frame, coordinates, color, thickness of bbox

    cv2.imshow('frame',frame) # if mask is passed instead of frame then the whole screen would be blank (dark)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()