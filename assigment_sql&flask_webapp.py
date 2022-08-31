# -*- coding: utf-8 -*-


from flask import Flask,request
import sqlite3

try:
    connec = sqlite3.connect("access_details.db")
    cur = connec.cursor()
    cur.execute("""
            CREATE TABLE IF NOT EXISTS user_account_info(
            id text,
            password text)""")
    cur.execute("""
            CREATE TABLE IF NOT EXISTS user_profile_info(
            user_name text,
            city text,
            country text,
            pin_code text,
            age text)""")
except:
    print("Incorrect format! kindly,enter the correct format")
finally:
    cur.close()
    connec.close()
    

app = Flask(__name__)

@app.route('/register', methods = ['POST']) ## Post method used to take value from front-end
def register():
    try:
        user = request.get_json() ## getting an input from front-end i.e. user in Jason format
        connec = sqlite3.connect("access_details.db")
        cur = connec.cursor()
        cur.execute("INSERT INTO user_account_info values ('{}','{}')".format(user['id'],user['password']))
        connec.commit() ## saving the changes into database
        return "Your user account created successfully!!!"
    except:
        return " Incorrect..!!Kindly, enter correct format"
    finally:
        cur.close()
        connec.close()
        

@app.route('/Profile-info',methods = ['POST'])
def profileInfo():
    try:
        user = request.get_json() ## getting an input from front-end i.e. user in Jason format
        connec = sqlite3.connect("access_details.db")
        cur = connec.cursor()
        cur.execute("INSERT INTO user_profile_info values ('{}','{}','{}','{}','{}')".format(user['user_name'],user['city'],user['country'],user['pin_code'],user['age']))
        connec.commit() ## saving the changes into database
        return "Your profile created successfully!!!"
    except:
        return " Incorrect..!!Kindly, enter correct format"
    finally:
        cur.close()
        connec.close()
        

@app.route('/update',methods = ['POST'])
def update():
    try:
        user = request.get_json() ## getting an input from front-end i.e. user in Jason format
        connec = sqlite3.connect("access_details.db")
        cur = connec.cursor()
        cur.execute("UPDATE user_account_info SET password='{}' WHERE id='{}'".format(user['password'],user['id']))
        connec.commit() ## saving the changes into database
        return "Password changed successfully!!!"
    except:
        return " Incorrect..!!Kindly, enter correct format"
    finally:
        cur.close()
        connec.close()
        
        
@app.route('/delete',methods = ['POST'])
def delete():
    try:
        user = request.get_json() ## getting an input from front-end i.e. user in Jason format
        connec = sqlite3.connect("access_details.db")
        cur = connec.cursor()
        cur.execute("DELETE FROM user_profile_info WHERE id='{}' IN city ='{}'".format(user['id'],user['city']))
        connec.commit() ## saving the changes into database
        return "Change made in the database successfully!!!"
    except:
        return " Incorrect..!!Kindly, enter correct format"
    finally:
        cur.close()
        connec.close()
        
        
@app.route('/display')
def display():
    try:
        connec = sqlite3.connect("access_details.db")
        cur = connec.cursor()
        return {"user's details": list(cur.execute("SELECT id, user_name, city, country, age, pin_code FROM user_account_info,user_profile_info"))}
    except:
        return " Incorrect..!!Kindly, enter correct database name"
    finally:
        cur.close()
        connec.close()


app.run(port=5001)
