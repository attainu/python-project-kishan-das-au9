from dbconnect import DBHelper
import requests
from geopy.geocoders import Nominatim
import pickle
from booking import Booking


class RiderLocation:
    def getSourceLocation(self):
        # self.location=[]
        while True:
            locInput = int(input("For Current Location enter 1 : "))
            if locInput == 1:
                res = requests.get('http://ipinfo.io/')
                data = res.json()
                curLocList = list(map(float, data["loc"].split(',')))
                destLocList = self.getDestination()
                geolocator = Nominatim(user_agent='myapplication')
                location = geolocator.reverse(
                    "{},{}".format(curLocList[0], curLocList[1]))
                status = Booking().findDriver(
                    curLocList[0], curLocList[1], destLocList["loc"][0], destLocList["loc"][1])
                status["source"] = location
                status["destination"] = destLocList["destination_name"]
                return status
            elif locInput == 2:
                pickupLoc = input("Enter pickup location : ")
                geolocator = Nominatim(user_agent='myapplication')
                location = geolocator.geocode(pickupLoc)
                if location:
                    curLocList = [float(location.raw["lat"]),
                                  float(location.raw["lon"])]
                    destLocList = self.getDestination()
                    status = Booking().findDriver(
                        curLocList[0], curLocList[1], destLocList["loc"][0], destLocList["loc"][1])
                    return status
                else:
                    print("Invalid Pickup location")

    def getDestination(self):
        dest = input("Enter destination : ")
        geolocator = Nominatim(user_agent='myapplication')
        destination = geolocator.geocode(dest)
        if destination:
            res = [float(destination.raw["lat"]),
                   float(destination.raw["lon"])]
            destObj = {"loc": res, "destination_name": dest}
            return destObj
            # print(res[0]+res[1])
        else:
            print("Invalid Pickup location")

# RiderLocation().getSourceLocation()


class DriverLocation:
    def __init__(self):
        driver_info = pickle.load(open("driver.dat", "rb"))
        Dest = input("Enter CAB_LOCATION : ")
        geolocator = Nominatim(user_agent='myapplication')
        destination = geolocator.geocode(Dest)
        if destination:
            try:
                id = driver_info["driver_id"]
                lat = float(destination.raw["lat"])
                lon = float(destination.raw["lon"])
                DBHelper().update_driverLocation(id, lat, lon)

            except Exception as e:
                print('Location error {}'.format(e))

        else:
            print("Invalid Pickup location")
