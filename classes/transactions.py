class Transaction:
    def __init__(self, type, category, amount, date):
        self.type = type
        self.category = category
        self.amount = amount
        self.date = date

    def __repr__(self):
        return f"{self.type}{self.type.upper()}{self.category or "No category"}{self.amount}$"