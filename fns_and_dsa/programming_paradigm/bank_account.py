class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance

def deposit(self, amount):
        """Adds the specified amount to the account balance."""
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be positive.")

def withdraw(self, amount):
        """Deducts the amount from the balance if sufficient funds exist."""
        if amount <= self._account_balance:
            self._account_balance -= amount
            return True
        else:
            print("Insufficient funds.")
            return False

def display_balance(self):
        """Displays the current account balance."""
        print(f"Current Balance: ${self._account_balance:.2f}")