for i in range(3):
    ID = input("ENTER ID: ")
    if ID == "ADMIN111":
        for i in range(3):
            pswd = input("ENTER PASSWORD: ")
            if pswd == "NCERC111":
                print(
                    "LOGIN SUCCESSFUL\nYou have successfully signed into your account. You can close this window· "
                )
                break
            else:
                print("WRONG PASSWORD·\nTRY AGAIN!")
        else:
            print("TRY AFTER 60 SECONDS")

        break
    else:
        print("INCORRECT ID!")
else:
    print("TRY AFTER 60 SECONDS")
