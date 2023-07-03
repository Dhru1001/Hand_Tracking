import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()

while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=False)
    lmList = detector.findPosition(img, draw=False)

    # Check if there are at least two hands detected
    if len(lmList) >= 2 * 21:
        # Print the coordinates of the 5th landmark for each hand
        print("Hand 1:", lmList[4])
        print("Hand 2:", lmList[25])  # Assuming hand landmarks are stored consecutively
    elif len(lmList) >= 21:
        # Print the coordinates of the 5th landmark for the first hand
        print("Hand 1:", lmList[4])

    cTime = time.time()
    fps = 0  # Initialize fps with a default value
    if pTime != 0:
        fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
