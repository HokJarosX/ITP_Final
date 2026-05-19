from input.parser import load

def catergories_expenses(transactions):
    expences = {}
    for tr in transactions:
        if tr.type == "expense":
            cat = tr.category or "Other"
            expences[cat] = expences.get(cat, 0) + tr.amount
    return expences


if __name__=="__main__":
    transactions = load("data/transaction.json")
    print(catergories_expenses(transactions))


def categories_expense():
    return None