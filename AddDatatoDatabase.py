import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate(("C:/Users/yasser/Desktop/pythonProject2/Site_recherche/serviceAccountKey.json"))
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facialrecognition-33cf6-default-rtdb.firebaseio.com/"
})
ref = db.reference('Persons')

data = {
    "Fugitifs":
    {
    "11":
        {
            "name": "khadija ELMOHTAJ",
            "age": 20,
            "starting_search": 2021,
            "total_detection": 7,
            "last_detection_time": "2022-12-11 00:54:34",
            "img": "C:/Users/yasser/Desktop/pythonProject2/Site_recherche/Images/Fugitifs/11.jpg",
            "addresse":"Rue1",
            "CIN":"EE695830"
        },
    "12":
        {
            "name": "Asmaa EHOU",
            "age": 21,
            "starting_search": 2020,
            "total_detection": 7,
              "last_detection_time": "2022-12-11 00:54:34",
            "img": "C:/Users/yasser/Desktop/pythonProject2/Site_recherche/Images/Fugitifs/12.jpg",
            "addresse":"Rue2",
            "CIN":"EE883611"
        },
    "13":
        {
            "name": "Salma CHAKIRI",
            "age": 20,
            "starting_search": 2022,
            "total_detection": 7,
            "last_detection_time": "2022-12-11 00:54:34",
            "img": "C:/Users/yasser/Desktop/pythonProject2/Site_recherche/Images/Fugitifs/13.jpg",
            "addresse":"Rue3",
            "CIN":"EE883622"
        }
    },

    "Perdus":
    {
    "21":
        {
           "name": "Imane CHAIK",
            "age": 21,
            "starting_search": 2019,
            "total_detection": 6,
           "last_detection_time": "2022-12-11 00:54:34",
            "img": "C:/Users/yasser/Desktop/pythonProject2/Site_recherche/Images/Perduss/21.jpg",
            "addresse":"Rue4",
            "CIN":"EE883666"
        },
    "22":
        {
           "name": "Hajar Ed-rraji",
            "age": 20,
            "starting_search": 2021,
            "total_detection": 7,
            "last_detection_time": "2022-12-11 00:54:34",
            "img": "C:/Users/yasser/Desktop/pythonProject2/Site_recherche/Images/Perduss/22.jpg",
            "addresse":"Rue5",
            "CIN":"EE883644"
        },
    "23":
        {
            "name": "Imane Benchkroune",
            "age": 20,
            "starting_search": 2021,
            "total_detection": 7,
           "last_detection_time": "2022-12-11 00:54:34",
            "img": "C:/Users/yasser/Desktop/pythonProject2/Site_recherche/Images/Perduss/23.jpg",
            "addresse":"Rue6",
            "CIN":"EE883699"
        }
    }
}

for key, value in data.items():
    ref.child(key).set(value)
    
