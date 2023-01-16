# Distance Measurement - OpenCv and cvzone
Real -Time face distance measure from camera using OpenCV and cvzone-FaceMeshModule

# Introduction
Distance Measurement is the process of measuring how far an object is from another. There are many methods to calculate the distance but here, I just measure the distance from camera to object having real size of an object using cvzone and OpenCV.

# Dependencies
### Install Mediapipe
    $ pip3 install cvzone

### Libraries Used
    import cv2
    from cvzone.FaceMeshModule import FaceMeshDetector

# Methods to calculate the distance from camera

#### Calculating the focal length
we have a formula to calulate focal length:

    focal_length = (size_object_pixel * distance)/size_object

In this formula we don't know the object size and distance, but we need the real size of an object. Here, I have took the distance between two eyes i.e apporximately 6.3 and assume initial distance from camera is 50. The size of object pixel can be obtained by cvzone library.

#### Calculating the depth from camera
Now, we can easily calculate focal length. Then, after we can calculate distance from camera:

    distance or depth = (size_object * focal_length_calculated)/size_object_pixel

# Distance Measurement Demo
Click here to watch [demo](/output/distance_measure.avi)

# License
The MIT License (MIT). Please see [License File](/LICENSE) for more information.
