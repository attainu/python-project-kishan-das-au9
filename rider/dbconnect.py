# This file is used to initiate database connection

import mysql.connector as connector

class DBHelper:      
	def __init__(self):
		# initialization of connection
		self.con = connector.connect(host='localhost',username='root',password='root',port='3306',database='cab_booking')
		print('connected')

	# insert rider
	def insert_rider(self, user_name, password):
		# Insert query to add rider
		query = "insert into rider_info(rider_name, rider_password) values('{}','{}')".format(user_name,password)
		cur = self.con.cursor() 
		# Cursor class is an instance using which you can invoke methods that execute SQLite statements, fetch data from the result sets of the queries. You can create Cursor object using the cursor() method of the Connection object/class.
		cur.execute(query) 
		self.con.commit() # saving
		print("user_signed_up")

	def check_rider(self, user_name, password):
		# check rier in db
		query = "select * from rider_info where rider_name = '{}' and rider_password = '{}'".format(user_name,password)
		cur = self.con.cursor()
		cur.execute(query)
		rowcount = len(list(cur))
		self.con.commit()
		return rowcount


