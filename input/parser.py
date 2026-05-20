import json
from classes.transactions import Transaction

def successfully(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            print("File loaded successfully")
            return result
        except FileNotFoundError:
            print("File not found")
            return []
    return wrapper

@successfully
def load(path):
    with open(path, 'r') as file:
        data = json.load(file)

    transactions = []

    for i in data:
        transaction = Transaction(
            type = i["type"],
            date = i["date"],
            amount = i["amount"],
            category= i.get("category")
        )
        transactions.append(transaction)
    return transactions

