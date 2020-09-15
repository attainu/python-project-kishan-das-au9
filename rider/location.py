from dbconnect import DBHelper
import requests
from geopy.geocoders import Nominatim
import pickle

class RiderLocation:
    def __init__(self):
        # self.location=[]
        while True:
            locInput = int(input("For Current Location enter 1, or enter 2 for adding your pick up location : "))
            if locInput == 1:
                res = requests.get('http://ipinfo.io/')
                data = res.json()
                print(list(map(float,data["loc"].split(','))))
                break
            elif locInput == 2:
                pickupLoc = input("Enter pickup location : ")
                geolocator = Nominatim(user_agent='myapplication')
                location = geolocator.geocode(pickupLoc)
                if location:
                    
                    res = []
                    res.append(round(float(location.raw["lat"]),5))
                    res.append(round(float(location.raw["lon"]),5))
                    
                    print(res)
                    break
                else:
                    print("Invalid Pickup location")


class Destination:
    def __init__(self):
        Dest = input("Enter destination : ")
        geolocator = Nominatim(user_agent='myapplication')
        destination = geolocator.geocode(Dest)
        if destination:
            
            res = []
            res.append(round(float(destination.raw["lat"]),5))
            res.append(round(float(destination.raw["lon"]),5))
            
            print(res)
            # print(res[0]+res[1])                      
        else:
            print("Invalid Pickup location")

class DriverLocation:
    def __init__(self):
        driver_info = pickle.load(open("driver.dat","rb"))
        Dest = input("Enter CAB_LOCATION : ")
        geolocator = Nominatim(user_agent='myapplication')
        destination = geolocator.geocode(Dest)
        if destination:
            try:
                id = driver_info["driver_id"]
                lat = float(destination.raw["lat"])
                lon = float(destination.raw["lon"])
                DBHelper().update_driverLocation(id,lat,lon)

            except Exception as e:
                print('Location error {}'.format(e))
                                 
        else:
            print("Invalid Pickup location")







