import cv2
import time

video = cv2.VideoCapture(0)
while True:

    check, frame = video.read()
    print(check)
    print(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    cv2.imshow("img", frame)
    cv2.imshow("gray", gray)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
