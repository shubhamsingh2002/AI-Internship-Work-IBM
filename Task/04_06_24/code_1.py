import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

cap = cv2.VideoCapture(1)
dectector = HandDetector(maxHands=2)

offset = 20
imgsize = 400
counter = 0

folder = "project\Pictures\hello"

while True:
    success, img = cap.read()
    hands, img = dectector.findHands(img)
    if hands:
        hands = hands[0]
        x, y, w, h = hands['bbox']

        imgwhite = np.ones((imgsize, imgsize, 3), np.uint8) * 255

        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

        aspectratio = h / w

        if aspectratio > 1:
            k = imgsize / h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop, (wCal, imgsize))
            imgwhite[:, :wCal] = imgResize
        else:
            k = imgsize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgsize, hCal))
            imgwhite[:hCal, :] = imgResize

        cv2.imshow('ImageCrop', imgCrop)
        cv2.imshow('ImageWhite', imgwhite)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('s'):
        counter += 1
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg', imgwhite)
        print(counter)
