from user_information import UserInformation

filename = 'casino_data.csv'
user_data = UserInformation.read_csv_file(filename)

#Main casino program
while True:
     new_username = input("Enter new user name or type exit to exit: ")
     if new_username.lower() == 'exit':
          break
     
     if new_username in user_data:
          print('Username already exists!')
    
     else:
          new_password = input('Enter password: ')
          UserInformation.add_user_to_database(filename, new_username, new_password)
          print(f'User added! Welcome to MGKasino 2.0, {new_username}!')
          user_data[new_username] = {'password': new_password, 'balance': 10000}
#user_name = input('Enter username: ')
#verify_user(user_name, user_data)