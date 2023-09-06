import csv

def read_csv_file(filename):
    data = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            username, password, balance = row
            data.append({'username': username, 'password': password, 'balance': float(balance) })
    return data

filename = 'casino_data.csv'
user_data = read_csv_file(filename)

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
       


#Main casino program

user_name = input('Enter username: ')
verify_user(user_name, user_data)