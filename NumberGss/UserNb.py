from UserManNb import User_manager
from GameNb import NumberGuessingGame
from ScoreNb import Score

class User:
    def __init__(self, username=None, password=None, score_file=None, user_data=None):
        self.username = username
        self.password = password
        self.score_file = score_file
        self.user_data = user_data

    def menu(self):
        print('\nWelcome to Number Guessing Game! : )')
        print('1. Register')
        print('2. Log in')
        print('3. Exit')

        choice = input('Enter Choice: ')

        if choice == '1':
            self.register()
        elif choice == '2':
            self.login()
        elif choice == '3':
            quit()

    def register(self):
        username = input('Enter Username: ')
        password = input('Enter Password: ')

        users = User_manager.load_users()

        while True:
            if not User_manager.val_user(username, users) or not User_manager.val_pass(password):
                username = input('Enter Username: ')
                password = input('Enter Password: ')
                continue

            users[username] = password
            User_manager.save_users(users)
            print('Success!\n')
            self.menu()
            break
    
    def login(self):
        users = User_manager.load_users()
        while True:
            username = input('Enter Username: ')
            password = input('Enter Password: ')

            if username in users and users[username] == password:
                print('Login Successful!.\n')
                self.game_menu(username)
                break
            else:
                print('Incorrect username or password. Try again\n')

    def game_menu(self, username):
        game = NumberGuessingGame()
        while True:
            print(f'\nWelcome {username}')
            print('1. Play Game')
            print('2. View Leaderboards')
            print('3. Log out')

            choice = int(input('Enter Choice: '))
            if choice == 1:
                game.play_game(username)
            elif choice == 2:
                Score.display_leaderboards()
            elif choice == 3:
                self.menu()


