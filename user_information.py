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
    
    
    def add_user_to_database(filename, new_username, new_password):
        with open(filename, 'a', newline = '\n') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([new_username, new_password, 10000])
    
    def get_balance(username, user_data):
        return user_data[username]['balance']
    
    def set_balance(username,password, user_data, amount):
        user_data[username]['balance'] = amount
        with open(filename, 'w', newline = '\n') as file:
            csv_writer = csv.writer(file)
            for user, data in user_data.items():
                csv_writer.writerow([user, data['password'], data['balance']])
                
    def get_password(username, user_data):
        return user_data[username]['balance']




    def verify_user(user_name, user_data):
        for user in user_data:
            valid_user = False
            if user['username'] == str(user_name):
                valid_user = True
                break

        if valid_user == True:
                print('Valid user!')
                return
            
        print('Invalid user')

filename = 'casino_data.csv'
user_data = UserInformation.read_csv_file(filename)