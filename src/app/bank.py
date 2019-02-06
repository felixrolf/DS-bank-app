class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []
        self.transactions = []

    def open_account(self, account):
        for item in self.accounts:
            assert item['number'] != account['number'], 'Account number 1 already taken!'
        self.accounts.append(account)
        return account

    def add_transaction(self, *, sender, recipient, subject, amount):
        assert amount > 0, 'Amount has to be greater than 0'
        sender_exists = 0
        for item in self.accounts:
            if item['number'] == sender['number']:
                sender_exists = 1
        assert sender_exists == 1, 'Sender has no account yet!'
        recipient_exists = 0
        for item in self.accounts:
            if item['number'] == recipient['number']:
                recipient_exists = 1
        assert recipient_exists == 1, 'Recipient has no account yet!'
        transaction = {'sender': sender, 'recipient': recipient, 'subject': subject, 'amount': amount}
        self.transactions.append(transaction)
        return transaction
