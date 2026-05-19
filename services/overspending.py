from input.parser import load
from services.expences import catergories_expenses


def detect_overspending(transactions, budgets):
    if not transactions:
        print("no transactions found")
        return {}
    actual = catergories_expenses(transactions)
    result = {}

    for catagory, limit in budgets.items():
        spent = actual.get(catagory, 0)
        if spent > limit:
            result[catagory] = {
                "budget": limit,
                "spent": round(spent, 2),
                "over_by": round(spent-limit, 2),
                "percent_used": round((spent / limit) * 100)
            }
    return result

def print_overspending_report(result):
    if not result:
        print("great job! no overspending detected")
        return
    print("\n===== overspending report=====")
    for catagory, info in result.items():
        print(f"[{catagory.upper()}]")
        print(f"  budget : ${info['budget']}")
        print(f" spent :${info['spent']}")
        print(f" over by : ${info['over_by']}")
        print(f" used  : {info['percent_used']}% of budget")
    print("======\n")
if __name__=="__main__":
    import os
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    transactions = load(os.path.join(BASE_DIR,"data","transaction.json"))

    my_budgets  = {
        "food": 50,
        "transport":15,
        "entertainment":30,
        "shopping": 50,
        "bills":100,
        "health":40,
        "education":100,

         }
    result = detect_overspending(transactions, my_budgets)
    print_overspending_report(result)



