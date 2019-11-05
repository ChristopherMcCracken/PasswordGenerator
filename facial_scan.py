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

for c in contouring:                                    # loop over each countour
    if cv2.contourArea(c) < 100:                        #if too big it will be ignored
        continue

    # compute the rotated bounding box of the contour
    orig = image.copy()
    box = cv2.minAreaRect(c)
    box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
    box = np.array(box, dtype="int")

    box = perspective.order_points(box)
    cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)

    for (x, y) in box:
        cv2.circle(orig, (int(x), int(y)), 5, (0, 0, 255), -1)

    (tl, tr, br, bl) = box
    (tltrX, tltrY) = mid_point(tl, tr)
    (blbrX, blbrY) = mid_point(bl, br)

    (tlblX, tlblY) = mid_point(tl, bl)                  #top left to bottom left
    (trbrX, trbrY) = mid_point(tr, br)                  #top right to bottom right

    # draw midpoints
    cv2.circle(orig, (int(tltrX), int(tltrY)), 5, (255, 0, 0), -1)
    cv2.circle(orig, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
    cv2.circle(orig, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
    cv2.circle(orig, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)

    # draw lines from the midpoints
    cv2.line(orig, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)),
             (255, 0, 255), 2)
    cv2.line(orig, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)),
             (255, 0, 255), 2)

    dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
    dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))

    if pixelsPerMetric is None:                         #in inches, compute the ratio of pixels
        pixelsPerMetric = dB / args["width"]

    dimA = dA / pixelsPerMetric
    dimB = dB / pixelsPerMetric

    # draw the object sizes on the image
    cv2.putText(orig, "{:.1f}in".format(dimA),
                (int(tltrX - 15), int(tltrY - 10)), cv2.FONT_HERSHEY_SIMPLEX,
                0.65, (255, 255, 255), 2)
    cv2.putText(orig, "{:.1f}in".format(dimB),
                (int(trbrX + 10), int(trbrY)), cv2.FONT_HERSHEY_SIMPLEX,
                0.65, (255, 255, 255), 2)

    cv2.imshow("Image", orig)                           # show the outputs to user
    cv2.waitKey(0)

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


