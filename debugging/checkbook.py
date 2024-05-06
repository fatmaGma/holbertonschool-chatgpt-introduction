class Checkbook:
    def __init__(self):
        """
        Initialize a new Checkbook object with a balance of 0.0.
        """
        self.balance = 0.0
    
    def deposit(self, amount):
        """
        Deposit the specified amount into the checkbook balance.
        Args:
        amount (float): The amount to deposit.
        Prints:
        - A message indicating the deposited amount.
        - The current balance after the deposit.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))
    
    def withdraw(self, amount):
        """
        Withdraw the specified amount from the checkbook balance if sufficient funds are available.
        Args:
        amount (float): The amount to withdraw
        Prints:
        - A message indicating the withdrawn amount and the current balance if the withdrawal is successful.
        - An error message if there are insufficient funds.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
             self.balance -= amount
             print("Withdrew ${:.2f}".format(amount))
             print("Current Balance: ${:.2f}".format(self.balance))
     
    def get_balance(self):
        """
        Print the current balance of the checkbook.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main function to interact with the Checkbook object.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            amount = float(input("Enter the amount to deposit: $"))
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = float(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
