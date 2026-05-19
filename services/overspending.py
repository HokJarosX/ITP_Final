from input.parser import load
from services.expences import catergories_expenses


def print(param):
    pass


def round(spent, param):
    pass


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
                "over_by": round(spent-limit, 2)
            }
    return result

     def print_overspending_report(result):
         if not result:
             print("great job! no overspending detected")
             return
         print("\n===== overspending report=====")
         for catagory, info , in result.items():
             print(f"[{catagory.upper()}]")
             print(f"  budget : ${info['budget']}")
             print(f" spent :${info['spent']}")
             print(f" over by : ${info['over-by']}")
             print("======\n")



