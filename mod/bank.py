class BankAccount:
    """Immitation of the bamk account."""

    def __init__(self, balance: int | float = 0) -> None:
        self._balance = balance

    def get_balance(self) -> int | float:
        return self._balance

    def deposit(self, amount: int | float) -> None:
        self._balance += amount

    def withdraw(self, amount: int | float) -> None:
        if amount <= self._balance:
            self._balance -= amount
        else:
            raise ValueError("На счете недостаточно средств")

    def transfer(self, account: "BankAccount", amount: int | float) -> None:
        self.withdraw(amount)
        account.deposit(amount)


account1 = BankAccount(100)
account2 = BankAccount(200)
try:
    account1.transfer(account2, 150)
except ValueError as e:
    print(e)
