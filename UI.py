from classes import transactions
from filter import *
from input.parser import load
from services import FinanceTracker
from services.FinanceTracker import  FinanceTracker


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

    transactions = load("data/transaction.json")
    tracker = FinanceTracker(transactions)

    my_budgets = {
        "food":50,
        "transport":15,
        "entertainment": 30,
        "shopping":50,
        "bills":100,
        "health":40,
        "education":100,
    }

    result = tracker.detect_overspending(my_budgets)

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
            print(f"All transactions: ")
            for t in transactions:
                print(t)
        elif x == 2:
            print(f"Categories: {tracker.catergories_expenses()}")
        elif x == 3:
            print(f"Monthly summary: {tracker.monthly_summary()}")
        elif x == 4:
            result = tracker.detect_overspending(my_budgets)
            tracker.print_overspending_report(result)

        elif x == 5:
            inp = input("Enter a category: ")
            MyFilter = FilterCategory(transactions, inp)
            print(MyFilter.apply())

        elif x == 6:
            inp1 = input("Enter a data: ")
            inp2 = input("Enter a second data: ")
            MyFilter = FilterDate(transactions, inp1, inp2)
            print(MyFilter.apply())

        elif x == 7:
            break



