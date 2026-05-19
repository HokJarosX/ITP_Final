from input.parser import load
from services import monthlySummary
from services.expences import categories_expenses
def main():
    tr = load("data/transaction.json")

    report = categories_expenses(tr)
    monthlySummary = monthlySummary(tr)
    print(report)

    print(tr)

main()