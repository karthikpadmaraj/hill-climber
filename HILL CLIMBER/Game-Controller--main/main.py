import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
import pyautogui

detector = HandDetector(detectionCon=0.5, maxHands=2)
cap = cv.VideoCapture(0)
cap.set(3,400)
cap.set(4,600)

while True:
    success, img = cap.read()
    img = cv.flip(img, 1)
    hand, img = detector.findHands(img)
    if hand and hand[0]["type"] == "Left":
        fingers = detector.fingersUp(hand[0])
        nbFingers = fingers.count(1)
        cv.putText(img,f'Fingers : {nbFingers}',(350, 50), cv.FONT_HERSHEY_PLAIN,2,(0,255,0),2)
        if nbFingers == 5:
            pyautogui.keyDown("right")
            pyautogui.keyUp("left")
        if nbFingers == 0:
            pyautogui.keyDown("left")
            pyautogui.keyUp("right")

    cv.imshow('Game camera', img)
    cv.waitKey(1)
