import cv2
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import  storage

cred = credentials.Certificate("C:/Users/yasser/Desktop/pythonProject2/Site_recherche/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facialrecognition-33cf6-default-rtdb.firebaseio.com/",
    'storageBucket': "facialrecognition-33cf6.appspot.com"
})
# Importing images
folderPath = 'C:/Users/yasser/Desktop/pythonProject2/Site_recherche/Images/Perdus_detected'
#folderPath = 'C:/Users/yasser/Desktop/pythonProject2/Site_recherche/Images/Fugitifs_detected'
#folderPath = 'C:/Users/yasser/Desktop/pythonProject2/Site_recherche/Images/Perdus'
#folderPath = 'C:/Users/yasser/Desktop/pythonProject2/Site_recherche/Images/Fugitifs'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
PersonsIds = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    PersonsIds.append(os.path.splitext(path)[0])
    

    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
