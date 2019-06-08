import glob
import face_recognition

def face_compare_func(img1, img2):
    img1 = 'photos/50210887.jpg'
    img2 = 'photos/50210887.jpg'
    face = face_recognition.load_image_file('photos/50210887.jpg')
    face = face_recognition.face_encodings(face)[0]
    unknown_picture = face_recognition.load_image_file('photos/50210887.jpg')
    unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
    results = face_recognition.compare_faces([face], unknown_face_encoding)
    
    if results[0] == True:
        print('-----------------------------------------------------')
    else:
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++')

def open_files(img):
    for filename in glob.glob('registered_photos/' + '*.jpg'):
        filename = filename
        print(face_compare_func(filename, img))

face_compare_func(1, 1)
