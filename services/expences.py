from input.parser import load

def categories_expenses(transactions):
    expenses = {}
    for tr in transactions:
        if tr.type =="expense":
            cat = tr.category or "Other"
            expenses[cat] = expenses.get(cat,0) + tr.amount
    return expenses