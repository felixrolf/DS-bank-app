class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts=[]
        self.transactions=[]

    def open_account(self,account):
        for item in self.accounts:
            assert item["number"] != account["number"],"Account number 1 already taken!"
        self.accounts.append(account)
        return account

    def add_transaction(self,*,sender, recipient, subject, amount):
        message = "Amount has to be greater than 0"
        assert amount > 0, message
        Sendervorhanden=0
        for item in self.accounts:
            if item["number"] == sender["number"]:
                Sendervorhanden=1
        assert Sendervorhanden == 1, "Sender has no account yet!"
        Empfängervorhanden = 0
        for item in self.accounts:
            if item["number"] == recipient["number"]:
                Empfängervorhanden = 1
        assert Empfängervorhanden == 1, "Recipient has no account yet!"
        transaction= {"sender":sender, "recipient":recipient, "subject":subject, "amount":amount}
        self.transactions.append(transaction)
        return transaction
