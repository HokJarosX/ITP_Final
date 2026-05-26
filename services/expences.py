from classes.transactions import Transaction



def catergories_expenses(transactions):
    expences = {}
    total_spen = 0
    only_expenses = (tr for tr in transactions if tr.getType() == "expense")
    for tr in only_expenses:
        cat = tr.getCategory() or "Other"

        amount = tr.getAmount()
        expences[cat] = expences.get(cat, 0) + amount
        total_spen += amount
    report = {}
    for cat, amount in expences.items():
        parcent =  (amount / total_spen) * 100 if amount > 0 else 0
        report[cat] = {
            "spent" : amount,
            "percent %" :  round(parcent , 1)


        }
    return report






def categories_expense():
    return None