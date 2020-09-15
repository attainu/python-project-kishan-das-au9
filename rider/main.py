from rider_info import RIDER
from driver_info import DRIVER

if __name__ == "__main__":    
    y= int(input("Are you a Rider or a Driver ? Type 1 for RIDER 2 for DRIVER :  "))
    if y == 1:
        RIDER()
    elif y==2:
        DRIVER()

