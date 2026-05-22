from input.parser import load
from classes.transactions import Transaction



def catergories_expenses(transactions):
    expences = {}
    only_expenses = (tr for tr in transactions if tr.getType() == "expense")
    for tr in only_expenses:
        if tr.getType() == "expense":
            cat = tr.getCategory() or "Other"
            expences[cat] = expences.get(cat, 0) + tr.getAmount()
    return expences




def categories_expense():
    return None