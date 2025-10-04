class BankAccount:
    def __init__(self,account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0.0:
            self.balance += amount
        else:
            print(f'Please add positive amount')
            
            
    def withdraw(self,amount):
        if self.balance >= amount and amount > 0.0:
            self.balance -= amount
        else:
            print(f'Sorry, You don\'t have enough balance in your account')
            
            
    def get_balance(self):
        return self.balance
    
    def __str__(self):
        return f'[{self.account_number}] {self.owner_name} → Balance: ${self.balance:.2f}'



class SavingsAccount (BankAccount):
    def __init__(self, account_number, owner_name, balance,interest_rate = 0.05):
        super().__init__(account_number, owner_name, balance)
        self.interest_rate = interest_rate
        

    def add_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        return interest_amount
    

class Bank:
    def __init__(self, accounts = None):
        self.__accounts = accounts if accounts is not None else []
        
    
    def add_account(self,account):
        self.__accounts.append(account)
        
    def find_account(self, account_number):
        find_acc_number = None
        if len(self.__accounts) != 0:
            for acc_number in self.__accounts:
                if acc_number.account_number == account_number:
                    find_acc_number = acc_number
                
        return find_acc_number if find_acc_number is not None else 'Not found'
    

    def show_all_accounts(self):
        if len(self.__accounts) != 0:
            for account in self.__accounts:
                print(f'Account Number: {account.account_number}, Owner: {account.owner_name}, Balance: {account.balance}')
        else:
            print('No accounts available')
            
            
    def deposit_to(self, account_number, amount):
        account = self.find_account(account_number)
        if isinstance(account, BankAccount):
            account.deposit(amount)
        else:
            print('Account not found.')
            

    def withdraw_from(self, account_number, amount):
        account = self.find_account(account_number)
        if isinstance(account, BankAccount):
            account.withdraw(amount)
        else:
            print('Account not found.')
            

# Test run
b1 = Bank()
acc1 = BankAccount("101", "Rahim", 5000)
acc2 = SavingsAccount("102", "Karim", 8000, 0.1)

b1.add_account(acc1)
b1.add_account(acc2)

b1.show_all_accounts()
print()

b1.deposit_to("101", 1000)
b1.withdraw_from("102", 2000)

acc2.add_interest()

b1.show_all_accounts()