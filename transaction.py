class InvalidAmountError():
    pass
class InvalidCategoryError:
    pass
class Transaction:
    allow_transaction_type =["food","salary","entertainment","other"]
    def __init__(self,amount,category,description,t_type):
        self.amount = amount
        self.category = category
        self.description = description
        self.t_type = t_type
        self.validate()
    def validate(self):
        if self.amount <= 0:
            raise InvalidAmountError("amount must be in positive value ") 
        if self.category not in self.allow_transaction_type:
            raise InvalidCategoryError(" category must be in food,salary,entertainment,other ")
        if self.t_type not in ["income","expense"]:
            raise ValueError("t_type must be either 'income' or 'expense'")
    def __str__(self):
        return f" Transaction(amount={self.amount}, category='{self.category}', description='{self.description}', t_type='{self.t_type}')"
    def __repr__(self):
        return self.__str__()
        
        

        