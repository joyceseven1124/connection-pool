# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 19:00:13 2022

@author: 劉佳怡
"""

import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling

dbconfig = { 
    "host":"localhost",
    "port":3307,
    "database":"website",
    "user":"root",
    "password":"xu.6ru8u6"}

connection_pool = pooling.MySQLConnectionPool(pool_name = "test_pool",
    pool_size = 3,
    pool_reset_session = False,
    autocommit = True,
    **dbconfig
    )



def filt (input_username):
    connection_object = connection_pool.get_connection()
    cursor = connection_object.cursor()
    cursor.execute("SELECT * FROM member WHERE username= %s ",(input_username,)) 
    myresult = cursor.fetchone()
    connection_object.close()
    return myresult

def add(input_name,input_username,input_password):
    connection_object = connection_pool.get_connection()
    cursor = connection_object.cursor()
    cursor.execute("INSERT INTO member (name,username,password) VALUES(%s,%s,%s)",(input_name,input_username,input_password))
    connection_object.close()


def confirm(input_username,input_password):
    connection_object = connection_pool.get_connection()
    cursor = connection_object.cursor()
    cursor.execute("SELECT * FROM member WHERE username=%s ",(input_username,))
    myresult = cursor.fetchone()
    connection_object.close()
    
    if myresult != None:
        if myresult[2] == input_username and myresult[3] == input_password:
            return "correct"
        else:
            return "wrong"
    else: 
        return "wrong"
    
def message_content():
    connection_object = connection_pool.get_connection()
    cursor = connection_object.cursor()
    cursor.execute("SELECT member.name,message.content,message.time FROM member INNER JOIN message ON member.id = message.member_id  ORDER BY message.time DESC ")
    myresult = cursor.fetchall()
    connection_object.close()
    return myresult

def message_send(id,content):
    connection_object = connection_pool.get_connection()
    cursor = connection_object.cursor()
    cursor.execute("INSERT INTO message(member_id,content) VALUES(%s,%s)",(id,content))
    connection_object.close()
        
    
 


        

        

    





    
    

   


