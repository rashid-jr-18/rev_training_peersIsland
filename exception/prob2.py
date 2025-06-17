class InsufficientFundsError(Exception):
    """Custom exception for insufficient balance"""
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        """
        Withdraws money from the account.
        
        :param amount: Amount to withdraw
        :return: Remaining balance or error message
        """

        try:
            if amount < 0:
                raise ValueError("Withdrawal amount cannot be negative.")
            if amount > self.balance:
                raise InsufficientFundsError("Insufficient balance to withdraw.")
            
            self.balance -= amount
            return f"Withdrawal successful. Remaining balance: ₹{self.balance}"
        
        except ValueError as ve:
            return f"ERROR: {ve}"
        except InsufficientFundsError as ie:
            return f"ERROR: {ie}"
        except Exception as e:
            return f"ERROR: Unexpected exception - {e}"
        

account = BankAccount(100)
print(account.withdraw(150))  # Should raise InsufficientFundsError
print(account.withdraw(-10))  # Should raise ValueError
print(account.withdraw(50))