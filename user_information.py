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

