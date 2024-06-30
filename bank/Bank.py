class BalanceException(Exception):
    pass

class bank_account:
    def __init__(self, initialAmount, accName):
        self.balance = initialAmount
        self.name = accName
        print(f'Account {self.name} is created. Balance is {self.balance}')
    
    def getBalance(self):
        print(f'\nAccount "{self.name}" balanace: {self.balance:.2f}')

    def deposit(self, amount):
        self.balance = self.balance + amount
        print('Deposit Complete.')
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f'\nSprry, account "{self.name}" only has a balance of {self.balance:.2f}'
            )
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print('\nWithdraw Complete.')
            self.getBalance()
        except BalanceException as error:
            print(f'Withdraw Interupted, {error}')
    
    def transfer(self, amount, account):
        try:
            print('\n************\n\nBeginning Transfer... 🚀')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer complete! ✅\n\n *********')
        except BalanceException as error:
            print(f'Transfer Interrupted. {error}')

class InterestRewaradsAcct(bank_account):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print('\nDeposit Complete.')
        self.getBalance()

class SavingsAcc(InterestRewaradsAcct):
    def __init__(self, initialAmount, accName):
        super().__init__(initialAmount, accName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount - self.fee)
            print('\nWithdraw Complete. ')
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw Interrupted: {error}')

Aicka = bank_account(1000, 'Aicka')

Aicka.getBalance()