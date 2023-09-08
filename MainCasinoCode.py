#pulling user functions from user_information.py
from user_information import UserInformation

#creating filename variable to use read_csv file function to create hash of current users, passwords, and balances(user data)
filename = 'casino_data.csv'
user_data = UserInformation.read_csv_file(filename)

#Making user login/create user profile before allowing access to casino
verified_user = False
while verified_user == False:
     username = input("Enter username, or new user type desired username to create new account. Type exit to exit ").lower()
     
     if username.lower() == 'exit':
          verified_user = True
          break
     
     if username in user_data:
          password = input(f"Please enter password for {username}: ")
          pw_check = UserInformation.get_password(username, user_data)
          if password == pw_check:
               balance = UserInformation.get_balance(username, user_data)
               print(f'Welcome back, {username}! Your balance is {balance}.')
               verified_user = True
          else:
               print('Invalid password. Please try again')
               break
    
     else:
          password = input('Enter desired password: ')
          pw_check = input('Please re-enter password: ')
          while password != pw_check:
               password = input('Passwords do not match. Re-enter password')
               pw_check = input('Enter password again')
          UserInformation.add_user_to_database(filename, username, password)
          print(f'User added! Welcome to MGKasino 2.0, {username}!')
          user_data[username] = {'password': password, 'balance': 10000}
          verified_user = True


#user_name = input('Enter username: ')
#verify_user(user_name, user_data)