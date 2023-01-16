import cv2
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    flip_img = cv2.flip(frame, 1)

    if not ret:
        break

    cv2.imshow("Distance Measure", flip_img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

