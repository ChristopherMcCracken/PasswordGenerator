"""
Test python file to start the facial recognition with openCV
SimpleCV will not work with anything higher than python2.7
OpenCV is what will be used for this project

"""
from scipy.spatial import distance as dist
import imutils
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import cv2

def mid_point(pt_a, pt_b):
    return (pt_a[0] + pt_b[0]) * 0.5, (pt_a[1] + pt_b[1]) * 0.5

ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image", required = True, help = "path to the input image")

ap.add_argument("-w", "--width", type=float,
                required=True, help = "width of the left-most object in the image (in inches)")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])                       # load image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)          # Grayscale the image
gray = cv2.GaussianBlur(gray, (7, 7), 0)                # Blur

edged = cv2.Canny(gray, 50, 100)                        # Edge detections
edged = cv2.dilate(edged, None, iterations=1)           # dilate the edge
edged = cv2.erode(edged, None, iterations=1)            # erode to close gaps

contouring = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)   # Contours
contouring = imutils.grab_contours(contouring)

(contouring, _) = contours.sort_contours(contouring)    # sort by left to right
pixelsPerMetric = None

'''
for c in contouring:
    if cv2.contourArea(c) < 100:
        continue
'''

'''
With openCV we can use:
Background Subtracting,
Color Filtering, 
Edge Detection, 
Feature Matching for Object Recognition **
General Object Recognition **
We will mainly need object recognition and feature matching for this particular program

Link below helps with opencv and how python can detect shapes and compare to other sources
https://www.pyimagesearch.com/2016/03/28/measuring-size-of-objects-in-an-image-with-opencv/
'''


