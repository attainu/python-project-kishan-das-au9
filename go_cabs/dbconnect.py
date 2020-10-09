# This file is used to initiate database connection

import mysql.connector as connector


class DBHelper:
    def __init__(self):
        # initialization of connection
        self.con = connector.connect(
            host='localhost', username='root', password='root', port='3306', database='cab_booking')
        print('connected')

# INSERT RIDER
    def insert_rider(self, user_name, password):
        # Insert query to add rider
        query = "insert into rider_info(rider_name, rider_password) values('{}','{}')".format(
            user_name, password)
        cur = self.con.cursor()
        # Cursor class is an instance using which you can invoke methods that execute SQLite statements,
        # fetch data from the result sets of the queries.
        #  You can create Cursor object using the cursor() method of the Connection object/class.
        cur.execute(query)
        self.con.commit()  # saving
# CHECK RIDER

    def check_rider(self, user_name, password):
        # check rier in db
        query = "select * from rider_info where rider_name = '{}' and rider_password = '{}'".format(
            user_name, password)
        cur = self.con.cursor()
        cur.execute(query)
        info = list(cur)
        self.con.commit()
        return info
# BOOKING A CAB

    def getCab(self, lat, lon):
        query = "SELECT *, SQRT(POW(2,({}-lat)) + POW(2,({}-lon))) as distance from cab_booking.driver_info where isavailable = 1 having distance < 3 order by distance limit 1".format(lat, lon)

        cur = self.con.cursor()
        cur.execute(query)
        cabInfo = list(cur)
        self.con.commit()
        return cabInfo

# ADDING RIDER HISTORY
    def addHistory(self, insertObj):
        query = "Insert into history(rider_id, driver_id, source, destination) values({},{},'{}','{}')".format(
            insertObj["rider_id"], insertObj["driver_id"], insertObj["source"], insertObj["destination"])
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
# GETTING RIDER HISTORY

    def getHistory(self, rider_id):
        query = "Select driver_info.driver_name, driver_info.cab_number, history.source, history.destination from history join driver_info on history.driver_id = driver_info.driver_id where history.rider_id = {}".format(
            rider_id)

        cur = self.con.cursor(dictionary=True)
        cur.execute(query)
        historyList = list(cur)
        self.con.commit()
        return historyList


# INSERT DRIVER

    def insert_driver(self, user_name, cab_no, password):
        # Insert query to add driver
        query = "insert into driver_info(driver_name, cab_number, driver_password) values('{}','{}','{}')".format(
            user_name, cab_no, password)
        cur = self.con.cursor()
        # Cursor class is an instance using which you can invoke methods that execute SQLite statements,
        # fetch data from the result sets of the queries.
        #  You can create Cursor object using the cursor() method of the Connection object/class.
        cur.execute(query)
        self.con.commit()
# CHECK DRIVER

    def check_driver(self, user_name, cab_no, password):
        # check rier in db
        query = "select * from driver_info where driver_name = '{}' and cab_number = '{}' and driver_password = '{}'".format(
            user_name, cab_no, password)
        cur = self.con.cursor()
        cur.execute(query)
        info = list(cur)
        self.con.commit()
        return info
# UPDATING THE DRIVER'S LOCATION

    def update_driverLocation(self, id, lat, lon):
        # update location
        query = "UPDATE driver_info SET lat = {}, lon = {} WHERE driver_id = {}".format(
            lat, lon, id)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
# UPDATING THE DRIVER'S AVAILABILITY

    def updateisavailable(self, id, isavailable):
        # update location
        query = "UPDATE driver_info SET isavailable = {} WHERE driver_id = {}".format(
            isavailable, id)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
