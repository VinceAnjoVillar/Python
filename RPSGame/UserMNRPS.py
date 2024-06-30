import os

class User_Manager:
    @staticmethod
    def create_file():
        if os.path.exists('User_Data.txt'):
            with open('User_Data.txt', 'w') as file:
                pass

    @staticmethod
    def load_users():
        try:
            with open('User_Data.txt', 'r') as file:
                lines = file.readlines()

            users = {}
            for line in lines:
                data = line.strip().split(',')
                if len(data) == 2:
                    username, password = data
                    users[username] = (password)
                else:
                    return False
            return users
        
        except FileNotFoundError:
            print('User File not found')
            return {}
    
    @staticmethod
    def save_users(users):
        with open('User_Data.txt', 'w') as file:
            for username, password in users.items():
                file.write(f'{username},{password}\n')

    @staticmethod
    def validate_username(username, users):
        if username in users:
            print('Username alread exists\n')
            return False
        if len(username) < 4:
            print('Username must be at least 4 characters long.\n')
        return True
    
    @staticmethod
    def validate_password(password):
        if len(password) < 6:
            print('Password must be at least 6 characters long.\n')
        return True