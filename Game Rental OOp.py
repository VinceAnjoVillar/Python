class Game:
    def __init__(self, name, quantity, cost):
        self.name = name
        self.quantity = quantity
        self.cost = cost

    def __str__(self):
        return f"{self.name}: Quantity - {self.quantity}, Cost - {self.cost}"
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0
        self.points = 0
        self.inventory = []

    def __str__(self):
        return f"Username: {self.username}, Balance: {self.balance}, Points: {self.points}, Inventory: {self.inventory}"
class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def update_game(self, game, quantity=None, cost=None):
        if quantity is not None:
            game.quantity = quantity
        if cost is not None:
            game.cost = cost
class GameRentalSystem:
    def __init__(self):
        self.games_lib = {
            'Donkey Kong': Game('Donkey Kong', 3, 2),
            'Super Mario': Game('Super Mario', 5, 3),
            'Tetris': Game('Tetris', 2, 1),
        }
        self.users = {}
        self.admin_user = Admin('admin', 'adminpass')

    def main_menu(self):
        print('Welcome to Game Rental System!')
        print('1. Available Games')
        print('2. Register')
        print('3. Admin Log-in')
        print('4. User Log-in')
        print('5. Exit\n')

        choice = input('Choose an option: ')

        if choice == '1':
            self.display_available_games()
        elif choice == '2':
            self.register()
        elif choice == '3':
            self.admin_login()
        elif choice == '4':
            self.user_login()
        elif choice == '5':
            print('Thank you!')
            quit()

    def display_available_games(self):
        print('Available Games:')
        for game in self.games_lib.values():
            print(game)
        input('Press any key to return to Main Menu')

    def register(self):
        print('Register to access and rent games : )')
        username = input('Enter Username: ')
        password = input('Enter Password: ')
        balance = 0
        points = 0

        self.users[username] = User(username, password)

        while len(password) < 8:
            print('Password must be at least 8 characters long')
            password = input('Enter Password: ')

        print(f'Your username is {username}, your password is {password}, your current balance is {balance}, and your current points are {points}')
        print('Welcome!\n')

        choice = input('Do you wish to Log in(4) or Return to Main Menu?(5): ')
        if choice == '4':
            self.user_login()
        elif choice == '5':
            self.main_menu()
        else:
            print('Invalid Input!')
            self.register()

    def admin_login(self):
        while True:
            username = input('Enter Admin User: ')
            password = input('Enter Admin Password: ')

            if username == self.admin_user.username and password == self.admin_user.password:
                self.admin_menu()
                break
            else:
                print('Invalid Username or Password\n')

    def user_login(self):
        username = input("Username: ")
        password = input("Password: ")
        if username in self.users and self.users[username].password == password:
            print(f'Welcome {username}')
            self.user_menu(username)
        else: 
            print("Wrong username or password")
            self.main_menu()

    def admin_menu(self):
        print('Welcom Admin')
        print('1. Update Library')
        print('2. Exit\n')

        while True:
            choice = input('Enter Choice: ')

            if choice == '1':
                self.admin_edit()
                break
            elif choice == '2':
                self.main_menu()
                break

    def admin_edit(self):
        print("Edit Library")
        print("1. Update Game Quantity")
        print("2. Update Game Cost")
        print("3. Add New Game")
        print("4. Back to Admin Menu")

        choice = input("Enter choice: ")

        if choice == '1':
            self.update_game_quantity()
        elif choice == '2':
            self.update_game_cost()
        elif choice == '3':
            self.add_new_game()
        elif choice == '4':
            self.admin_menu()

    def update_game_quantity(self):
        print("Update Game Quantity")
        game_name = input("Enter game name: ")
        quantity = int(input("Enter new quantity: "))
        if game_name in self.games_lib:
            self.games_lib[game_name].quantity = quantity
            print(f"Quantity of {game_name} updated to {quantity}")
        else:
            print("Game not found")

    def update_game_cost(self):
        print("Update Game Cost")
        game_name = input("Enter game name: ")
        cost = int(input("Enter new cost: "))
        if game_name in self.games_lib:
            self.games_lib[game_name].cost = cost
            print(f"Cost of {game_name} updated to {cost}")
        else:
            print("Game not found")

    def add_new_game(self):
        print("Add New Game")
        game_name = input("Enter game name: ")
        quantity = int(input("Enter quantity: "))
        cost = int(input("Enter cost: "))
        self.games_lib[game_name] = Game(game_name, quantity, cost)
        print(f"Game {game_name} added to library")

    def user_menu(self, username):
        print('Welcome to Game Rental')
        print('1. Rent a game')
        print('2. Return a game')
        print('3. Top up')
        print('4. Check Inventory')
        print('5. Redeem Points')
        print('6. Check points')
        print('7. Exit\n')

        choice = input('Enter Choice: ')

        if choice == '1':
            self.rent_game(username)
        elif choice == '2':
            self.return_game(username)
        elif choice == '3':
            self.top_up(username)
        elif choice == '4':
            self.check_inventory(username)
        elif choice == '5':
            self.redeem_points(username)
        elif choice == '6':
            self.check_points(username)
        elif choice == '7':
            self.main_menu()

    def rent_game(self, username):
        while True:
            try:
                print('Rent a game')
                print(self.games_lib)

                gamename = input('Select Game by typing the game name: ')

                if gamename in self.games_lib and self.games_lib[gamename]['quantity'] > 0:
                    if self.user_acc[username]['balance'] >= self.games_lib[gamename]['cost']:
                        self.user_acc[username]['balance'] -= self.games_lib[gamename]['cost']
                        self.games_lib[gamename]['quantity'] -= 1
                        self.user_acc[username]['points'] += 1
                        if username not in self.user_inventory:
                            self.user_inventory[username] = [gamename]
                        else:
                            self.user_inventory[username].append(gamename)
                        print(f'Game Successfully rented, Remaining balance is: {self.user_acc[username]["balance"]}\n')
                    else:
                        print('Insufficient Balance')
                elif gamename in self.games_lib and self.games_lib[gamename]['quantity'] <= 0:
                    print('Game is out of stock')
                else:
                    print('Invalid game selection')

            except ValueError as e:
                self.user_menu(username)

            choice = input('Enter A to rent another game, enter Y to return to menu: ')
            if choice.lower() == 'y':
                return self.user_menu(username)
            elif choice.lower() != 'a':
                print('Invalid Input. Enter A or Y only')

    def return_game(self, username):
        while True:
            try:
                print("\nReturn a game")
                print(self.user_inventory[username])

                game_name = input("\nEnter the name of the game to return: ")
                
                if game_name in self.user_inventory.get(username, []):
                    self.user_inventory[username].remove(game_name)
                    self.games_lib[game_name]['quantity'] += 1
                    print(f"Game '{game_name}' returned successfully.\n")
                else:
                    print("Game not found in the user's inventory or not rented by the user.\n")

            except ValueError as e:
                self.user_menu(username)
            
            input('Press Enter to return to menu: ')
            self.user_menu(username)

    def top_up(self, username):
        while True:
            try:
                amount = int(input('Enter Amount to Top up: '))

                self.user_acc[username]['balance'] += amount
                print(f'You have deposited {amount}, your new balance is {self.user_acc[username]["balance"]}\n')
            
            except ValueError as e:
                self.user_menu(username)

            input('Press Enter to return to menu: ')
            self.user_menu(username)

    def check_inventory(self, username):
        while True:
            try:
                print()
                if username in self.user_inventory:
                    print(f'Your inventory: {self.user_inventory[username]}\n')
                else:
                    print("Your inventory is empty.\n")

            except ValueError as e:
                self.user_menu(username)

            input('Press Enter to return to menu: ')
            self.user_menu(username)

    def redeem_points(self, username):
        while True:
            try:
                print()
                print('Redeem Points\n')
                
                if self.user_acc[username]["points"] >= 3:
                    print("You can redeem your points to rent a game.")
                    choice = input("Do you want to redeem points? (Y/N): ")
                    if choice.lower() == "y":
                        self.user_acc[username]["points"] -= 3
                        print("Points redeemed successfully!")
                        print(self.games_lib)
                        gamename = input("Select a game by typing the game name: ")
                        if gamename in self.games_lib and self.games_lib[gamename]['quantity'] > 0:
                            self.games_lib[gamename]['quantity'] -= 1
                            self.user_inventory[username] = self.user_inventory.get(username, []) + [gamename]
                            print(f'Game "{gamename}" successfully rented!\n')
                            return self.user_menu(username)
                        else:
                            print('Invalid game selection or game is out of stock')
                            self.redeem_points(username)
                    elif choice == "n":
                        self.user_menu(username)
                    else:
                        print("Invalid input. Please enter Y or N.")
                        self.redeem_points(username)
                else:
                    print("You do not have enough points to redeem.")
                    self.redeem_points(username)
            except ValueError as e:
                self.user_menu(username)

    def check_points(self, username):
        print(f'Available points: {self.user_acc[username]["points"]}\n')
        print('Enter Choice')
        print('1. Redeem points')
        print('2. Exit')
        choice = input('Enter choice: ')
        if choice == '1':
            self.redeem_points(username)
        elif choice == '2':
            return self.user_menu(username)

game_rental_system = GameRentalSystem()
game_rental_system.main_menu()
