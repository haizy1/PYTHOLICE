#DANS events CREER UN FICHIER "camera.py" ET COLLER CE CODE DEDANS
import cv2
from simple_facerec import SimpleFacerec
import numpy as np
import pickle as pk
import winsound

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Load Camera
cap = cv2.VideoCapture(0)
camera_location = "ensa"
camera_num_1 = 1

# Load emergency sound
emergency_sound = 'emergency.wav'

while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

        # Play emergency sound
        winsound.Beep(1000, 500)

    cv2.imshow("Frame", frame)
    print("Visage detecte dans la camera", camera_location, camera_num_1)  # Affiche un message d'alerte avec la localisation de la camera 1
    key = cv2.waitKey(1)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()µ
#
#___________________________________________________________________________________
#
#DANS events -> "views.py" COLLER CE CODE
from django.shortcuts import render
import cv2
from django.http import HttpResponse
from django.template import loader
import winsound

def video_feed(request):
    # Load Camera
    cap = cv2.VideoCapture(0)

    def generate():
        while True:
            ret, frame = cap.read()
            _, jpeg = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')

    return HttpResponse(generate(), content_type='multipart/x-mixed-replace; boundary=frame')


def detect_faces(request):
    # Encode faces from a folder
    sfr = SimpleFacerec()
    sfr.load_encoding_images("images/")

    # Load Camera
    cap = cv2.VideoCapture(0)
    camera_location = "ensa"
    camera_num_1 = 1

    # Load emergency sound
    emergency_sound = 'emergency.wav'

    while True:
        ret, frame = cap.read()

        # Detect Faces
        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

            cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

            # Play emergency sound
            winsound.Beep(1000, 500)

        cv2.imshow("Frame", frame)
        print("Visage detecte dans la camera", camera_location, camera_num_1)  # Affiche un message d'alerte avec la localisation de la camera 1
        key = cv2.waitKey(1)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
 
#
#___________________________________________________________________________________
#
#DANS events -> "urls.py" COLLER CE CODE
from django.contrib import admin
from django.conf.urls import path
from django.urls import include
from events.views import video_feed, detect_faces

urlpatterns = [
    path('video_feed/', video_feed, name='video_feed'),
    path('detect_faces/', detect_faces, name='detect_faces'),
]

#
#___________________________________________________________________________________
#
#DANS events -> "templates/home.html" COLLER CE CODE
<!DOCTYPE html>
<html>
<head>
    <title>Video Stream</title>
</head>
<body>
    <h1>Video Stream</h1>
    <img src="{% url 'video_feed' %}" />
</body>
</html>