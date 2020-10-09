from dbconnect import DBHelper
from location import RiderLocation
import pickle


class RIDER:
    def __init__(self):
        while True:
            action = int(
                input("\nEnter 1 for login and Enter 2 for signup : "))
            user_name = input("ENTER YOUR USER_NAME : ")
            password = input("ENTER YOUR PASSWORD : ")
            if action == 1:
                rider_info = DBHelper().check_rider(user_name, password)
                if len(rider_info) == 1:
                    driver_dict = {}
                    driver_dict["rider_id"] = rider_info[0][0]
                    driver_dict["rider_name"] = rider_info[0][1]
                    driver_dict["rider_password"] = rider_info[0][2]

                    print("\nwelcome", user_name, driver_dict)
                    pickle.dump(driver_dict, open("rider.dat", "wb"))
                    first_menu = "1. Book a ride"
                    insertObj = {}
                    while True:
                        print("\nENTER YOUR PREFERENCE : ")
                        preference = int(
                            input(" {} \n 2: History \n 3: Exit\n ".format(first_menu)))
                        if preference == 1:
                            status = RiderLocation().getSourceLocation()
                            print(status)
                            if status:
                                first_menu = "4. End a ride"
                                # get riderid from rider.dat

                                rider_info = pickle.load(
                                    open("rider.dat", "rb"))
                                # rider_id=rider_info["rider_id"]
                                insertObj["rider_id"] = rider_info["rider_id"]
                                insertObj["driver_id"] = status["driver_id"]
                                insertObj["source"] = status["source"]
                                insertObj["destination"] = status["destination"]
                            else:
                                first_menu = "1. Book a ride"
                        elif preference == 4 and insertObj["source"]:
                            # End The ride
                            DBHelper().addHistory(insertObj)
                            insertObj = {}
                            print("history")
                        elif preference == 2:
                            # History query call
                            rider_info = pickle.load(open("rider.dat", "rb"))
                            history = DBHelper().getHistory(
                                rider_info["rider_id"])
                            print(history)
                        elif preference == 3:
                            break
                        else:
                            print("Invalid input")
                print(rider_info)
                break
            if action == 2:
                try:
                    DBHelper().insert_rider(user_name, password)
                except Exception as e:
                    print("You've already signedup. Please login again")


# RIDER()
