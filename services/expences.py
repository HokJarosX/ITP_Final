from input.parser import load
from classes.transactions import Transaction


def catergories_expenses(transactions):
    expences = {}
    for tr in transactions:
        if tr.getType() == "expense":
            cat = tr.getCategory() or "Other"
            expences[cat] = expences.get(cat, 0) + tr.getAmount()
    return expences


if __name__=="__main__":
    transactions = load("data/transaction.json")
    print(catergories_expenses(transactions))


def categories_expense():
    return None