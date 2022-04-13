#from crypt import methods
#from crypt import methods
from cProfile import label
from enum import unique
from unicodedata import name
from ctypes.wintypes import MSG
from flask import Flask, render_template, request, url_for ,session 

import psycopg2
import psycopg2.extras

import os
import re
import secrets



app=Flask(__name__)

app.config['SECRET_KEY'] = 'clintoo678david0000'
conn=psycopg2.connect("dbname='duka' user='postgres' host='localhost' password='5132'")

@app.route('/')


@app.route("/index", methods=['GET','POST']) 
def index():
    if request.method=='post' and 'name'in request.form and 'subject' in request.form and 'email' in request.form and 'message' in request.form:
       cur=conn.cursor()

       name=request.form['name']
       subject=request.form['subject']
       email=request.form['email']
       message=request.form['message']

       rows=[name,subject,email,message]
       quary=("INSERT INTO public.accounts( name, subject, email, message)VALUES ( %s, %s, %s, %s)")
       cur.execute(rows,quary)

       conn.commit()

    return render_template ('index.html' , )
    


app.run(debug=True)