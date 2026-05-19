from classes import transactions
from services.overspending import detect_overspending, print_overspending_report
from input.parser import load
from services.expences import catergories_expenses
from services.monthlySummary import monthlySummary

def setBudget(my_budget):
    categories = input("Enter categories: ")
    if categories in my_budget:
        try:
            my_budget[categories] = int(input("Enter integer: "))
        except ValueError:
            print("Invalid input")
    else:
        print("Invalid input")


def UserInterface():

    tr = load("data/transaction.json")
    report = catergories_expenses(tr)
    Msum = monthlySummary(tr)

    my_budgets = {
        "food":50,
        "transport":15,
        "entertainment": 30,
        "shopping":50,
        "bills":100,
        "health":40,
        "education":100,
    }

    result = detect_overspending(tr, my_budgets)

    while True:

        print("\n0. Set a budget")
        print("1. Show all transactions")
        print("2. Show categories")
        print("3. Show monthly summary")
        print("4. Show overspendings")
        print("5. Exit")

        x = int(input("Enter a number: "))
        if x == 0:
            setBudget(my_budgets)
        elif x == 1:
            print(f"All transactions: {tr}")
        elif x == 2:
            print(f"Categories: {report}")
        elif x == 3:
            print(f"Monthly summary: {Msum}")
        elif x == 4:
            result = detect_overspending(tr, my_budgets)
            print_overspending_report(result)
        elif x == 5:
            break



