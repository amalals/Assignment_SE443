import requests

# Get: 
# First 3:
# List users
# Single user
# Single user not found
# Post:
# Create
# Register successful 
# Register unsuccessful

# Here below we have the GET Requests with 

list_user = requests.get('https://reqres.in/api/users?page=2')
# print(str(list_user.status_code) + "\nThe Response is Successful")
single_user = requests.get('https://reqres.in/api/users/2')
# print(str(single_user.status_code) + "\nThe Response is Successful")
single_user_not_found = requests.get('https://reqres.in/api/users/23')
# print(str(single_user_not_found.status_code) + "\nThe Response is 404 Not Found")

# Here below we have the POST Requests with same mentioned data in reqres.in


create = requests.post('https://reqres.in/api/users', data={
    "name": "morpheus",
    "job": "leader"
})

# print(str(create.status_code) + "  The request has succeeded & the requested resource has been created")

register_successful = requests.post('https://reqres.in/api/register', data= {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
})
# print(str(register_successful.status_code) + "  The request has succeeded")

register_unsuccessful = requests.post('https://reqres.in/api/register', data={
    "email": "sydney@fife"
})

# print(str(register_unsuccessful.status_code) + " Bad Request")


choice = (int(input("Please enter the requests statuses You want to check: \nPress 1 for GET & 2 for POST: ")))

if choice == 1:
    Get_input = int(input("Please enter the whcih request's status you want to get: Press 1 for List User, 2 for Single User, 3 for Single User not found \n"))
    if Get_input == 1:
        print("\nThe Response is \n")
        print(str(list_user.status_code) + "\nThe Response is Successful")
    elif Get_input == 2:
        print("\nThe Response is \n")
        print(str(single_user.status_code) + "\nThe Response is Successful")
    elif Get_input == 3:
        print("\nThe Response is \n")
        print(str(single_user_not_found.status_code) + "\nThe Response is 404 Not Found")
    else:
        print('You have entered wrong input please try again ')

elif choice == 2:
    Get_input = int(input("Please enter the whcih request's status you want to get: \nPress 1 for Create, 2 Register Successful, 3 for Register Unsuccessful \n"))
    print("")
    if Get_input == 1:
        print("\nThe Response is \n")
        print(str(create.status_code) + "  The request has succeeded & the requested resource has been created")
    elif Get_input == 2:
        print("\nThe Response is \n")
        print(str(register_successful.status_code) + "  The request has succeeded")
    elif Get_input == 3:
        print("\nThe Response is \n")
        print(str(register_unsuccessful.status_code) + " Bad Request")
    else:
        print('You have entered wrong input please try again ')
else:
    print('You have entered wrong input please try again ')