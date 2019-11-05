import face_recognition     # can use this or possibly OpenCV as well
import cv2                  # for webcams use
import numpy as np          # for shapes, contouring, corners etc.

def facialRecognition():

    video = cv2.VideoCapture(0)     #starts the camera

    picture_of_me = face_recognition.load_image_file("me.jpg")
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

    # need to get this unknown_picture to be a picture taken from camera
    unknown_picture = face_recognition.load_image_file("unknown.jpg")
    unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

    known_faces = [
        picture_of_me
    ]

    known_face_names = [
        "Quintin",
        "Chris",
        "Jordan"
    ]

    """
    WHAT WE NEED:
    We need to be able to open the computers webcam with cv2 and scan the face. 
    It will then scan the face it is currently looking at and compare against the known_faces. Then when it 
    recognizes the known face it attaches the known_face_names with the face. This may or may not be
    needed. We can keep for testing purposes.
    
    """

    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        ret, frame = video.read()       #grab one frame from video

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)       #frame size is 1/4 for faster process
        rgb_small_frame = small_frame[:, :, ::-1]       #face recognition uses RGB instead of BGR(OpenCV)

        # process every other frame
        if process_this_frame:
            # find all faces
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # does it match a known face?
                matches = face_recognition.compare_faces(known_faces, face_encoding)
                name = "Face not recognized"

                # # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_faces, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame

        # Display
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale  1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw boxes around each face detected
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Label with name below the above box
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the image
        cv2.imshow('Video', frame)

        # To quit just hit q on the keyboards
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam
    video.release()
    cv2.destroyAllWindows()

"""
    # Now we can see the two face encodings are of the same person with `compare_faces`!
    results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
    if results[0]:
        print("It's a picture of me!")
        return my_face_encoding  # This holds a unique matrix of the face, same each run
    else:
        print("It's not a picture of me!")
        exit()
"""