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

#create the object of flask
# which represent a web application
 
webApp = Flask("PATIENT MANAGEMENT SYSTEM: ")

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



def main():
    # it will run the app infinitly till user wont quite
    webApp.run()
    # webApp.run(port = 5001)  -> optionaly you can give the port number


if __name__ == "__main__":
    main()