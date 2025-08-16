class BankAccount:
    def __init__(self,balance):
        self._balance=balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, current_amount):
        if current_amount<0 :
            raise ValueError("Invalid Amount")
        self._balance=current_amount

    @balance.deleter
    def balance(self):
        print("Amount has been removed")

bal=BankAccount(50)
print(f"Here is your Bank balance : {bal.balance}")

bal.balance += 20
print(f"Here is your Bank balance : {bal.balance}")


