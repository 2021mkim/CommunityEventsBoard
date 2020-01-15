import os
from app import app
from flask import render_template, request, redirect

events = [
        {"event":"First Day of Classes", "date":"2019-08-21"},
        {"event":"Winter Break", "date":"2019-12-20"},
        {"event":"Finals Begin", "date":"2019-12-01"}
    ]

from flask_pymongo import PyMongo
# from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = 'events'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://dbUser:GXPdgXz1pMA2KZlx@cluster0-qwaak.mongodb.net/events?retryWrites=true&w=majority'

mongo = PyMongo(app)


# INDEX

@app.route('/')
@app.route('/index')

def index():
  # connect to the database
    collection = mongo.db.events
    #query the database to all events
    events = list(collection.find({}))
    # store events as a dictionary call events
    for x in events:
        print(x["event_name"])
    # print event
    return render_template('index.html', events = events)

# CONNECT TO DB, ADD DATA

@app.route('/add')

def add():
    # connect to the database
    collection = mongo.db.events
    # insert new data
    collection.insert({"event_name": "test", "event_date": "today"})
    # return a message to the user
    return "you added an event to the database"

@app.route('/results',methods = ["get", "post"])

def results():
    # connect to the database
    userinfo = dict(request.form)
    print(userinfo)
    event_name = userinfo["event_name"]
    event_date = userinfo["event_date"]
    event_category = userinfo["event_category"]
    collection = mongo.db.events
    # insert new data
    collection.insert({"event_name": event_name, "event_date": event_date ,"event_category":event_category})
    # collection.insert({"event_name": "test", "event_date": "today"})
    # return a message to the user
    return redirect("/index")

@app.route("/secret")
def secret():
    #connect to the database
    collection = mongo.db.events
    #delete everything from the database
    #invoke the delete_many method on the collection
    collection.delete_many({})
    return redirect('/index')

@app.route("/school")
def school():
    collection = mongo.db.events
    school_event = collection.find({"event_category" : "school"})
    return render_template('index.html', events = school_event)

@app.route("/service")
def service():
    collection = mongo.db.events
    school_event = collection.find({"event_category" : "service"})
    return render_template('index.html', events = school_event)

@app.route("/travel")
def travel():
    collection = mongo.db.events
    school_event = collection.find({"event_category" : "travel"})
    return render_template('index.html', events = school_event)
