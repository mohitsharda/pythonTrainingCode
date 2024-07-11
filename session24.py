"""
   Web Application Development With Flask

   1. Install Flash In Virtual Env
      pip Install FLask

    2. Create object of flask

    3. Create a function run the flask app using run()

    4. in main function 

"""

from flask import *
import datetime
import hashlib
from session21C import MongoDbHelper

#create the object of flask
# which represent a web application
 
webApp = Flask("DOCTORS APP: ")
dbHelper = MongoDbHelper()

@webApp.route("/") # Decorator  "/ ->> is a home-Page"
def index():
    #here you can either return plane text or you cann return html
    # message = "Welcome to patient management system: Its.  {}".format(datetime.datetime.now()
    # message = """
    # <html>
    # <head>
    #     <title>Doctor App</title>
    #     <body>
    #         <centre>
    #            <h3>
    #            WELCOME TO PATIENT MANAGEMENT SYSTEM
    #            </h3>
    #         </centre>
    #     </body>
    # </head>
    # </html>

    # """
    # return message
    return render_template("index.html")


@webApp.route("/register") # Decorator  "/ ->> is a Register-page"
def register():
    return render_template("register.html")

@webApp.route("/add-user", methods=["POST"]) 
def addUserInDb():
    # Create a dictionary with data from html register form
    userData = {
        "name":  request.form["name"],
        "email":  request.form["email"],
        "password":  hashlib.sha256(request.form["password"].encode('utf-8')).hexdigest(),
       "createdOn":  datetime.datetime.now()
    }

    dbHelper.collection = dbHelper.db["users"]
    # Save user in database ie MongoDb
    result = dbHelper.insert(userData)
    # message = "Welcome to HomePage . User Id is: {}".format(result.inserted_id)
    # return message


    # Write the data in the Session Object
    # This data can now be used anywhere in the project
    session['name'] = userData["name"]
    session['email'] = userData["email"]

    # return render_template("home.html", name=session['name'], email=session['email'])
    return render_template("home.html",name=session['name'], email=session['email'])


@webApp.route("/fetch-user", methods=["POST"])
def fethUserFromDb():

    # Create a Dictionary with Data from HTML Register Form
    userData = {
        "email": request.form["email"],
        "password": hashlib.sha256(request.form["password"].encode('utf-8')).hexdigest(),
    }

    dbHelper.collection = dbHelper.db["users"]
    # Fetch user in DataBase i.e. MongoDB
    result = dbHelper.fetch(query=userData)

    print("result is: ", result)

    if len(result)>0:
        userData = result[0] # get the dictionary from list
        session['email'] = userData["email"]
        session['name'] = userData["name"]
        return render_template("home.html", name=session['name'],    email=session['email'])
    else:
        return "User Not Found. Please Try Again"


@webApp.route("/add-patient", methods=["POST"])
def addPatientInDb():

    # Create a Dictionary with data from html register form
    patientData = {
        "name": request.form["name"],
        "email": request.form["email"],
        "phone": request.form["phone"],
        "gender": request.form["gender"],
        "age": int(request.form["age"]),
        "address": request.form["address"],                
        "doctorEmail": request.form["email"],
        "doctorName": request.form["name"],
        "createdOn": datetime.datetime.now()
    }

    dbHelper.collection = dbHelper.db["patients"]

    # Save Patient in DataBase i.e. MongoDB
    result = dbHelper.insert(patientData)
    message = "Patient Added Successfully"
    return message

@webApp.route("/fetch-patients")
def fetchPatientsFromDb():

    # Create a Dictionary with Data from HTML Register Form
    userData = {
        "doctorEmail": session["email"]
    }

    dbHelper.collection = dbHelper.db["patients"]
    # Fetch user in DataBase i.e. MongoDB
    result = dbHelper.fetch(query=userData)

    print("result:", result)

    if len(result)>0:
        print(result)
        return "Patients Fetched"
    else:
        return "Patients Not Found. Please Try Again"

def main():
    # In order to use Session Tracking, create a Secret Key
    webApp.secret_key = "doctors-app-key-v1"

    # it will run the app infinitly till user wont quite
    webApp.run()
    # webApp.run(port = 5001)  -> optionaly you can give the port number


if __name__ == "__main__":
    main()