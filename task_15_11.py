name = "admin"
password = "wel@1234"
user_name = input("enter the username:")
password_input = input("enter the password:")
if user_name == " " and password_input == " ":
    print("login is invalid or empty")
elif user_name == name:
    print("user name is correct")
    if password_input == password:
        print("password is valid")
else:
    print("user name is invalid")
    

