import os
import pymysql
from flask import Flask, render_template,request,flash, jsonify
import json
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key= "secret_word"
app.config['IMAGE_UPLOADS'] = "static/uploads/images"
# username = os.getenv('C9_USER')

# ----For connectionto pymysql database---?
# # Connect to the database

connection = pymysql.connect(host='my-database-class.crgear1afurv.ca-central-1.rds.amazonaws.com',
                             user='root',
                             password='12345678',
                             db='Cookshack')
                             


# connection = pymysql.connect(host='localhost',
#                              user=username,
#                              password='',
#                              db='Cookshack')




@app.route("/")
def index():
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = """SELECT Recipes.Images, Users.User_name, Recipes.Recipe_name,Allergens.Allergen_name, Categories.Category_name, WorldCuisine.WorldCuisine_name FROM Recipes 
            	INNER JOIN Users ON Users.User_ID = Recipes.User_ID INNER JOIN Allergens ON Allergens.Allergen_ID = Recipes.Allergen_ID 
            	INNER JOIN Categories ON Categories.Category_ID = Recipes.Category_ID 
            	INNER JOIN WorldCuisine ON Recipes.WorldCuisine_ID = WorldCuisine.WorldCuisine_ID;"""
            cursor.execute(sql)
            list_of_recipes = []
            for item in cursor:
                list_of_recipes.append(item)
            print(list_of_recipes, "list_of_recipes")
    return render_template("index.html", recipe_data = list_of_recipes)
    
@app.route("/addrecipe",  methods=["GET", "POST"])
def addrecipe():
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = """SELECT Recipes.Images, Users.User_name, Recipes.Recipe_name,Allergens.Allergen_name, Categories.Category_name, WorldCuisine.WorldCuisine_name FROM Recipes 
            	INNER JOIN Users ON Users.User_ID = Recipes.User_ID INNER JOIN Allergens ON Allergens.Allergen_ID = Recipes.Allergen_ID 
            	INNER JOIN Categories ON Categories.Category_ID = Recipes.Category_ID 
            	INNER JOIN WorldCuisine ON Recipes.WorldCuisine_ID = WorldCuisine.WorldCuisine_ID limit 3;"""
            cursor.execute(sql)
            list_of_recipes = []
            for item in cursor:
                list_of_recipes.append(item)
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
            print(request.form['ingredients'], "ingredien")
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                sql = """ SELECT MAX(User_ID) FROM Users"""
                cursor.execute(sql)
                result = cursor.fetchall()
                last_insert_id = result[0]['MAX(User_ID)']
                image  = request.files['picture']
                image.save(os.path.join(app.config['IMAGE_UPLOADS'], image.filename))
                print(image.filename)
                sqlinsert = """INSERT INTO Recipes 
                ( Recipe_name, Ingredients,Instructions,Category_ID, 
                WorldCuisine_ID, User_ID, Allergen_ID, Images) 
                VALUES ('{}', '{}', '{}', {}, {}, {}, {},'{}');""".format(request.form['recipe'],
                request.form['ingredients'],request.form['instructions'], 
                request.form['mealtype'], request.form['cuisinetype'],
                last_insert_id,request.form['allergen'],image.filename)
                
                
                cursor.execute(sqlinsert)
                connection.commit()
    return render_template("addrecipe.html", recipe_data = list_of_recipes)
                                 

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/recipe/<name>")
def about_recipe(name):
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = """SELECT Users.User_name, Recipes.Ingredients,Recipes.Instructions,
                Recipes.Recipe_name,Recipes.Images, Allergens.Allergen_name, Categories.Category_name, WorldCuisine.WorldCuisine_name FROM Recipes 
            	INNER JOIN Users ON Users.User_ID = Recipes.User_ID INNER JOIN Allergens ON Allergens.Allergen_ID = Recipes.Allergen_ID 
            	INNER JOIN Categories ON Categories.Category_ID = Recipes.Category_ID 
            	INNER JOIN WorldCuisine ON Recipes.WorldCuisine_ID = WorldCuisine.WorldCuisine_ID
            	WHERE Recipes.Recipe_name = '{}';""".format(name)
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result, "list_of_recipes")
    return render_template("about.html", recipe = result)
    
if __name__=="__main__":
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True) 
            




















# mail server-DO NOT DELETE-----

# https://myaccount.google.com/lesssecureapps

# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT']= 465
# app.config['MAIL_USERNAME'] = 'digitalclickmultiplier@gmail.com'
# app.config['MAIL_PASSWORD'] = ''
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
 
#  -----------------serpate code dont use together-->
 # commit command need cause you are changing some data in pipline python3 my_db.py
        # finally:
        #     connection.close()  
# -------mail----DO NOT DELETE---



