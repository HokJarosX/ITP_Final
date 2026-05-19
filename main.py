from input.parser import load
from services.expences import catergories_expenses

def main():
    tr = load("data/transaction.json")

    report = catergories_expenses(tr)

    print(f"All transactions: {tr}")

    print(f"Часть Абыля(категории):{report}")

main()