import app

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.transactions = []

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
        transaction = {'sender': sender, 'recipient': recipient, 'subject': subject, 'amount': amount}
        self.transactions.append(transaction)
        self.accounts[sender.number].subtract_from_balance(amount)
        self.accounts[recipient.number].add_to_balance(amount)
        return transaction




