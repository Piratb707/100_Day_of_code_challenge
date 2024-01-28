
class BankAccoun:
    def __init__(self, accountHolder):
        self._balance = 0
        self._name = accountHolder
        with open(self._name + 'Ledger.txt', 'w') as LedgerFile:
            LedgerFile.write('Balance is 0 \n')

    def deposi(self, amount):
        if amount <= 0:
            return
        self._balance += amount
        with open(self._name + 'Ledger.txt', 'a') as LedgerFile:
            LedgerFile.write('Deposit ' + str(amount) + '\n')
            LedgerFile.write('Balance is ' + str(self._balance) + '\n')

    def withdraw(self, amount):
        if self._balance < amount < 0:
            return "Not enough money on account"

        self._balance -= amount
        with open(self._name + 'Ledger.txt', 'a') as LedgerFile:
            LedgerFile.write('Withdraw ' + str(amount) + '\n')
            LedgerFile.write('Balance is ' + str(self._balance) + '\n')

acct = BankAccoun('Alice')
acct.deposi(120)
acct.withdraw(40)

acct._balance = 1000000000
acct.withdraw(1000)

acct._name = 'Bob'
acct.withdraw(1000)