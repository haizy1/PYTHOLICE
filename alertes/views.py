from django.shortcuts import render
import cv2 as cv
import numpy as np
import pickle as pk
import winsound
from django.shortcuts import render


# Create your views here.
def alertes_view(request):
    return render(request, 'alertes/alertes.html')
def criminels_view(request):
    return render(request, 'criminels/criminels.html')
def home(request):
    return render(request, 'events/home.html', {})
def basededonnées_view(request):
    return render(request, 'basededonnées/basededonnées.html')

#Scripts alertes:


face_cascade = cv.CascadeClassifier('cascades/data/haarcascade_frontalface_default')
recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read("traineru.yml") 

labels = {}
with open("labels.pickle", "rb") as f:
    labels = pk.load(f)
    labels = {v:k for k,v in labels.items()}

def alertes(request):
    camera_location = "ensa"  # Remplacez par la localisation réelle de la caméra
    camera_num_1 = 1  # Numéro de la première caméra
    
    cap = cv.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            id_, conf = recognizer.predict(roi_gray)

            if conf < 90:
                name = "criminal"
            else:
                name = labels[id_]

            font = cv.FONT_HERSHEY_SIMPLEX
            color = (255,255,255)
            stroke = 2
            cv.putText(frame, name, (x,y), font, 1, color, stroke, cv.LINE_AA)
            img_item = "8.png"
            cv.imwrite(img_item, roi_color)
            color = (0, 0, 255)
            stroke = 2
            end_cord_x = x + w
            end_cord_y = y + h
            cv.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

        cv.imshow('frame', frame)
        print("Visage détecté dans la caméra", camera_location, camera_num_1)  # Affiche un message d'alerte avec la localisation de la caméra 1
        winsound.Beep(1000, 500)  # Génère une alerte sonore (fréquence: 1000 Hz, durée: 500 ms)
        
        if cv.waitKey(20) & 0xFF == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()

    return render(request, 'alertes.html')