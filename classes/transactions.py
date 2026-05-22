class Transaction:
    def __init__(self, type, category, amount, date):
        self._type = type
        self._category = category
        self._amount = amount
        self._date = date


    def __repr__(self):
        return f"{self._type} {self._type.upper()} {self._category or 'No category'} {self._amount}$"

    def getType(self):
        return self._type
    def getCategory(self):
        return self._category
    def getAmount(self):
        return self._amount
    def getDate(self):
        return self._date

    def __str__(self):
        return (f"|type = {self._type}|"
                f"|category = {self._category}|"
                f"|amount = {self._amount}|"
                f"|date = {self._date}|")
    def __iter__(self):
        return iter([self.type,self.category,self.amount,self.date])