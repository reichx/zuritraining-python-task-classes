class Budget:

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    #methods
    def topup(self):
        topup_result = 'Deposit transaction of NGN{}.00 into ' + self.category + ' category is complete.'
        return(topup_result.format(self.amount))
        
            
    def balance(self):
        balance_result = 'Your current balance for ' + self.category + ' category is NGN{}.00'
        return(balance_result.format(self.amount))

    def withdraw(self):
        withdraw_result = 'Withdrawal of NGN{}.00 from ' + self.category + ' category is successful. Transaction complete.'
        return(withdraw_result.format(self.amount))
    
    def transfer(self):
        transfer_result = 'Transfer of NGN{}.00 to ' + self.category + ' category is successful. Transaction complete.'
        return(transfer_result.format(self.amount))

category_0 = Budget("Clothing", 2000)
category_1 = Budget("Food", 3000)
category_2 = Budget("Entertainment", 1500)
category_3 = Budget("Transportation", 1000)

print(category_0.topup())
print(category_1.balance())
print(category_2.withdraw())
print(category_3.transfer())
