class Budget:
   balance=0


    def __init__(self,category):
        self.category = category
        



foodCategory = Budget("food")
clothCategory = Budget("Clothes")
bookCategory = Budget("Books")
entertainmentCategory = Budget("entertainment")

    
def deposit(self,amount, selection):
        if selection == None:
            return []
        else:
            self.balance += amount
           
  
    def get_balance(self):
        return self.balance

    def check_funds(self,amount):
        if self.balance< amount:
            return True
        else:
            return False
  
  def withdraw(self, amount, ):
      
    if self.check_funds(amount):
      self.balance -= amount
      return True
    else:
      return False
  
  def transfer(self, amount, selectedCatergory):
    if self.withdraw(amount,"Transfer to " selectedCatergory.category):
     selectedCatergory.deposit(amount,"Transfer from "+self.category)
      return True
    else:
      return False
