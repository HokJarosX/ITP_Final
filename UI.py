from classes import transactions
from filter import FilterCategory
from services.overspending import detect_overspending, print_overspending_report
from input.parser import load
from services.expences import catergories_expenses
from services.monthlySummary import monthlySummary
from services.filter import Filter, FilterData, FilterCategory
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
        print("5. Filter by category")
        print("6. Filter by data")
        print("7. Exit")

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
            inp = input("Enter a category: ")
            MyFilter = FilterCategory(tr, inp)
            print(MyFilter.apply())

        elif x == 6:
            inp = input("Enter a data: ")
            MyFilter = FilterData(tr, inp)
            print(MyFilter.apply())

        elif x == 7:
            break


