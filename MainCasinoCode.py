#pulling user functionality from user_information.py
from user_information import UserInformation
from card_functions import CardFunctions
from blackjack_functionality import BlackJack

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
#testing
print(f'{username} with password {password} has a balance of ${balance}.')
balance = BlackJack.play_blackjack(balance)
print(balance)


