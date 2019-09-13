import os
import pymysql
from flask import Flask, render_template,request,flash, jsonify
import json
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key= "secret_word"

# ----For connectionto pymysql database---?
username = os.getenv('C9_USER')
# # Connect to the database

connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Cookshack')


@app.route("/")
def index():
   return render_template("index.html")
    
@app.route("/addrecipe",  methods=["GET", "POST"])
def addrecipe():
    if request.method == 'POST':
         print("Hello is there anybody there!")  
         print(request.form['name'])
         print(request.form['country'])
         print(request.form['DOB'])
         print(request.form['email'])
         print(request.form['CuisineType'])
         try:
            # Run a query
            with connection.cursor() as cursor:
                sql = "SELECT * FROM WorldCuisine;"
                cursor.execute(sql)
                result = cursor.fetchall()
                print(result)
         finally:
         # Close the connection, regardless of whether or not the above was successful
            connection.close()
    return render_template("addrecipe.html", page_title="addrecipe")

@app.route("/register")
def register():
    return render_template("register.html")



if __name__=="__main__":
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True) 
            
# mail server-DO NOT DELETE-----

# https://myaccount.google.com/lesssecureapps

# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT']= 465
# app.config['MAIL_USERNAME'] = 'digitalclickmultiplier@gmail.com'
# app.config['MAIL_PASSWORD'] = 'Dan8pzh4p27'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
# app.config['MAIL_DEFAULT_SENDER'] ='digitalclickmultiplier@gmail.com.com'
# mail = Mail(app)




# @app.route("/")
# def index():
#     msg = Message('Mail test', recipients = ['digitalclickmultiplier@gmail.com'])
#     msg.body ="This is a mail testing email"
#     # msg.html =
#     mail.send(msg)
#     return "Sent"
#     # render_template("index.html")
# -------mail----DO NOT DELETE---



