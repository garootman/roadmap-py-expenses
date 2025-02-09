from datetime import datetime


class Expense:
    """
    A class to represent an expense at storage.

    id: A unique identifier for the expense
    amount: How much money was spent
    category: optional, string, a category of exp.
    description: A short description of the expense
    createdAt: The date and time when the expense was created
    updatedAt: The date and time when the expense was last updated

    """

    def __init__(self, id, description, amount, createdAt=None, updatedAt=None, category=None):
        self.id = id
        self.description = description
        if createdAt is None:
            createdAt = datetime.now()
        if updatedAt is None:
            updatedAt = datetime.now()
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        self.category = category
        self.amount = self.check_amount(amount)

   
    def __str__(self):
        return f"expense {self.id}: {self.description}, {self.amount}"

    def __repr__(self):
        return f"expense {self.id}: {self.description}"

    @staticmethod
    def check_amount(amt):
        # check if amount is ok to be used as expense
        # convert to float, positive
        amt = float(amt)
        if amt <=0:
            print ("amount must be >0")
            return None
        return amt
 
    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "amount": self.amount,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            description=data["description"],
            status=data["status"],
            createdAt=data["createdAt"],
            updatedAt=data["updatedAt"],
        )
