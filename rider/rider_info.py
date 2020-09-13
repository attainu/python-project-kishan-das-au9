from dbconnect import DBHelper


def main():
    x = int(input("enter 1 for login and enter 2 for signup"))
    if x !=1  and x != 2:
        print("enter valid input")

    else:
        user_name = input("Enter user_name : ")
        password = input("Enter password : ")
        if x == 1:
            count = DBHelper().check_rider(user_name,password)
            if count == 1:
                print("welcome", user_name)
            else:
                print("FOFF")          
        if x == 2:
            DBHelper().insert_rider(user_name,password)

if __name__ == "__main__":
    main()

