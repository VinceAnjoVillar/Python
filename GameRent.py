game_library = {
    "Donkey Kong" : {"Quantity" : 3, "Cost" : 2},
    "Super Mario Bros" : {"Quantity" : 5, "Cost" : 2},
    "Tetris" : {"Quantity" : 2, "Cost" : 1},
}
user_account ={"Ian" :{"password" : "a", "balance": 10, "points": 0}}

user_rented = {}

admin_username = "admin"
admin_password = "adminspass"

def main():
    while True:
        try:
            print("Welcome to Game Rental Store")
            print("1. Sign Up")
            print("2. Sign In")
            print("3. Sign In as Administrator")
            print("4. Exit")
            choice = int(input("Enter your choice: "))

            while True:
                if choice == 1:
                    sign_up()
                if choice == 2:
                    sign_in()
                if choice == 3:
                    admin()
                if choice == 4:
                    print("Exiting...")
                    exit()
                else:
                    return
        except ValueError as e:
            print("")

def sign_up():
    while True:
        try:
            username = input("Enter Username (leave blank to go back): ")
            balance = 0
            points = 0
            if not username:
                main()
            if username in user_account:
                print("Username already exists. Enter a different username")
                continue
            while True:
                try: 
                    password = input("Input password (at least 9 characters): ")
                    if len(password) < 8:
                        print("Password is not at least 8 characters")
                        continue
                    if len(password) > 8:
                        user_account[username] = {"password" : password, "balance" : balance, "points" : points}  
                        print("Sign Up successful")
                        main()
                    else:
                        print("Invalid input.")
                        continue 
                except ValueError as e:
                    print(e)
                    sign_up()
        except ValueError as e:
            print(e)
            sign_up()

def sign_in():
    print("Sign In")
    while True:
        try:
            username = input("Enter username (leave blank to go back): ")
            if not username:
                main()
            password = input("Enter password: ")
            if user_account.get(username) and user_account[username]['password'] == password:
                print("Login Successful")
                rentalmain(username)
            else:
                print("Invalid username or password")
        except ValueError as e:
            print(e)
            main()

def rentalmain(username):
    print(f"Welcome to Game Rental Store {username}")
    print("1. Rent")
    print("2. Return")
    print("3. Top-Up")
    print("4. Display Games")
    print("5. Check Points and Balance")
    print("6. Check recently rented game")
    print("7. Log out")
    choice = int(input("Enter your choice: "))

    if not choice:
        rentalmain(username)
    else:
        while True:
            if choice == 1:
                rent(username)
            if choice == 2:
                returnitem(username)
            if choice == 3:
                top_up(username)
            if choice == 4:
                display_available_games(username)
            if choice == 5:
                checkpoints(username)
            if choice == 6:
                latest_rent(username)
            if choice == 7:
                main()
            else:
                rentalmain(username)
    
def rent(username):
    while True:
        try:
            print("Rent a game")
            print(game_library)

            gamename = input("Select Game (leave blank to go back): ")

            if gamename not in game_library:
                print("Game is not on the database. Try again")
                rent(username)
            if not gamename:
                rentalmain(username)
            if game_library[gamename]['Quantity'] <= 0:
                print("Cannot Rent")
            if game_library[gamename]['Quantity'] > 0:
                print("1. Pay using Balance")
                print("2. Pay using points: ")
                pay = int(input("Choose how to pay: "))

                if pay == 1:
                    if user_account[username]['balance'] <= 0:
                        print("Not enough balance to rent. Top up")
                        rent(username)
                    else:
                        user_account[username]['balance'] -= game_library[gamename]['Cost']
                        if game_library[gamename]['Quantity'] > 0:
                            user_account[username]['points'] += float(game_library[gamename]['Cost']) // 2
                            game_library[gamename]['Quantity'] -=1
                            print(f"Rented Successfully. User Balance: {user_account[username]['balance']}, Points: {user_account[username]['points']} ")
                            user_rented[username] = {"Rented Game" : gamename, "Returned" : "No"}
                        else:
                            return
                if pay == 2:
                    if user_account[username]['points'] <= game_library[gamename]['Cost']:
                        print("Not enough points to rent.")
                        continue
                    else:
                        user_account[username]['points'] -= game_library[gamename]['Cost']
                        game_library[gamename]['Quantity'] -=1
                        print(f"Rented Successfully. User Balance: {user_account[username]['balance']}, Points: {user_account[username]['points']} ")
                        user_rented[username] = {"Rented Game" : gamename, "Returned" : "No"}
                        return
                else:
                    return
        except ValueError as e:
            rentalmain(username)


def returnitem(username):
    while True:
        try:
            print("Return Item")
            item_to_return = input("Enter the name of the item you want to return: ")

            if item_to_return not in game_library:
                print("Invalid Input try again")
                returnitem(username)
            else:
                quantity_of_item = int(input("Enter the quantity of item to return: "))
                game_library[item_to_return]['Quantity'] += quantity_of_item
                user_rented[username] = {"Rented Game" : item_to_return, "Returned" : "Yes"}
                print(f"Successfully returned {item_to_return}, Quantity: {quantity_of_item}")
                rentalmain(username)
        except ValueError as e:
            rentalmain(username)

def top_up(username):
    while True:
        try:
            print("Top Up")
            print(f"Username: {username}, Current Balance: {user_account[username]['balance']}")

            topup_amt = float(input("Enter amount to top up: "))
            user_account[username]['balance'] += topup_amt
            print("Top up Successful")
            print(f"Username: {username}, New Balance: {user_account[username]['balance']}")
            rentalmain(username)
        except ValueError as e:
            rentalmain(username)
    
def display_available_games(username):
    print(f"Available Games: {game_library}")
    rentalmain(username)

def checkpoints(username):
    print(f"Available Balance: {user_account[username]['balance']}, Points: {user_account[username]['points']}")

def latest_rent(username):
    print(f"Last Rented Game: {user_rented[username]['Rented Game']}, Returned: {user_rented[username]['Returned']}")


def admin():
    print("Admin login")
    username = input("Enter username (leave blank to go back): ")
    if not username:
        main()
    if username == admin_username:
        password = input("Enter password: ")
        if password == "adminpass":
            print("Log In Successful")
            adminmenu()
        else:
            print("Invalid Password or Username.")
            admin()
    else: 
        print("Try Again")
        admin()

def adminmenu():
    while True: 
        try:
            print("Welcome Admin")
            print(f"Current Game Library: {game_library}")
            print("1. Add Quantity")
            print("2. Increase Price")
            print("3. Add Game")
            print("4. View Rent History")
            print("5. Sign out")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                admin_add_quantity()
            if choice == 2:
                increase_price()
            if choice == 3:
                add_game()
            if choice == 4:
                print(user_rented)
                adminmenu()
            if choice == 5:
                main()
            else:
                return 
        except ValueError as e:
            main()

def admin_add_quantity():
    while True: 
        try:    
            print(game_library)
            game_name = input("Enter the name of the item you want to add a quantity (leave blank to go back): ")
            quantity_of_item = int(input("Enter the quantity of the game: "))
            game_library[game_name]['Quantity'] += quantity_of_item


            if not game_name:
                adminmenu()
            if game_name is int:
                print("Invalid Input. Try again")
                admin_add_quantity()
            else:
                print(f"Successfully added another {quantity_of_item} copies {game_name}. ")
                print(f"Updated Library: {game_library}")
                print("1. Add quantity to another game")
                print("2. Go back")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    admin_add_quantity()
                if choice == 2:
                    adminmenu()
                else:
                    print("Invalid Input")
        except ValueError as e:
            adminmenu()

def increase_price():
    while True: 
        try:
            print("Change Price")
            print(game_library)

            game_name = input("Enter the name of the item you want to increase the price (leave blank to go back): ")

            if not game_name:
                adminmenu()
            if game_name not in game_library:
                print("Game Does not exist. Try again")
            else:
                new_price = int(input("Enter the new price of the game: "))
                game_library[game_name]['cost'] = new_price
                print("Price changed successfully.")

                print("1. To change the price of another game.")
                print("2. Go back to main menu")
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    increase_price()
                if choice == 2:
                    adminmenu()
                else:
                    print("Invalid Input")
                    increase_price()

        except ValueError as e:
            adminmenu()

def add_game():
    while True: 
        try:
            print("Add Game")
            print(game_library)
            new_game_name = input("Input the name of the game you want to add: ")

            if new_game_name in game_library:
                print("This Game is already on the database. Try again.")
                add_game()
            else:
                new_game_quantity = int(input("Input the quantity of the new game: "))

                if new_game_quantity <= 0:
                    print("Quantity cant be less than 0.")
                    continue
                else:
                    new_game_cost = int(input("Enter the price of the new game: "))

                    if new_game_cost == 0:
                        print("Are you sure you want to add a free game?")
                        choice = str(input("(y/n):"))
                        if choice == 'y':
                            game_library[new_game_name] = {"Quantity" : new_game_quantity, "Cost" : new_game_cost}
                            print(f"{game_library[new_game_name]} Successfully Added a FREE game to the Library")

                            print(f"Updated Library: {game_library}")

                            choice = str(input("Would you like to add another game? (y/n): "))
 
                            if choice == 'y':
                                add_game()
                            else:
                                adminmenu()
                        else:
                            continue

                    if new_game_cost <= 0:
                        print("Cost can't be less than 0")
                        continue
                    else:
                        game_library[new_game_name] = {"Quantity" : new_game_quantity, "Cost" : new_game_cost}

                        print(f"{game_library[new_game_name]} Successfully Added to Library")

                        print(f"Updated Library: {game_library}")

                        choice = str(input("Would you like to add another game? (y/n): "))
 
                        if choice == 'y':
                            add_game()
                        else:
                            adminmenu()
        except ValueError as e:
            adminmenu()

main()
