import glob
import face_recognition


def open_files(img):
    for filename in sorted(glob.glob('/home/maska/Documents/hakaton_fbr/registered_photos/' + '*.jpg')):
        img1 = '/home/maska/Documents/hakaton_fbr/photos/11111.jpg'
        face = face_recognition.load_image_file(img1)
        face = face_recognition.face_encodings(face)[0]
        unknown_picture = face_recognition.load_image_file(filename)
        unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
        results = face_recognition.compare_faces([face], unknown_face_encoding)
        if results[0] == True:
            return ("https://vk.com/id"+filename[52:-4])
