# data_base : list[tuple[str, str]] = [("qasim",'1234'),
#                                      ("sir zia", '12345'),
#                                     ]
# input_user : str = input("Enter user name")
# input_password : str = input("Enter user name")
# for row in data_base:
#     user, password = row
#     if input_user == user and input_password == password:
#         print("Valid User")
#         break
# else:
#     print("user not found or invalid user")
    



data_base_1 : list[tuple[str,str]] = [("Naveed sarwar",'1234'),
                                        ("Muhammad usman",'1234'),
                                          ]
input_user_1 : str =input("enter your user name")
input_pass_1 : str = input("enter your passowrd")
for row1 in data_base_1:
    user1, password1 = row1
    if input_user_1 == user1 and  input_pass_1  == password1:
        print("valid user")
        break
else: 
    print("invalid username/password")