admin_pss = input('Enter Master password:  ')

def view_pass():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            User_name, user_pass = data.split('|')
            print(f'User: {User_name}, Password: {user_pass}')

def add_pass():
    User_name = input('Enter Username: ')
    user_pass = input('Enter Password: ')

    with open('password.txt', 'a') as f:
        f.write(f'{User_name} | {user_pass}\n')


while True:
    mode = input('Would you like to ADD a new accounts or VIEW existing accounts(type add to add and type view to view, type Q to exit): ')

    if mode.upper() == 'Q':
        break

    if mode.lower() == 'add':
        add_pass()
    elif mode.lower() == 'view':
        view_pass()
    else:
        print('Invalid input')
        continue

