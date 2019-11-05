import face_recognition


def facialRecognition():
    picture_of_me = face_recognition.load_image_file("me.jpg")
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

    # need to get this unknown_picture to be a picture taken from camera
    unknown_picture = face_recognition.load_image_file("unknown.jpg")
    unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

    # Now we can see the two face encodings are of the same person with `compare_faces`!
    results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
    if results[0]:
        print("It's a picture of me!")
        return my_face_encoding  # This holds a unique matrix of the face, same each run
    else:
        print("It's not a picture of me!")
        exit()
