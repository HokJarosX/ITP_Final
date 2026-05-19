from input.parser import load

def catergories_expenses(transactions):
    expences = {}
    for tr in transactions:
        if tr.type == "expense":
            cat = tr.category or "Other"
            expences[cat] = expences.get(cat, 0) + tr.amount
    return expences


