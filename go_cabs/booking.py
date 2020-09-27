from dbconnect import DBHelper

#BOOKING A CAB IF ANY CAB'S ARE AVAILABLE
class Booking:
    def findDriver(self, sourcelat, sourcelon, destlat, destlon):
        print(sourcelat, sourcelon, destlat, destlon)
        cabList= DBHelper().getCab(sourcelat, sourcelon)
        if len(cabList) == 1:
            confirmation = int(input("We have found 1 cab. Press 1 to confirm booking : "))
            if confirmation == 1:
                print("Cab Driver {} is on his way to pick you up. Cab number is {}".format(cabList[0][1],cabList[0][2]))
                return {"driver_id": cabList[0][0]}
        else:
            print("No cabs are available")