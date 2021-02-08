""" wrangling.py - utilities to supply data to the templates.

This file contains a pair of functions for retrieving and manipulating data
that will be supplied to the template for generating the table."""
import csv
import pyrebase


def username():
    return 'nata3'
def listToString(s):  
    
    # initialize an empty string 
    str1 = " " 
    
    # return string   
    return (str1.join(s)) 
def data_wrangling():
    
    

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
    data=[]
    data1 = db.child("Messages").get()
    for m in data1.each():
        data.append(m.key()+": "+m.val())
    datapy=[]
    datapy1 = db.child("Python messages").get()
    for m in datapy1.each():
        if type(m.val())==list:
            val=listToString( m.val())
        else:
            val=m.val()
        datapy.append(m.key()+": "+val)
    #print(users.val()) # {"Morty": {"name": "Mortimer 'Morty' Smith"}, "Rick": {"name": "Rick Sanchez"}}

    return data,datapy

