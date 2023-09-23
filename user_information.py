import csv

class UserInformation:
    def read_csv_file(filename):
        data = {}
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                username, password, balance = row
                data[username] = {'password': password, 'balance': float(balance)}
        return data
    
    #adding new userbase to csv and user_data dictionary
    def add_user_to_database(filename, new_username, new_password):
        with open(filename, 'a', newline = '\n') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([new_username, new_password, 10000])

    #getting balance for specified user
    def get_balance(username, user_data):
        return user_data[username]['balance']
    
    #changing balance
    def change_balance(username,password, user_data, amount):
        user_data[username]['balance'] = amount
        with open(filename, 'r') as file:
             data = list(csv.reader(file))

        for i, row in enumerate(data):
             if row[0] == username:
                  data[i][2] = str(amount)

        with open(filename, 'w', newline = '\n') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data)
            
    #returning balance for specified username
    def get_password(username, user_data):
        return user_data[username]['password']
    
    #changing password for specified username
    def change_password(username, balance, user_data, new_password):
        user_data[username]['password'] = new_password
        with open(filename, 'w', newline = '\n') as file:
            csv_writer = csv.writer(file)
            for user, data in user_data.items():
                csv_writer.writerow([user, data['password'], data['balance']])

    #method to get or create user from login
    def user_verification(user_data):
        not_verified = True
        while not_verified == True:
            username = input("Enter username, or new user type desired username to create new account. Type exit to exit ").lower()
            
            if username.lower() == '':
                 print('Invalid username. Username cannot be empty')
                 break
            
            if username.lower() == 'exit':
                not_verified = False
                break
            
            if username in user_data:
                password = input(f"Please enter password for {username}: ")
                pw_check = UserInformation.get_password(username, user_data)
                if password == pw_check:
                        balance = UserInformation.get_balance(username, user_data)
                        print(f'Welcome back, {username}! Your balance is {balance}.')
                        not_verified = False
                        return username
                        
                else:
                        print('Invalid password. Please try again')
                                
            else:
                password = input('Enter desired password: ')
                pw_check = input('Please re-enter password: ')
                while password != pw_check:
                        password = input('Passwords do not match. Re-enter password: ')
                        pw_check = input('Enter password again: ')
                UserInformation.add_user_to_database(filename, username, password)
                print(f'User added! Welcome to MGKasino 2.0, {username}!')
                user_data[username] = {'password': password, 'balance': 10000}
                not_verified = False
                return username

filename = 'casino_data.csv'
user_data = UserInformation.read_csv_file(filename)