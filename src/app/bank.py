import app
import time
from datetime import date

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.transactions = []
        print(f'Hello customer! You are entering GLS. Please wait a few seconds...')
        time.sleep(1)
        print(f'-- Loading completed --')
        time.sleep(1)
        print()
        print(f'Press [1] for Add Account')
        time.sleep(1)
        print(f'Press [2] for Add Transaction')


    def open_account(self, account):
        assert isinstance(account, app.Account), 'Account should be an app.Account'
        assert account.number not in self.accounts, 'Account number 1 already taken!'
        self.accounts[account.number] = account
        return account

    def add_transaction(self, *, sender, recipient, subject, amount):
        assert amount > 0, 'Amount needs to be greater than 0'
        assert sender.number in self.accounts, 'Sender has no account yet!'
        assert recipient.number in self.accounts, 'Recipient has no account yet!'
        assert sender.balance > amount, 'Account has not enough funds'
        transaction = app.Transaction(sender=sender.number, recipient=recipient.number, subject=subject, amount=amount)
        self.transactions.append(transaction)
        self.accounts[sender.number].subtract_from_balance(amount)
        self.accounts[recipient.number].add_to_balance(amount)
        return transaction


        #print(f'Die Summe aller Transaktionen beträgt {sum.transactions}')




