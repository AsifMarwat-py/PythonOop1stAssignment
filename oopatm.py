class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()
    
    def menu(self):
        while True:
            try:
                user_input = int(input(""" 
                Hello, How would you like to proceed?
                1. Create PIN
                2. Deposit Balance
                3. Withdraw Balance
                4. Check Balance
                5. Exit
                """))
                if user_input == 1:
                    self.create_pin()
                elif user_input == 2:
                    self.deposit_balance()
                elif user_input == 3:
                    self.withdraw()
                elif user_input == 4:
                    self.check_balance()
                elif user_input == 5:
                    print("Goodbye!")
                    break
                else:
                    print("Invalid option. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
    
    def create_pin(self):
        while True:
            pin = input("Enter a numeric PIN (4-6 digits): ")
            if pin.isdigit() and 4 <= len(pin) <= 6:
                self.pin = pin
                print("PIN created successfully.")
                break
            else:
                print("Invalid PIN. Please enter a 4-6 digit numeric PIN.")
    
    def withdraw(self):
        if self._verify_pin():
            try:
                amt = int(input("Enter the amount you want to withdraw: "))
                if amt <= self.balance:
                    self.balance -= amt
                    print("Withdrawal successful.")
                else:
                    print("Insufficient balance.")
            except ValueError:
                print("Please enter a valid amount.")
    
    def deposit_balance(self):
        if self._verify_pin():
            try:
                amt = int(input("Enter the amount you want to deposit: "))
                self.balance += amt
                print("Amount deposited successfully.")
            except ValueError:
                print("Please enter a valid amount.")
    
    def check_balance(self):
        if self._verify_pin():
            print(f"Your current balance is: {self.balance}")
    
    def _verify_pin(self):
        tmp = input("Please enter your PIN: ")
        if tmp == self.pin:
            return True
        else:
            print("Invalid PIN.")
            return False

# Create an instance of Atm
atm = Atm()
