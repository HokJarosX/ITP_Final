from classes import transactions
from input.parser import load
from services.expences import catergories_expenses
from services.monthlySummary import monthlySummary
def main():
    tr = load("data/transaction.json")

    report = catergories_expenses(tr)
    print(report, "\n")

    sum = monthlySummary(tr)
    print(sum)

    print(tr)


main()