import os
import random
from mixins import ScoreMixins
from datetime import datetime

class NumberGuesser(ScoreMixins):
    def __init__(self):
        self.data_folder = 'data'
        self.score_file = os.path.join(self.data_folder, 'highest_score.txt')
        self.load_highest_score_date_file = os.path.join(self.data_folder, 'highest_score_date.txt')

        super().__init__(self.score_file)

        self.create_data_folder()

    def create_data_folder(self):
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)

    def load_highest_score_date(self):
        if os.path.exists(self.load_highest_score_date_file):
            with open(self.load_highest_score_date_file, 'r') as file:
                return file.read()
        return None

    def save_highest_score_and_Date(self, score, date):
        try:
            with open(self.score_file, 'w') as file:
                file.write(str(score))
            with open(self.load_highest_score_date_file, 'w') as file:
                file.write(date)
        except IOError:
            print('Error: Unable to save score and date')

    def play_number_guesser(self):
        secret_number = random.randint(1, 100)
        attempts = 0

        print('Guess the number between 1 - 100')
        print('Enter q to quit.\n')

        while True:
            guess = input('Enter Guess: ')
            if guess.lower() == 'q':
                print('Quitting the Game..')
                break
            
            if not guess.isdigit():
                print('Enter a number')
                continue

            guess = int(guess)
            attempts += 1

            if guess < secret_number:
                print('Too low')
            elif guess > secret_number:
                print('Too High')
            else:
                print(f'You Guessed the number in {attempts} attempts')
                high_score = self.load_highest_score()
                high_score_date = self.load_highest_score_date()
                if high_score is None or attempts < high_score:
                    if high_score is not None:
                        print(f'New Record! Previous Record {high_score} (Achieved on: {high_score_date})')
                    current_datetime = datetime.now().strftime('%Y - %m - %d  %H: %M: %S')
                    self.save_highest_score_and_Date(attempts, current_datetime)
                else:
                    print(f'Fail to achieve new record. Current Record {high_score} (Achieved on {high_score_date})')
                break
        
    def display_menu(self):
        print('\nMenu.')
        print('1. Start Game')
        print('2. View Highest Score')
        print('3. Quit')

    def start(self):
        while True:
            self.display_menu()
            choice = int(input('Enter Choice: '))
            if choice == 1:
                self.play_number_guesser()
            elif choice == 2:
                high_score = self.load_highest_score()
                high_score_date = self.load_highest_score_date()
                if high_score is not None:
                    print(f'Highest score: {high_score} (Achieved on: {high_score_date})')
                else:
                    print('No recorder score yet')
            elif choice == 3:
                print('Exiting the game')
                break
            else:
                print('Invalid Choice')

