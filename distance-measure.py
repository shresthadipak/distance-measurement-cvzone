import cv2
from faceModule import faceDetector

cap = cv2.VideoCapture(0)

detector = faceDetector()
out = cv2.VideoWriter('output/distance_measure.avi', cv2.VideoWriter_fourcc(*'MPEG'), 7, (640, 480))
while True:
    ret, frame = cap.read()
    flip_img = cv2.flip(frame, 1)
    image = detector.detector(flip_img, draw=False)

    if not ret:
        break

    out.write(image)    
    cv2.imshow("Distance Measure", image)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

