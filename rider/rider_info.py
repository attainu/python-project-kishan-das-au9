from dbconnect import DBHelper
from location import RiderLocation,Destination
class RIDER:
    def __init__(self):
        while True:
            x = int(input("enter 1 for login and enter 2 for signup : "))
            if x !=1  and x != 2:
                print("enter valid input")

            else:
                try:
                    user_name = input("Enter user_name : ")
                    password = input("Enter password : ")
                    if x == 1:
                        count = DBHelper().check_rider(user_name,password)
                        if count == 1:
                            print("welcome", user_name)
                            RiderLocation()  
                            Destination()
                            break
                        else:
                            print("invalid user_name or password")          
                    if x == 2:
                        DBHelper().insert_rider(user_name,password)
                        print("welcome", user_name)
                        RiderLocation()
                        Destination()
                        break

                except Exception as e:
                    print('Please try again an error{} has occured. Please login again'.format(e))
                    break
                    

RIDER()