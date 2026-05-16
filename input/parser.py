import json
from classes.transactions import Transaction

def load(path):
    try:
        with open(path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("File not found")
        return []

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

