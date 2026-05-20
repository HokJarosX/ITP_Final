from classes.transactions import Transaction


def monthlySummary(transactions):
    incomeExpemceConutAndTotal = {"incomeCount": 0,
                    "expensesCount": 0,
                    "totalIncome": 0,
                    "totalExpenses": 0,
                                  "currentBalance":0}


    for transaction in transactions:
        if transaction.getType() == "income":
            incomeExpemceConutAndTotal["incomeCount"] += 1
            incomeExpemceConutAndTotal["totalIncome"] += transaction.getAmount()
            incomeExpemceConutAndTotal["currentBalance"] += transaction.getAmount()

        else:
            incomeExpemceConutAndTotal["expensesCount"] += 1
            incomeExpemceConutAndTotal["totalExpenses"] += transaction.getAmount()
            incomeExpemceConutAndTotal["currentBalance"] -= transaction.getAmount()


    return incomeExpemceConutAndTotal


def detect_overspending():
    return None


def print_overspending_report():
    return None