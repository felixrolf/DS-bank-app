class Account:
    def __init__(self, *, firstname, lastname, number, balance=0.0):
        assert isinstance(number, int), 'Number needs to be an integer'
        assert isinstance(balance, float), 'Balance needs to be a float'
        self.firstname = firstname
        self.lastname = lastname
        self.number = number
        self.balance = balance

    def info(self):
        # 'Number 1: Albert Einstein - 100.0 €'
        return f'Number {self.number}: {self.firstname} {self.lastname} - {self.balance} €'

    def has_funds_for(self, amount):
        return self.balance >= amount

    def add_to_balance(self, amount):
        assert amount > 0, 'Amount needs to be greater than 0'
        new_balance = self.balance + amount
        self.balance = new_balance

    def subtract_from_balance(self, amount):
        assert amount < self.balance, 'Account has not enough funds'
        new_balance = self.balance - amount
        self.balance = new_balance





