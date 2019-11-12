import cv2

def takeUserImage():
    cam = cv2.VideoCapture(0)

    imageTaken = False

    while True:
        ret, frame = cam.read()
        cv2.imshow("Take picture", frame)
        if not ret:
            break

        keyPress = cv2.waitKey(1) & 0xFF

        # check if 'q' or the space bar is pressed
        # q quits the window and the space bar takes a picture
        if keyPress == ord('q'):
            print("Closing window. No image taken")
            break
        elif keyPress == ord(' '):
            imgName = "user.jpg"
            cv2.imwrite(imgName, frame)
            print("Image taken, closing window")
            imageTaken = True
            break

    cam.release()

    cv2.destroyAllWindows()

    return imageTaken
