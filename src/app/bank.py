class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.transactions = []

    def open_account(self):
        # Add an account
        (number=1, firstname='Albert', lastname='Einstein')
