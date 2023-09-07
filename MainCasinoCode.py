#pulling user functions from user_information.py
from user_information import UserInformation

#creating filename variable to use read_csv file function to create hash of current users, passwords, and balances(user data)
filename = 'casino_data.csv'
user_data = UserInformation.read_csv_file(filename)

#Making user login/create user profile before allowing access to casino
verified_user = False
while verified_user == False:
     new_username = input("Enter new user name or type exit to exit: ").lower()
     if new_username.lower() == 'exit':
          verified_user = True
          break
     
     if new_username in user_data:
          print('Username already exists!')
    
     else:
          new_password = input('Enter password: ')
          UserInformation.add_user_to_database(filename, new_username, new_password)
          print(f'User added! Welcome to MGKasino 2.0, {new_username}!')
          user_data[new_username] = {'password': new_password, 'balance': 10000}
          verified_user = True


#user_name = input('Enter username: ')
#verify_user(user_name, user_data)