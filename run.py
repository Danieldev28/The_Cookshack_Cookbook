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
        if request.form["btn"] == "Sign in":
            # insert command!
             with connection.cursor() as cursor:
                sql = """INSERT INTO Users
                ( User_name,Dateofbirth,Email,Country) 
                VALUES ('{}', '{}', '{}', '{}');""".format(request.form['name'],
                request.form['DOB'],request.form['email'],request.form['country'])
                cursor.execute(sql)
                connection.commit()
                flash("Thanks {} , for submitting your information".format
                (request.form["name"]))
        else:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                sql = """ SELECT MAX(User_ID) FROM Users"""
                cursor.execute(sql)
                result = cursor.fetchall()
                last_insert_id = result[0]['MAX(User_ID)']
                
                sqlinsert = """INSERT INTO Recipes 
                ( Recipe_name, Ingredients,Instructions,Category_ID, 
                WorlCuidine_ID, User_ID, Allergen_ID) 
                VALUES ('{}', '{}', '{}', {}, {}, {}, {});""".format(request.form['recipe'],
                request.form['ingredients'],request.form['instructions'], 
                request.form['mealtype'],request.form['cuisinetype'], 
                last_insert_id,request.form['allergen'])
           
                cursor.execute(sqlinsert)
                connection.commit()
    return render_template("addrecipe.html")
            # commit command need cause you are changing some data in pipline python3 my_db.py
        # finally:
        #     connection.close()                        

    
    

# @app.route("/register")
# def register():
#     return render_template("register.html")



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



