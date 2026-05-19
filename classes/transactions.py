class Transaction:
    def __init__(self, type, category, amount, date):
        self.type = type
        self.category = category
        self.amount = amount
        self.date = date

    def __repr__(self):
        cat = self.category if self.category else "No category"
        return f"({self.date} | {self.type.upper()} | {cat} | {self.amount}$)"

