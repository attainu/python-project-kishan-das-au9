from dbconnect import DBHelper
from location import DriverLocation
import pickle

class DRIVER:
    def __init__(self):
        while True:
            action = int(input("enter 1 for login and enter 2 for signup : "))
            user_name = input("ENTER YOUR USER_NAME : ")
            cab_no = input("ENTER YOUR CAB_NUMBER : ")
            password = input("ENTER YOUR PASSWORD : ")

            if action == 1:
                driver_info = DBHelper().check_driver(user_name,cab_no, password)
                if len(driver_info) == 1:
                    driver_dict = {}
                    driver_dict["driver_id"] = driver_info[0][0]
                    driver_dict["driver_name"] = driver_info[0][1]
                    driver_dict["cab_number"] = driver_info[0][2]
                    driver_dict["driver_password"] = driver_info[0][3]
                    driver_dict["isavailable"] = driver_info[0][4]
                    
                    driver_dict["lat"] = float(driver_info[0][5] or 0)
                    driver_dict["lon"] = float(driver_info[0][6] or 0)
                    
                    print("welcome", user_name,driver_dict)
                    pickle.dump(driver_dict,open("driver.dat","wb"))
                    while True:
                        print("ENTER YOUR PREFERENCE : ")
                        preference=int(input(" 1: Update Location \n 2: Update Availabiltiy \n 3: Exit\n " ))
                        if preference == 1:
                            DriverLocation()
                        elif preference == 2:
                            print("do you want to update your availability ? ")
                            isavailable = (input("Enter y to update and n to not : "))
                            if isavailable == "y":
                                
                                pref= int(input("Enter 1 if you are available and 0 if not : "))
                                driver_info = pickle.load(open("driver.dat","rb"))
                                if pref == 1:
                                    DBHelper().updateisavailable(driver_info["driver_id"],1)
                                else:
                                    DBHelper().updateisavailable(driver_info["driver_id"],0)
                        elif preference == 3:
                            break
                        else:
                            print("Invalid input")
                print(driver_info)
                break
            if action == 2:
                try:
                    DBHelper().insert_driver(user_name, cab_no, password)
                except Exception as e:
                    print("You've already signedup. Please login again")
                        
# DRIVER()                        