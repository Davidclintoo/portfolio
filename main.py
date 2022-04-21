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
#conn=psycopg2.connect("dbname='duka' user='postgres' host='localhost' password='5132'")
conn=psycopg2.connect("dbname='d1m8odf2nbe0jt' user='idlxsyofckzrsu' port='5432 ' host='ec2-52-30-133-191.eu-west-1.compute.amazonaws.com' password='377cc0aab4454edd009635c4786b072f4e75ef0d07fc222ff7020a6c6d950a4a'")


@app.route('/')


@app.route("/index", methods=['GET','POST']) 
def index():
    ms=''
    if request.method=='post'  :
       cur=conn.cursor()

       name=request.form['name']
       subject=request.form['subject']
       email=request.form['email']
       message=request.form['message']

       rows=[name,subject,email,message]
       quary=("INSERT INTO accounts( name, subject, email, message) VALUES( %s, %s, %s, %s)")
       cur.execute(rows,quary)

       conn.commit()
      
      
          
    return render_template ('index.html' , ms=ms )
    

if __name__ == '__main__':
   app.run(debug=True)