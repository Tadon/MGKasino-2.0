#pulling user functions from user_information.py
from user_information import UserInformation

#required variables
filename = 'casino_data.csv'
user_data = UserInformation.read_csv_file(filename)
username = ''
password = ''
balance = 0

#Gathering username, balance, and password so we can game!

while username == '':
     username = UserInformation.user_verification(user_data)
     balance = UserInformation.get_balance(username, user_data)
     password = UserInformation.get_password(username, user_data)

print(f'{username} with password {password} has a balance of ${balance}.')