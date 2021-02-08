import pyrebase

config = {
    "apiKey": "AIzaSyDYMIiRWQL3mB5LMlDmozCoGeBS-dkOeLE",
    "authDomain": "my-first-app-d7846.firebaseapp.com",
    "databaseURL": "https://my-first-app-d7846-default-rtdb.firebaseio.com",
    "projectId": "my-first-app-d7846",
    "storageBucket": "my-first-app-d7846.appspot.com",
    "messagingSenderId": "283305479305",
    "appId": "1:283305479305:web:a10854a818c542ad418a58",
    "measurementId": "G-2ZQF1S7SDS"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
#db.child("Sent by Python").child("Morty")
data={"Pyname":["Naz","tbt"],"Pyocc":"TA"}
#db.child("Messages").push(data)
db.child("Python messages").set(data)