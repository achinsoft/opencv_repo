import cv2
import time

video = cv2.VideoCapture(0)
while True:

    check, frame = video.read()

    frame=cv2.resize(frame, (200, 200))
    print(check)
    print(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    guss = cv2.GaussianBlur(gray, (21, 21), 0)
    cv2.imshow("img", frame)
    cv2.imshow("gray", gray)
    cv2.imshow("guss", guss)
    key = cv2.waitKey(100)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
