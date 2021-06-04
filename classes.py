import home

class Category:

    # constructor
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    # methods
    def deposit(self, amount):
        self.amount += amount
        return "You have successfully deposited {} in {} category.".format(amount, self.category)

    
    def budget_balance(self):
        return "This is the current balance: {}".format(self.amount)


    def check_balance(self, amount):
        if self.amount >= amount:
            return True
        else:
            return False    

    
    def withdraw(self, amount):
        self.amount -= amount
        return "You have successfully withdrawn {} from the {} category.".format(amount, self.category)


    def transfer(self, amount, category):
        if self.check_balance(amount) is True:
            self.withdraw(amount)
            category.deposit(amount)
            return True
        else:
            return False
        


food_category = Category("Food", 200)
clothing_category = Category("Clothing", 300)
car_category = Category( "Car Expenses", 500)


print(food_category.deposit(250))
print(food_category.budget_balance())
print(food_category.withdraw(50))
print(food_category.budget_balance())