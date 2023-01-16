from cvzone.FaceMeshModule import FaceMeshDetector
import cv2

class faceDetector():
    
    def __init__(self, no_of = 2, size_object = 6.3):
        self.no_of = no_of
        self.size_object = size_object 


    def detector(self, image, draw=True):
        self.detect = FaceMeshDetector(maxFaces=self.no_of)   
        img, faces = self.detect.findFaceMesh(image, draw=draw) 

        if faces:
            face = faces[0]
            pointLeft = face[145]
            pointRight = face[374]

            if draw:
                cv2.line(img, pointLeft, pointRight, (0,255, 0), 3)
                cv2.circle(img, pointLeft,5,(255,0,255), cv2.FILLED)
                cv2.circle(img, pointRight,5,(255,0,255), cv2.FILLED)

            size_object_pixel, _ = self.detect.findDistance(pointLeft, pointRight)

            # print(size_object_pixel)

            # Calculating the focal length
            distance = 50

            focal_length = (size_object_pixel * distance)/self.size_object

            # print(focal_length)

            # Calculating the depth
            focal_length_cal = 830
            distance_from_camera = (self.size_object * focal_length_cal)/size_object_pixel

            cv2.putText(image, f'Depth: {int(distance_from_camera)} cm', (face[10][0]-95, face[10][1]-50), cv2.FONT_HERSHEY_SIMPLEX,1, (0,0, 255), 2)

        return image                   

