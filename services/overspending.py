from input.parser import load
from services.expences import catergories_expenses


def detect_overspending(transactions, budgets):
    actual = catergories_expenses(transactions)
    result = {}

    for catagory, limit in budgets.items():
        spent = actual.get(catagory, 0)
        if spent > limit:
            result[catagory] = {
                "budget": limit,
                "spent": spent,
                "over_by": spent - limit,
            }
    return result

def print_overspending_report(result):
    for catagory, info in result.items():
        print(f"{catagory}: overspent by${info['over_by']}")
def get_default_budgets():
    return{
        "food":50,
        "transport":15,
        "shopping": 50
    }
if __name__=="__main__":
    transactions = load("data/transaction.json")

    result = detect_overspending(
        transactions, get_default_budgets()
    )

    print_overspending_report(result)


